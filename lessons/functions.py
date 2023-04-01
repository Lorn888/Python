def area(radius = 3):
    return(3.14 * radius * radius)

def vol(area, length):
    print(area* length)

radius = int(input("Enter radius: "))
length = int(input("enter length: "))


vol(area(radius), length)