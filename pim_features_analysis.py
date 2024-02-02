"""Analysis of the PIM strucure features."""
import argparse
import csv
import re
from pathlib import Path
from typing import List
from typing import Pattern
from typing import Sequence
from typing import Union

__version__ = "0.1.0"


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(prog="pim_feature_analyis", description=__doc__)
    parser.add_argument(
        "input_csv",
        type=str,
        help="Path to the input file.",
    )
    parser.add_argument("--version", "-V", action="version", version=__version__)
    return parser.parse_args()


def main() -> None:
    """Main function."""
    args: argparse.Namespace = parse_args()
    print(args)
    analyze_features(args.input_csv)


def analyze_features(input_csv: Union[str, Path]) -> None:
    """Analyze the features."""
    if isinstance(input_csv, str):
        input_csv = Path(input_csv)
    if not input_csv.exists():
        raise FileNotFoundError(f"File {input_csv} not found.")
    output_csv: Path = input_csv.parent / f"{input_csv.stem}_analyzed.csv"

    forbidden_chars: Pattern[str] = re.compile(r"[^a-zA-Z0-9_\-]")

    with input_csv.open("r", encoding="utf-8") as csv_file, output_csv.open(
        "w", encoding="utf-8", newline=""
    ) as out_file:
        reader = csv.DictReader(csv_file)
        header: Sequence[str] | None = reader.fieldnames
        if header is None:
            raise ValueError(f"No header found in input file: {input_csv.as_posix()}")
        writer = csv.writer(out_file)
        writer.writerow(header)
        count_of_invalid_features: int = 0
        for row in reader:
            found_forbidden_chars: List[str] | None = forbidden_chars.findall(
                row["Identifier"]
            )
            if found_forbidden_chars and len(found_forbidden_chars) > 0:
                print(
                    f"Found forbidden characters in {row['Identifier']}: {found_forbidden_chars}"
                )
                count_of_invalid_features += 1
                writer.writerow(row.values())


if __name__ == "__main__":
    main()
