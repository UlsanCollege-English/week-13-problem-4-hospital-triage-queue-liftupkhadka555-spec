def select_patients(patients, k):
    if k <= 0:
        return []

    # Stable sort by (severity asc, arrival_order asc)
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Select first k patients and return names
    return [p["name"] for p in sorted_patients[:k]]