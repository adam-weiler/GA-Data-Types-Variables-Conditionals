#Exercise 6

def wrap_text(my_text, my_symbols): #Returns my_symbols, my_text, and my_symbols backwards.
    return my_symbols + my_text + my_symbols[::-1]

print(wrap_text('hello', '==='))
print(wrap_text('new message', '---===###'))
print(wrap_text('WE BOUGHT A ZOO!', '🐢🐵🦍🦄🐺🐹'))