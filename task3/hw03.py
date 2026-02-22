import sys
from pathlib import Path

from colorama import Fore, Style, init

init(autoreset=True)


def print_directory_tree(directory: Path, indent: str = "") -> None:
    """Recursively print the directory tree with colored output.

    Directories are printed in blue; files are printed in green.

    Args:
        directory: The Path object of the directory to display.
        indent: The current indentation string for nested items.
    """
    items = sorted(directory.iterdir(), key=lambda p: p.name.lower())
    for item in items:
        if item.is_dir():
            print(indent + Fore.BLUE + Style.BRIGHT + item.name + "/")
            print_directory_tree(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name)


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python hw03.py <path_to_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Error: path '{path}' does not exist.")
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + f"Error: '{path}' is not a directory.")
        sys.exit(1)

    print(Fore.BLUE + Style.BRIGHT + path.name + "/")
    print_directory_tree(path)


if __name__ == "__main__":
    main()
