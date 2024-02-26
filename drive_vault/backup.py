import os
from datetime import datetime
from zipfile import ZipFile, ZIP_DEFLATED


class Backup:
    """Helper class for creating zip backups."""

    @staticmethod
    def create(directories: list[str]) -> str:
        """Creates a zip backup of the specified directories.

        Args:
            directories: A list of directories to include in the backup.

        Returns:
            The name of the created backup zip file.
        """

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"backup_{current_time}.zip"

        try:
            with ZipFile(backup_filename, "w", compression=ZIP_DEFLATED) as zipf:
                for directory in directories:
                    for root, _, files in os.walk(directory):
                        for file in files:
                            try:
                                zipf.write(os.path.join(root, file), os.path.relpath(
                                    os.path.join(root, file), os.path.join(directory, "..")))
                            except IOError as e:
                                print(
                                    f"Warning: Error adding {file} to archive: {e}")
        except IOError as e:
            print(f"Error creating backup: {e}")
            return ""  # Or raise an exception for better control

        return backup_filename
