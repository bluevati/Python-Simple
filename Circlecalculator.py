# get the radius of circle from user & call functions & show the result
def main():
    r=float(input("Tell me radius of your circle:"))
    area = calculate_area(r)
    circumference = calculate_circumference(r)
    #print & calculate the result to two decimal places
    print(f"The area of your Circle is: {area:.2f}\nThe circumference of your Circle is: {circumference:.2f}" )

# the function of calculating area
def calculate_area(r):
    pi=3.14159
    return pi * r * r

# the function of calculating circumference
def calculate_circumference(r):
    pi=3.14159
    return 2 * pi * r

main()