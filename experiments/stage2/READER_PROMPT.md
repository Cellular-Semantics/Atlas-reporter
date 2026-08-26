# Stage 2 reader task

You are answering ONE question from ONE supplied excerpt file. This is a controlled
experiment: your job is to report what the excerpt does or does not support.

## Rules — these are the experiment

1. Read EXACTLY ONE file: the context path given below. Do NOT read any other file,
   do NOT search the web, do NOT run any other tool first.
2. Answer ONLY from that file's contents. Do NOT use prior knowledge of the paper,
   the cell types, or the biology, even if you are confident.
3. If the excerpt does not contain the answer, set `answerable` to false and leave
   `answer` empty. Reporting absence is a correct outcome, not a failure — do not
   guess, hedge, or supply a plausible answer from background knowledge.
4. `support_quote` must be copied verbatim from the excerpt. If you cannot copy one,
   the answer is not supported and `answerable` should be false.

## Output

Write JSON to the output path given below, and nothing else:

```json
{"answerable": true, "answer": "...", "support_quote": "..."}
```
