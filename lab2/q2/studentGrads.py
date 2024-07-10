def process_grades(file_path):
    total_grade = 0
    num_students = 0
    average_grade = 0  
    failed_students = []

    file1 = open(file_path, 'r')
    
    while True:
        line = file1.readline()
        if not line:
            break
        name, grade = line.strip().split()
        grade = int(grade)
        total_grade += grade
        num_students += 1
        if grade < 60:
            failed_students.append(name)
    file1.close()
    
    if num_students > 0:
        average_grade = total_grade / num_students  
        
    print(f"Average grade: {average_grade}")
    print("Failed students:", failed_students)

# Example usage
file_path = "G:/labs/python/lab2/q2/students.txt"
process_grades(file_path)
