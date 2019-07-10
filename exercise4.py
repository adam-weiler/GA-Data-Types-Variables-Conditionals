#Exercise 4

def long_string(my_string): #Returns whether my_string is less than or greater than 8.
    if len(my_string) < 8:
        return False
    else:
        return True

print(long_string('Short')) #False
print(long_string('Really long string')) #True
print(long_string('')) #False
print(long_string('Super-duper extra really long string.')) #True