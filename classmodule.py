def sqFtHouse ():
    length = float(input("What is the length of your house (in ft)? "))
    width = float(input("What is the width of your house (in ft)? "))

    area = length * width
    print(f"The square footage of the house is {area:.2f} square feet")


def calc_circumference():
    radius = float(input("What is the radius of your circle (in ft)? "))
    import math
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is {circumference:.2f}")

