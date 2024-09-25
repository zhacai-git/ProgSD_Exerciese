name = input("")
if len(name) < 5:
    surname = input("")
    name = name + surname
    print(name.upper())
else:
    print(name.lower())