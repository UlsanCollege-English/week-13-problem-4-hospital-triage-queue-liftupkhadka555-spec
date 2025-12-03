[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/0_s-nl4i)
# hw04 – Hospital Triage Queue

## Overview
You will implement a helper function to select the next `k` patients to call from an emergency room waiting list. Each patient has:

- `name`: string
- `severity`: integer 1–5 (1 = most urgent)
- `arrival_order`: non‑negative integer (0, 1, 2, …)

Priority rules:
1. Lower `severity` number (more urgent) first.
2. Tie on severity → earlier `arrival_order` first.

Return up to `k` patient names in the correct call order.

## Function Specification
```python
def select_patients(patients, k):
    """Return up to k patient names in priority order.

    patients: list[dict] with keys 'name', 'severity', 'arrival_order'
    k: non-negative int
    """
    ...
```

Rules:
- Sort by `severity` ascending, then `arrival_order` ascending.
- If `k` >= number of patients, return all names in priority order.
- If `k` == 0 or `patients` is empty, return `[]`.

## Example
```python
patients = [
    {"name": "Alex",  "severity": 3, "arrival_order": 5},
    {"name": "Bella", "severity": 1, "arrival_order": 6},
    {"name": "Chris", "severity": 1, "arrival_order": 2},
]

select_patients(patients, 2)
# ['Chris', 'Bella']
```

## Constraints
- `0 <= len(patients) <= 100_000`
- `0 <= k <= 100_000`
- `severity ∈ {1,2,3,4,5}`

## Complexity Target
- Time: `O(n log n)` (sorting) or better with a heap / selection strategy.
- Space: `O(n)` (you may build a structure or sort a copy).

## Suggested Implementation Steps
1. Clarify inputs/outputs in your own words.
2. Confirm ordering criteria (severity, then arrival_order).
3. Choose approach: full sort vs. heap for top `k`.
4. Implement using either:
   - `sorted(patients, key=lambda p: (p['severity'], p['arrival_order']))`
   - `heapq` pushing tuples `(severity, arrival_order, name)` until `k` popped.
5. Slice first `k` names (or all if fewer than `k`).
6. Test with edge cases: empty list, `k=0`, single patient, all same severity.
7. Verify complexity reasoning.

## Hints
- Simplicity: sorting is fine unless performance of partial selection matters.
- Heap optimization: for large `n` and small `k`, a heap can reduce work.
- Return only names, never full patient dictionaries.

## Running Tests
From repo root:
```bash
python -m pytest -q
```
Optionally add your own quick script examples.

## FAQ
- **Modify in place?** You may; tests do not require preserving original order.
- **`k` larger than number of patients?** Return all in priority order.
- **`k == 0`?** Return `[]`.
- **Invalid severities?** Assume input validity; no need for extra validation.
- **Expected complexity?** About `O(n log n)` (sort) or `O(n log k)` (heap for top `k`).
- **Exact ties?** If severity and arrival_order both equal, relative order is arbitrary.