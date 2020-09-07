#Program to calculate area of a circle

def calculate_radius(rad):
    radius = float(rad)
    area = 3.142 * radius * radius
    print('The area of the circle is ' + str(area))

print('Specify x to close the program')

while True:
    rad = input('Enter the radius of the circle: ')
    if rad == 'x':
        break
    calculate_radius(rad)
