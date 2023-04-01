# #global scope variable
# my_name = 'Patryk'

# def print_name():
#     print('the name inside the function is', my_name)

# print("outside the function the name is", my_name)
# print_name()

#global scope variable

# def print_name():
#     #local scope variable
#     my_name = 'Patryk'
#     print('the name inside the function is', my_name)

# print("outside the function the name is", my_name)
# print_name()

my_name = 'Patryk'

def print_name():
    global my_name
    my_name ='Josh'
    print('the name inside the function is', my_name)

print_name()
print("outside the function the name is", my_name)