print("Get your demographics")

def validate_age():
    """Prompts the user for input and validates it is a digit."""
    try:
        return int(input ("Age: "))
    except ValueError:
        print("Invalid value.\n Please enter a number")
    except Exception as e:
        print(f"Error: {e}")

def get_demographics(age):
    """Return the life-stage category string based on an integer age."""
    if 1 <= age < 3:
        return "Toddler"
    elif 3 <= age < 5:
        return "Pre-schooler"
    elif 5 <= age < 12:
        return "Child"
    elif 12 <= age < 19:
        return "Teenager"
    elif 19 <= age < 34:
        return "Young adult"
    elif 34 <= age < 54:
        return "Middle-aged adult"
    elif 54 <= age < 64:
        return "Older adult"
    elif age >= 65:
        return "Senior"
    elif age < 0:
        print("Age can not be less than 0")
        return None

user_age = validate_age()

if user_age:
    demographics = get_demographics(user_age)
    if demographics:
        print(f"You are a {demographics}.")
