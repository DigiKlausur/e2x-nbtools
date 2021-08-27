import os
from os.path import join as pjoin


def _jupyter_nbextension_paths():
    root = os.path.dirname(__file__)
    base_path = pjoin(root, "nbextensions")

    paths = [
        dict(
            section="notebook",
            src=pjoin(base_path, "checkpoints"),
            dest="checkpoints",
            require="checkpoints/main",
        )
    ]

    return paths
