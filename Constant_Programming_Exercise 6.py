import re

# Function to validate phone numbers941
def validate_phone(phone):
    pattern = r'\d\d\d-\d\d\d-\d\d\d\d$'
    return bool(re.match(pattern, phone))

# Function to validate Social Security Numbers
def validate_ssn(ssn):
    pattern = r'\d\d\d-\d\d\d-\d\d\d\d$'
    return bool(re.match(pattern, ssn))

# Function to validate US ZIP codes
def validate_zip(zip_code):
    pattern = r'\d\d\d\d\d$'
    return bool(re.match(pattern, zip_code))

# Main function to get input from the user
def main():
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number: ")
    zip_code = input("Enter a ZIP code: ")


    if validate_phone(phone):
        print("Phone number is valid ")
    else:
        print("Phone number is invalid ")

    if validate_ssn(ssn):
        print("Social Security Number is valid ")
    else:
        print("Social Security Number is invalid ")

    if validate_zip(zip_code):
        print("ZIP code is valid ")
    else:
        print("ZIP code is invalid ")

# Run the program
if __name__ == "__main__":
    main()