def remove_duplicates(stu_rollno):
  unique_rollno = set()
  for rollno in stu_rollno:
    if rollno not in unique_rollno:
      unique_rollno.add(rollno)
  return list(unique_rollno)

stu_rollno = [112, 113, 112, 114]
unique_rollno = remove_duplicates(stu_rollno)
print(unique_rollno)