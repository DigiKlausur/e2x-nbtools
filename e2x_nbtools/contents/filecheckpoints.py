import os
import re
import glob
import datetime

from notebook.services.contents.filecheckpoints import FileCheckpoints
from traitlets import Integer


class E2XFileCheckpoints(FileCheckpoints):

    number_of_checkpoints = Integer(5, config=True)

    def make_checkpoint(self, contents_mgr, path):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        checkpoint_id = "checkpoint-" + timestamp
        src_path = contents_mgr._get_os_path(path)
        dest_path = self.checkpoint_path(checkpoint_id, path)
        print("Saving at", dest_path)
        self._copy(src_path, dest_path)
        return self.checkpoint_model(checkpoint_id, dest_path)

    def create_checkpoint(self, contents_mgr, path):
        checkpoints = self.list_checkpoints(path)
        if len(checkpoints) < self.number_of_checkpoints:
            return self.make_checkpoint(contents_mgr, path)
        res = self.make_checkpoint(contents_mgr, path)
        checkpoints = self.list_checkpoints(path)[self.number_of_checkpoints:]
        print("To delete")
        print(checkpoints)
        for checkpoint in checkpoints:
            self.delete_checkpoint(checkpoint["id"], path)
        return res

    def list_checkpoints(self, path):
        """list the checkpoints for a given file
        This contents manager currently only supports one checkpoint per file.
        """
        path = path.strip("/")
        checkpoint_ids = self.find_checkpoint_ids(os.path.splitext(path)[0])

        return sorted(
            [
                self.checkpoint_model(cid, self.checkpoint_path(cid, path))
                for cid in checkpoint_ids
                if os.path.isfile(self.checkpoint_path(cid, path))
            ],
            key=lambda x: x["last_modified"],
            reverse=True,
        )

    def find_checkpoint_ids(self, nb_name):
        path = os.path.join(self.checkpoint_dir, nb_name)
        pattern = f"{path}-checkpoint*.ipynb"
        checkpoints = [
            os.path.splitext(os.path.basename(path))[0] for path in glob.glob(pattern)
        ]
        ids = [
            re.search(f"{nb_name}-(.*)", checkpoint).groups()[0]
            for checkpoint in checkpoints
        ]
        return ids
