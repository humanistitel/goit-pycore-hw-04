
def total_salary(path):
    """Analyze a salary file and return total and average salary.

    Args:
        path: Path to the text file with developer salaries.

    Returns:
        A tuple (total, average) or (0, 0) if the file is empty or missing.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            salaries = []
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) < 2:
                    continue
                try:
                    salaries.append(float(parts[1]))
                except ValueError:
                    continue
        if not salaries:
            return 0, 0
        total = sum(salaries)
        average = total / len(salaries)
        return total, average
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0


if __name__ == "__main__":
    from pathlib import Path
    
    total, average = total_salary(Path(__file__).parent / "salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
