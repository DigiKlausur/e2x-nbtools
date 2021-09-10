import os
import time
import unittest

from tempfile import TemporaryDirectory
from notebook.services.contents.largefilemanager import LargeFileManager

from e2x_nbtools.contents.filecheckpoints import E2XFileCheckpoints


class TestE2XFileCheckpoints(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = TemporaryDirectory()
        self.contents_mgr = LargeFileManager()
        self.contents_mgr.checkpoint_class = E2XFileCheckpoints

        self.contents_mgr.checkpoints = E2XFileCheckpoints()
        self.contents_mgr.root_dir = self.tmp_dir.name
        self.contents_mgr.checkpoints.root_dir = self.tmp_dir.name

    def createNotebook(self):
        return self.contents_mgr.new_untitled(path='', ext=".ipynb")

    def testListCheckpoints(self):
        self.contents_mgr.checkpoint_class.number_of_checkpoints = 2
        path = self.createNotebook()['path']
        time.sleep(1)
        assert len(self.contents_mgr.list_checkpoints(path)) == 1
        time.sleep(2)
        self.contents_mgr.create_checkpoint(path)
        assert len(self.contents_mgr.list_checkpoints(path)) == 2
        time.sleep(2)
        self.contents_mgr.create_checkpoint(path)
        assert len(self.contents_mgr.list_checkpoints(path)) == 2

    def testRemoveCheckpoints(self):
        self.contents_mgr.checkpoint_class.number_of_checkpoints = 2
        path = self.createNotebook()['path']
        time.sleep(1)
        assert len(self.contents_mgr.list_checkpoints(path)) == 1
        time.sleep(2)
        self.contents_mgr.create_checkpoint(path)
        assert len(self.contents_mgr.list_checkpoints(path)) == 2
        checkpoints = self.contents_mgr.list_checkpoints(path)
        self.contents_mgr.delete_checkpoint(checkpoints[0]['id'], path)
        assert len(self.contents_mgr.list_checkpoints(path)) == 1

    def tearDown(self):
        self.tmp_dir.cleanup()

