
def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Patients are dictionaries with:
      - "name": string
      - "severity": integer 1 (most urgent) to 5 (least urgent)
      - "arrival_order": integer, smaller means arrived earlier

    Priority rules:
      1. Lower severity number first.
      2. If severity ties, lower arrival_order first.

    Return a list of names in the correct order. If k is 0 or there are
    no patients, return [].
    """

    # TODO Steps 1–3: Restate the problem, and list input, output, and key fields.
    # TODO Steps 4–5: Decide whether to use sorting or a priority queue; write pseudocode.
    # TODO Step 6: Implement the selection logic to pick the top k patients.
    # TODO Step 7: Test with small examples (including empty list and k=0).
    # TODO Step 8: Confirm the time complexity is about O(n log n).
    pass


if __name__ == "__main__":
    # Optional manual test
    sample_patients = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample_patients, 2))
