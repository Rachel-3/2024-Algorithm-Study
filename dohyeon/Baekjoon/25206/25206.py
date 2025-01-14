# 백준 25206 - 너의 평점은
# 분류 : 구현

total_scores = 0
total_grades = 0

grade_list = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

for i in range(20) :
    subject, score, grade = input().split()
    score = float(score)
    if grade != "P" :
        total_scores += score
        total_grades += score * grade_list[grade]

print("%.6f" % (total_grades / total_scores))