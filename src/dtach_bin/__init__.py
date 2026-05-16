"""Precompiled dtach binary, shipped as platform-specific wheels.

After `pip install dtach-bin`, the `dtach` binary is on PATH (placed in
the active venv's bin/ directory by pip). Use it directly via subprocess,
or call ``dtach_bin.path()`` for the absolute path.
"""

from __future__ import annotations

import shutil
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dtach-bin")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"


def path() -> str:
    """Return the absolute path to the dtach binary.

    Raises FileNotFoundError if dtach is not on PATH — which shouldn't
    happen after a successful ``pip install dtach-bin``.
    """
    p = shutil.which("dtach")
    if p is None:
        raise FileNotFoundError(
            "dtach binary not found on PATH — was `pip install dtach-bin` "
            "actually completed in this environment?"
        )
    return p
