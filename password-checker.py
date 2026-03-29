password = input("Enter your password: ")
has_len= len(password)>=8
has_digit= any(char.isdigit() for char in password)
has_upper= any(char.isupper() for char in password)

if has_len and has_digit and has_upper:
    print("Your password is strong.")
elif has_len and (has_digit or has_upper):
    print("Your password is moderate.")
else:
    print("Your password is weak. Please choose a stronger password.")