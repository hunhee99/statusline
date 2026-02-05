from .core import StatusLine
from importlib.metadata import version, PackageNotFoundError

__all__ = ["StatusLine"]

try:
    __version__ = version("statusline")
except PackageNotFoundError:
    __version__ = "0.0.0"