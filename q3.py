password = input("Enter your password: ")

length = len(password)
has_upper = False
has_lower = False
digit_count = 0
special_count = 0

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

# Scoring
score = 0

if length >= 10:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if digit_count >= 3:
    score += 1
if special_count >= 2:
    score += 1

# Strength output
print("\nPassword Strength: ", end="")
if score == 5:
    print("Very Strong")
elif score == 4:
    print("Strong")
elif score == 3:
    print("Moderate")
elif score == 2:
    print("Weak")
else:
    print("Very Weak")

flag=0

# Suggestions
print("\nSuggestions to improve your password:")
if length < 10:
    print("- Use at least 10 characters.")
    flag+=1
if not has_upper:
    print("- Add at least 1 uppercase letter (A-Z).")
    flag+=1
if not has_lower:
    print("- Add at least 1 lowercase letter (a-z).")
    flag+=1
if digit_count < 3:
    print(f"- Add at least {3 - digit_count} more number(s).")
    flag+=1
if special_count < 2:
    print(f"- Add at least {2 - special_count} more special character(s) (e.g., !, @, #, etc).")
    flag+=1

if flag==0:
    print("IMPROVEMENT NOT REQUIRED.")
