#gradebook.Py
# Name:jiya garg
# Date:04-november-2025
# title:simpleimport csv

def welcome():
    print("\nWelcome to GradeBook Analyzer")
    print("1. Manual Entry")
    print("2. CSV Import")
    print("q. Quit")

def manual_input():
    marks = {}
    n = int(input("Number of students: "))
    for i in range(n):
        name = input(f"Student {i+1} name: ").strip()
        score = float(input(f"Student {i+1} marks: "))
        marks[name] = score
    return marks

def csv_input(filename):
    marks = {}
    with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                if len(row) >= 2:  # avoid index errors
                    marks[row[0].strip()] = float(row[1])
    return marks

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def print_results(marks, grades):
    if not marks:
        print("No data to display.")
        return

    print("\nName\tMarks\tGrade")
    print("-"*24)
    for name in marks:
        print(f"{name}\t{marks[name]:.2f}\t{grades[name]}")

    avg = round(sum(marks.values()) / len(marks), 2)
    max_score = max(marks.values())
    min_score = min(marks.values())

    max_students = [name for name, score in marks.items() if score == max_score]
    min_students = [name for name, score in marks.items() if score == min_score]

    print("\nStatistics:")
    print(f"Average Marks: {avg}")
    print(f"Highest Marks: {max_score} by {', '.join(max_students)}")
    print(f"Lowest Marks: {min_score} by {', '.join(min_students)}")

def main():
    while True:
        welcome()
        choice = input("Choose option: ").lower()
        if choice == '1':
            marks = manual_input()
        elif choice == '2':
            filename = input("Enter CSV filename: ").strip()
            marks = csv_input(filename)
        elif choice == 'q':
            print("Bye!")
            break
        else:
            print("Invalid input.")
            continue

        if not marks:
            print("No valid data found. Please try again.")
            continue

        grades = assign_grades(marks)
        print_results(marks, grades)

        again = input("\nAnalyze another? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
