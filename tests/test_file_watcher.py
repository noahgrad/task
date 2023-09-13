import unittest
import os
import shutil
from unittest.mock import patch
from lemonade_task.file_watcher import process_file, Watcher, Handler

class TestFileWatcher(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_dir'
        self.history_dir = 'history'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.history_dir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.history_dir)

    def test_process_file(self):
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('test content')

        def dummy_processing_func(filepath):
            with open(filepath, 'a') as f:
                f.write(' processed')

        process_file(test_file_path, {'txt': dummy_processing_func}, self.history_dir)

        self.assertFalse(os.path.exists(test_file_path))
        self.assertTrue(os.path.exists(os.path.join(self.history_dir, 'test_file.txt')))

        with open(os.path.join(self.history_dir, 'test_file.txt'), 'r') as f:
            content = f.read()
        self.assertEqual(content, 'test content processed')

    def test_watcher_init(self):
        watcher = Watcher(self.test_dir, {})
        self.assertEqual(watcher.DIRECTORY_TO_WATCH, self.test_dir)

    @patch('lemonade_task.file_watcher.process_file')
    def test_watcher_process_existing_files(self, mock_process_file):
        watcher = Watcher(self.test_dir, {})
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('test content')

        watcher.process_existing_files()
        mock_process_file.assert_called_with(test_file_path, {})

    @patch('lemonade_task.file_watcher.process_file')  # Replace 'your_module' with the actual module name
    def test_handler_process(self, mock_process_file):
        handler = Handler({})
        class DummyEvent:
            is_directory = False
            event_type = 'created'
            src_path = 'dummy_path'

        handler.process(DummyEvent())
        mock_process_file.assert_called_with('dummy_path', {})

if __name__ == '__main__':
    unittest.main()
