
def count(dictionary):
    sorted = list(dictionary.values())
    for belt in set(sorted):
        number = sorted.count(belt)
        print(f'there is {number} of {belt} belts')


# def ninaja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f"I am {key} and I am a {val} belt")
    
ninja_belts= {}

while True:
    ninaja_name = input('name here: ')
    ninja_belt = input('belt color here: ')
    ninja_belts[ninaja_name] = ninja_belt

    another = input('add another (y/n)')
    if another == 'y':
        continue
    else:
        break



count(ninja_belts)