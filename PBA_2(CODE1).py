import csv

attendance = {}   # employee_id -> number of days present

with open("attendance.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp_id = row["employee_id"]
        if row["status"] == "Present":
            if emp_id in attendance:
                attendance[emp_id] += 1
            else:
                attendance[emp_id] = 1

print("Employee ID  Days Present")
for emp_id, days in attendance.items():
    print(emp_id, "        ", days)
