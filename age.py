from datetime import datetime


def calculate_age(date_str):
    birth_date = datetime.strptime(date_str, "%d/%m/%Y")
    today = datetime.today()  # Current date
    # Calculate age based on year of birth
    age = today.year - birth_date.year
    # Check if birthday has not already happened this year, and adjust if it hasn't
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


# Ask user to input date of birth
user_input = input("Please enter your date of birth (DD/MM/YYYY): ")
# Calculate and print final age
print(f"Your age is: {calculate_age(user_input)}")
