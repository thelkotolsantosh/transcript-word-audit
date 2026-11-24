"""Measure word-level edit distance for paired reference and candidate transcripts."""
import argparse
import csv
import json


def distance(reference, candidate):
    previous = list(range(len(candidate) + 1))
    for i, word in enumerate(reference, 1):
        current = [i]
        for j, other in enumerate(candidate, 1):
            current.append(min(previous[j] + 1, current[-1] + 1,
                               previous[j - 1] + (word != other)))
        previous = current
    return previous[-1]


def evaluate(rows, ignore_case=False):
    results = []
    seen = set()
    total_words = total_errors = 0
    for row in rows:
        key = row["id"].strip()
        if not key or key in seen:
            raise ValueError("Each pair needs a unique nonempty id")
        seen.add(key)
        pair = [row["reference"], row["candidate"]]
        if None in pair or None in row:
            raise ValueError(f"Invalid column count for {key}")
        if ignore_case:
            pair = [line.casefold() for line in pair]
        reference, candidate = (line.split() for line in pair)
        errors = distance(reference, candidate)
        results.append(dict(id=key, errors=errors, reference_words=len(reference)))
        total_words += len(reference)
        total_errors += errors
    if not total_words:
        raise ValueError("Corpus must contain at least one reference word")
    return dict(errors=total_errors, reference_words=total_words,
                wer=total_errors / total_words, pairs=results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--ignore-case", action="store_true")
    args = parser.parse_args()
    try:
        with open(args.file, encoding="utf-8-sig", newline="") as source:
            rows = csv.DictReader(source, strict=True)
            if sorted(rows.fieldnames or []) != ["candidate", "id", "reference"]:
                raise ValueError("Expected id, reference and candidate headers")
            print(json.dumps(evaluate(rows, args.ignore_case)))
    except (KeyError, ValueError, OSError, AttributeError, csv.Error) as error:
        parser.exit(2, f"Cannot score input: {error}\n")
