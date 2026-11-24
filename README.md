# Transcript Word Audit

Measure how many words a speech recognizer inserts, deletes or substitutes compared with human transcripts. Use it to compare recognition systems on the same calls or to locate utterances for manual review.

## Quick start

Clone the repository, open its directory and run with Python 3.10 or later. All dependencies ship with Python.

    python audit.py examples/calls.csv

The example changes “payment is due” to “payment was due” and transcribes “thank you” correctly. One edit across five reference words gives a word error rate (WER) of 0.2.

## Input and output

Provide a UTF-8 CSV with id, reference and candidate columns. Quote fields containing commas. Each ID identifies one aligned utterance. JSON output includes edit counts per pair and a corpus-wide WER. Use --ignore-case to case-fold both strings. Punctuation counts and whitespace separates words.

## Implementation

audit.py computes the minimum edit distance with two rows of dynamic programming state. For sequences of m and n words, scoring takes O(mn) time and O(n) working memory per pair. The report retains one result per ID. Empty references count candidate words as insertions. An entirely empty reference corpus has no defined WER and exits with status 2.

## Verification and use

Run python -m unittest discover -s tests -v. Use anonymous IDs because the report includes them. This evaluator expects paired text and does not process audio. WER assigns equal weight to each edit, so review errors in names and amounts separately. A future extension could report edit alignments. See faq.md, CONTRIBUTING.md and the MIT LICENSE.
