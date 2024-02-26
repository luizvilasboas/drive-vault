import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


class Drive:
    __SCOPES = ["https://www.googleapis.com/auth/drive"]
    __TOKEN_FILENAME = "token.json"

    def __init__(self) -> None:
        self.creds = self.__auth_google_drive()

    def __auth_google_drive(self):
        """ Authenticates with Google Drive and stores credentials

        Returns:
            Credentials: Validated credentials object for accessing Google Drive
        """

        token_path = Path.home() / os.path.join(".config",
                                                "drive_vault", self.__TOKEN_FILENAME)

        creds = None

        if token_path.exists():
            creds = Credentials.from_authorized_user_file(str(token_path))

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.__SCOPES)
                creds = flow.run_local_server(port=0)
                token_path.parent.mkdir(parents=True, exist_ok=True)
                with open(str(token_path), 'w') as token:
                    token.write(creds.to_json())

        return creds

    def upload(self, zip_file: str) -> None:
        service = build('drive', 'v3', credentials=self.creds)

        folder_name = 'backup'
        folder_id = None
        result = service.files().list(
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            spaces='drive',
            fields='files(id)'
        ).execute()

        items = result.get('files', [])

        if not items:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = service.files().create(body=folder_metadata, fields='id').execute()
            folder_id = folder.get('id')
        else:
            folder_id = items[0]['id']

        file_metadata = {
            'name': os.path.basename(zip_file),
            'parents': [folder_id]
        }

        media = MediaIoBaseUpload(
            open(zip_file, 'rb'),
            mimetype='application/zip'
        )

        service.files().create(body=file_metadata, media_body=media).execute()

    def list(self) -> list[str]:
        service = build('drive', 'v3', credentials=self.creds)

        folder_name = 'backup'
        folder_id = None

        result = service.files().list(
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            spaces='drive',
            fields='files(id)'
        ).execute()

        items = result.get('files', [])

        if not items:
            return []

        folder_id = items[0]['id']

        result = service.files().list(
            q=f"'{folder_id}' in parents and mimeType='application/zip' and trashed=false",
            spaces="drive",
            fields="files(name)"
        ).execute()

        files = result.get('files', [])
        zip_file_names = [file.get('name') for file in files]

        return zip_file_names

    def remove(self, backup_name: str) -> bool:
        """
        Removes a backup .zip file by name.

        Args:
          backup_name: The name of the backup file to remove.

        Returns:
          True if the file was removed successfully, False otherwise.
        """

        service = build('drive', 'v3', credentials=self.creds)

        folder_name = 'backup'
