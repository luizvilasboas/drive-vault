import unittest
import shutil
import os
from drive_vault.backup import Backup
import zipfile


class TestBackup(unittest.TestCase):
    def setUp(self):
        self.dir1 = os.path.join(os.getcwd(), 'test_dir1')
        self.dir2 = os.path.join(os.getcwd(), 'test_dir2')
        os.makedirs(self.dir1, exist_ok=True)
        os.makedirs(self.dir2, exist_ok=True)

        with open(os.path.join(self.dir1, 'file1.txt'), 'w') as f:
            f.write('Content of file1')
        with open(os.path.join(self.dir2, 'file2.txt'), 'w') as f:
            f.write('Content of file2')

    def tearDown(self):
        shutil.rmtree(self.dir1)
        shutil.rmtree(self.dir2)

    def test_zip_multiple_directories(self):
        """
        Test that the function successfully zips multiple directories.
        """

        directories = [self.dir1, self.dir2]

        output_zip_got = Backup.create(directories)

        self.assertTrue(os.path.exists(output_zip_got))

        with zipfile.ZipFile(output_zip_got, 'r') as zipf:
            print(zipf.namelist())
            print(os.path.relpath('test_dir1/file1.txt'))
            self.assertIn(os.path.relpath('test_dir1/file1.txt'), zipf.namelist())
            self.assertIn(os.path.relpath('test_dir2/file2.txt'), zipf.namelist())

        os.remove(output_zip_got)


if __name__ == '__main__':
    unittest.main()
