# FAQ

## 1. What does this evaluate?

It scores text output from speech recognition against human reference transcripts.

## 2. What problem does it solve?

It gives two recognition systems a common error measure on the same utterances.

## 3. Who can use it?

QA reviewers can identify high-error calls for closer inspection.

## 4. What does the report include?

Each pair gets an edit count, alongside the corpus error total and WER.

## 5. Which language runs it?

The evaluator and its tests are written in Python.

## 6. Which libraries are required?

csv parses the input and json serializes the results. Both ship with Python.

## 7. Do I need a GPU?

No. The alignment computation runs on a CPU.

## 8. How do I install it?

Clone the repository and run the script with Python 3.10 or later.

## 9. Can I ignore capitalization?

Pass --ignore-case to case-fold both sides before splitting words.

## 10. How do I run the demo?

Run python audit.py examples/calls.csv from the project directory.

## 11. Where should I look in the source?

audit.py contains distance for individual pairs and evaluate for aggregation.

## 12. How is WER calculated?

Divide the sum of minimum word edit counts by the total reference word count.

## 13. What input format is supported?

Use a UTF-8 CSV with unique utterance IDs and paired reference and candidate fields.

## 14. What does 0.2 mean?

The system needed one word edit per five reference words in aggregate.

## 15. Can I customize tokenization?

Change the split step in evaluate and pin that behavior with a regression test.

## 16. What happens on malformed input?

The CLI prints an error on stderr and exits with code 2.

## 17. Why is WER above one?

Extra predicted words can outnumber all words in the reference set.

## 18. Why did punctuation change my score?

A comma attached to a word is part of its token. Apply consistent preprocessing if needed.

## 19. How do I run the tests?

Run python -m unittest discover -s tests -v from the checkout.

## 20. How can I contribute?

Include a small synthetic pair and the manually verified expected score.

## 21. Can I score audio directly?

First transcribe it and pair each output with its human reference.

## 22. Can WER alone approve a deployment?

Also evaluate important terms, latency and performance on representative speakers.

## 23. What could be added next?

An edit alignment would show reviewers the specific words that changed.

## 24. Does the output contain private text?

It includes your IDs and counts. Choose anonymous IDs and keep input transcripts local.

## 25. Where is the worked calculation?

README.md explains the one substitution in examples/calls.csv.

