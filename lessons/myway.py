def ninaja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'your name is {key} and your belt color is {val} ')


dictionary = {}


while True:
    color = input('Enter your belt color ')
    name = input('Enter your name here ')
    dictionary[name] = color


    another = input('Do u wanna add more people? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninaja_intro(dictionary)