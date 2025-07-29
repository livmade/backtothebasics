# working with methods

name = "olivia nicole smith"
print(name.title())
print(name.upper())
print(name.lower()) 

#f-string
first_name = "olivia"
last_name = "smith"
full_name = f"{first_name} {last_name}"
print(full_name.title())

#f-string with a method
print(f"Hello, {full_name.title()}!")

#f-string with a method and a variable
message = f"Hello, {full_name.title()}!"