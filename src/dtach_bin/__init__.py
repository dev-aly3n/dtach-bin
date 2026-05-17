"""Precompiled dtach binary, shipped as platform-specific wheels.

After `pip install dtach-bin`, the `dtach` binary is placed in the
active venv's ``bin/`` directory by pip. Use it directly via subprocess
(if the venv's ``bin/`` is on PATH), or call ``dtach_bin.path()`` for
an absolute path that works even when the venv's ``bin/`` isn't on PATH
(e.g. with ``uv tool install`` and ``pipx`` layouts).
"""

from __future__ import annotations

import os
import shutil
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

try:
    __version__ = version("dtach-bin")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"


def path() -> str:
    """Return the absolute path to the dtach binary.

    Search order:
      1. ``<sys.prefix>/bin/dtach`` — where pip drops the binary from the
         wheel's ``shared-scripts`` slot. This catches ``uv tool install``,
         ``pipx``, and any other venv layout where the venv's ``bin/`` is
         not on the calling shell's PATH.
      2. ``shutil.which("dtach")`` — PATH lookup, which finds the system
         or Homebrew dtach when this package isn't being used.

    Raises FileNotFoundError only if neither succeeds.
    """
    candidate = Path(sys.prefix) / "bin" / "dtach"
    if candidate.exists() and os.access(candidate, os.X_OK):
        return str(candidate)
    p = shutil.which("dtach")
    if p is not None:
        return p
    raise FileNotFoundError(
        "dtach binary not found. Expected at one of:\n"
        f"  {candidate}\n"
        "  or on PATH via `shutil.which`.\n"
        "Was `pip install dtach-bin` actually completed in this environment?"
    )
