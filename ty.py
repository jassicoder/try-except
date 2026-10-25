try:
    n=int(input("Enter ur no."))
    print("the no. entered is",n)
except ValueError as j:
    print("Exception=",j)