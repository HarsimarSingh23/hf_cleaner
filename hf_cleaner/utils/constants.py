import os

PLATFORM = ["darwin", "linux", "win32"]

CACHE_LOC = {
    "darwin": os.path.expanduser("~/.cache/huggingface/hub"),
    "linux": os.path.expanduser("~/.cache/huggingface/hub"),
    "win32": os.path.join(os.path.expandvars("%USERPROFILE%"), ".cache", "huggingface", "hub")

}
