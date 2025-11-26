import os
import sys
import pytest

# Ensure we can import main.py from the homework folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import select_patients


@pytest.mark.parametrize(
    "patients, k, expected",
    [
        (
            [
                {"name": "Alex", "severity": 3, "arrival_order": 5},
                {"name": "Bella", "severity": 1, "arrival_order": 6},
                {"name": "Chris", "severity": 1, "arrival_order": 2},
            ],
            2,
            ["Chris", "Bella"],
        ),
        (
            [
                {"name": "Dana", "severity": 2, "arrival_order": 1},
                {"name": "Eli", "severity": 4, "arrival_order": 0},
            ],
            1,
            ["Dana"],
        ),
        (
            [
                {"name": "Frank", "severity": 5, "arrival_order": 10},
            ],
            1,
            ["Frank"],
        ),
        (
            [
                {"name": "Gina", "severity": 2, "arrival_order": 3},
                {"name": "Hank", "severity": 2, "arrival_order": 1},
            ],
            2,
            ["Hank", "Gina"],
        ),
    ],
)
def test_normal_cases(patients, k, expected):
    assert select_patients(patients, k) == expected


@pytest.mark.parametrize(
    "patients, k, expected",
    [
        ([], 3, []),
        (
            [
                {"name": "Ivy", "severity": 2, "arrival_order": 3},
            ],
            0,
            [],
        ),
        (
            [
                {"name": "Jay", "severity": 1, "arrival_order": 0},
                {"name": "Kai", "severity": 1, "arrival_order": 0},
            ],
            2,
            ["Jay", "Kai"],  # any order of these two is fine, but stable sort keeps input order
        ),
    ],
)
def test_edge_cases_empty_and_zero_k(patients, k, expected):
    assert select_patients(patients, k) == expected


@pytest.mark.parametrize(
    "patients, k",
    [
        (
            [
                {"name": "P" + str(i), "severity": (i % 5) + 1, "arrival_order": i}
                for i in range(20)
            ],
            5,
        ),
        (
            [
                {"name": "Q" + str(i), "severity": 1, "arrival_order": 20 - i}
                for i in range(20)
            ],
            10,
        ),
        (
            [
                {"name": "R" + str(i), "severity": 5 - (i % 5), "arrival_order": i}
                for i in range(50)
            ],
            50,
        ),
    ],
)
def test_larger_inputs_properties(patients, k):
    result = select_patients(patients, k)
    assert len(result) == min(k, len(patients))

    # Check ordering property: severity non-decreasing, arrival non-decreasing within same severity
    # Build a mapping from name to (severity, arrival_order)
    info = {p["name"]: (p["severity"], p["arrival_order"]) for p in patients}
    prev = None
    for name in result:
        severity, arrival = info[name]
        if prev is not None:
            prev_sev, prev_arr = prev
            assert severity >= prev_sev
            if severity == prev_sev:
                assert arrival >= prev_arr
        prev = (severity, arrival)
