try:
    n1=int(input("enter the 1st no."))
    n2=int(input("enter the 2nd no."))
    result=n1/n2
    print("Ur result is",result)
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except ValueError:
    print('enter a whole no.')
except:
    print("Invalid input")
else:
    print("No excpections")
finally:
    print("jassi jaisa koi nahin")

