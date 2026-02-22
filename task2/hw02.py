def get_cats_info(path):
    """Read a cats file and return a list of dictionaries with cat information.

    Args:
        path: Path to the text file with cat records.

    Returns:
        A list of dicts with keys 'id', 'name', 'age', or an empty list on error.
    """
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) < 3:
                    continue
                cats.append({"id": parts[0], "name": parts[1], "age": parts[2]})
    except FileNotFoundError:
        print(f"File not found: {path}")
    return cats


if __name__ == "__main__":
    from pathlib import Path

    cats_info = get_cats_info(Path(__file__).parent / "cats.txt")
    print(cats_info)
