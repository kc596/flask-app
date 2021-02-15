import os
import threading


"""
configs read from env variables
"""


_profile = None
_build_ver = None
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
    return _profile


def get_build_version():
    global _build_ver
    if _build_ver is None:
        with _lock:
            if _build_ver is None:
                try:
                    _build_ver = os.environ["BUILD_NUMBER"]
                except KeyError:
                    _build_ver = "000000_0"
    return _build_ver
