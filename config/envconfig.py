import os
import threading


"""
configs read from env variables
"""


_profile = None
_lock = threading.Lock()


def get_profile():
    global _profile
    if _profile is None:
        with _lock:
            if _profile is None:
                try:
                    _profile = os.environ["SSP_REGION"]
                except KeyError:
                    _profile = "local"
                print("using profile", _profile)  # TODO: use logger
    return _profile
