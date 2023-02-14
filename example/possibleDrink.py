age = int(input("How old are you?"))

if age < 18:
    print("You can't drink.")
elif age >= 18 and age < 35:
    print("You drink beer!")
else:
    print("Go ahead")
