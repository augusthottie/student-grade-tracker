#program to track student grades, add grade, calculate average, determine highest and lowest grade, and display a bar chart of grades
import matplotlib.pyplot as plt

#initialise grades to empty list
grades = []

#Add grade
def add_grade():
    print("Grades Before Adding ",  grades)
    input_str = input("Enter students grades separated by space: ")
    grades_list = list(map(float, input_str.split()))
    grades.extend(grades_list)
    print("Grades After Adding " , grades)
    print("Student Grades added successfully!!")

#List all grades
def display_grade():
    if len(grades) == 0:
        print("No grades to display")
    else:
        print("Student Grades as follows: ")
        for grade in grades:
            print(grade)

#Calculate average
def calculate_average():
    if len(grades) == 0:
        print("No grades to calculate average")
    else:
        average = sum(grades) / len(grades)
        print(f"Average grade is: {average}")

#Determine highest grade
def highest_grade():
    if len(grades) == 0:
        print("No grades to determine highest grade")
    else:
        highest = max(grades)
        print(f"Highest grade is: {highest}")

#Determine lowest grade
def lowest_grade():
    if len(grades) == 0:
        print("No grades to determine lowest grade")
    else:
        lowest = min(grades)
        print(f"Lowest grade is: {lowest}")

#Display bar chart of grades
def display_bar_chart():
    if len(grades) == 0:
        print("No grades to display")
    else:
        x_labels = [f"Student {i+1}" for i in range(len(grades))]
        plt.bar(x_labels, grades)
        plt.xlabel("Student")
        plt.ylabel("Grade")
        plt.title("Student Grades")
        plt.ion
        plt.show()
#Main
def main():
    while True:
        print("\n**********Student Grade Tracker***********")
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Calculate average")
        print("4. Determine highest grade")
        print("5. Determine lowest grade")
        print("6. Display bar chart")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                add_grade()
            case 2:
                display_grade()
            case 3:
                calculate_average()
            case 4:
                highest_grade()
            case 5:
                lowest_grade()
            case 6:
                display_bar_chart()
            case 7:
                print("Exiting the program......")
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
