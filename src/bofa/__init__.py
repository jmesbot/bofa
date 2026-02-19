from __future__ import annotations

from importlib import metadata

try:
    __version__ = metadata.version("bofa")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"


def main():
    from bofa.cli import main as cli_main

    cli_main()
