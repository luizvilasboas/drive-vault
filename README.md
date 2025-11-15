# drive-vault

> A Python application to create backups of local files and securely sync them with Google Drive.

## About the Project

Drive Vault is a Python application designed to simplify your backup routine. It helps you create backups of important files or folders on your system and securely syncs them with your Google Drive account, keeping your files safe in the cloud with ease.

Key features include:
*   **Automated Backups**: Select and schedule files or folders to back up regularly.
*   **Google Drive Sync**: Seamlessly upload and sync backups with your Google Drive account.
*   **File Filtering**: Choose specific file types or exclude certain files from backups.
*   **Error Handling**: Robust error detection and logging for seamless operation.

## Tech Stack

*   [Python](https://www.python.org/)
*   [Poetry](https://python-poetry.org/)

## Usage

Below are the instructions for you to set up and run the project locally.

### Prerequisites

You need to have the following software installed to run this project:

*   [Python](https://www.python.org/downloads/) (3.8 or higher)
*   [Poetry](https://python-poetry.org/docs/#installation)

### Installation and Setup

Follow the steps below:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/luizvilasboas/drive-vault.git
    ```

2.  **Navigate to the project directory**
    ```bash
    cd drive-vault
    ```

3.  **Install dependencies**
    ```bash
    poetry install
    ```

### Configuration

Before running the application, you must configure your Google Drive API credentials. Follow the official [Google Drive API Documentation](https://developers.google.com/drive/api/v3/quickstart/python) to create a `credentials.json` file and obtain the necessary tokens.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue in the [issue tracker](https://github.com/luizvilasboas/drive-vault/issues).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
