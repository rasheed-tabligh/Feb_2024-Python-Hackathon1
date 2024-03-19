age_str = input("Please enter your age: ")

try:
    age = int(age_str)
    
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
        
except ValueError:
    print("Invalid input. Please enter a valid age.")
