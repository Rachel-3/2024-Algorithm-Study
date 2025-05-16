grade_to_score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total_score = 0.0
total_credit = 0.0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade == "P":
        continue

    total_score += credit * grade_to_score[grade]
    total_credit += credit

print(f"{total_score / total_credit:.6f}")