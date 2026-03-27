# import csv module to work with CSV files
import csv


# Create and write data into the file
def write_file():
    # Ask user how many students to enter
    n = int(input("How many students? "))

    # Open file in write mode (this will create the file)
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)  # create writer object

        # write header (column names)
        writer.writerow(["First Name", "Last Name", "Exam1", "Exam2", "Exam3"])

        # loop to enter each student's data
        for i in range(n):
            print("\nEnter student", i + 1)

            # Get input from user
            first = input("First name: ")
            last = input("Last name: ")
            e1 = input("Exam 1: ")
            e2 = input("Exam 2: ")
            e3 = input("Exam 3: ")

            # write one row to the file
            writer.writerow([first, last, e1, e2, e3])


# Read and display the file
def read_file():
    # Open file in read mode
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        print("\nStudent Grades:\n")

        # loop through each row in the file
        for row in reader:
            print(row)   # print each row


# Call the functions( create and read files)
write_file()
read_file()