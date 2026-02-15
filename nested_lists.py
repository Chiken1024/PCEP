students: list[list] = [
  ["Aarav", [85, 78, 92]],
  ["Diya", [72, 88, 95]],
  ["Kabir", [90, 91, 89]],
  ["Ira", [60, 75, 70]]
]

highest_avg: list = ["", 0]
above_90: list[str] = []
avg: float = .0
for student in students:
  for grade in student[1]:
    if grade > 90 and student[0] not in above_90: above_90.append(student[0])
    avg += grade
  avg /= len(student[1])
  if avg > highest_avg[1]: highest_avg = [student[0], avg]
  if avg < 75: student[1] = [grade + 5 for grade in student[1]]
  avg = 0

print(f"""
Highest average: {int(highest_avg[1])} by {highest_avg[0]}
Students that scored a grade above 90: {above_90}
""")
print(
  "Final student scores:\n",
  *[" " + student[0] + ": " + str(student[1]) + "\n" for student in students]
)