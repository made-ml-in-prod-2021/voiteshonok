import os
import hydra


def get_path_from_root(path: str) -> str:
    root = hydra.utils.get_original_cwd()
    return os.path.join(root, path)
