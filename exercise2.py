#Exercise 2

def negative(my_number): #Returns if my_number is negative (true), positive(false), or 0(none).
    if (my_number > 0):
        return False
    elif (my_number < 0):
        return True
    elif (my_number == 0):
        return None

print(negative(3)) #Returns False.
print(negative(42)) #Returns False.
print(negative(-7)) #Returns True.
print(negative(0)) #Returns None.