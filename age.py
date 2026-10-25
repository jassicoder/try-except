try:
    a=int(input("Enter age"))
    if a >18:
        print("Valid age")
    else:
        raise ValueError
except ValueError:
    print("Invalid age")
finally:
    print("Ahaana mam is the best teacher")

