
age_input = input("Enter your age: ")


age = int(age_input)

if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
