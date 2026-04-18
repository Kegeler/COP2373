import numpy as np


# This function reads the CSV file and extracts only the exam grades
def load_data(file_name):
    # skip_header=1 → ignores the first row (column names)
    # usecols=(1,2,3) → selects only exam columns (not names)
    data = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=(1,2,3))
    return data


# FUNCTION 2: Exam Statistics

# This function calculates stats for each exam (column by column)
def exam_stats(data):
    print("\n=== Statistics for Each Exam ===")

    print("Mean (average):", np.mean(data, axis=0))
    print("Median:", np.median(data, axis=0))
    print("Standard Deviation:", np.std(data, axis=0))
    print("Minimum:", np.min(data, axis=0))
    print("Maximum:", np.max(data, axis=0))


# This function calculates stats using ALL exam grades together
def overall_stats(data):
    print("\n=== Overall Statistics (All Exams Combined) ===")

    print("Mean (average):", np.mean(data))
    print("Median:", np.median(data))
    print("Standard Deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))

# FUNCTION 4: Pass / Fail Analysis
# This function checks how many students passed or failed each exam
# Passing grade is 60 or higher
def pass_fail(data):
    print("\n=== Pass and Fail Results ===")

    # Create a True/False table (True = pass, False = fail)
    passing = data >= 60

    # Loop through each exam (column)
    for i in range(data.shape[1]):
        passed = np.sum(passing[:, i])   # count True values (passes)
        failed = data.shape[0] - passed  # total students - passed
        print(f"Exam {i+1}: Passed = {passed}, Failed = {failed}")

    # Overall pass percentage (all exams combined)
    total_pass = np.sum(passing)
    total_grades = data.size
    print("\nOverall Pass Percentage:", (total_pass / total_grades) * 100, "%")

# MAIN PROGRAM

# Load data from CSV file
data = load_data("grades.csv")

# Show first few rows to understand data structure
print("First 5 rows of data:")
print(data[:5])

# Run analysis functions
exam_stats(data)
overall_stats(data)
pass_fail(data)