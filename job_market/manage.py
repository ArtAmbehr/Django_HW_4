#!/usr/bin/env python
"""Some infos"""
import os
import sys


def main():
    """Interesting information"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Some kind of info"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
