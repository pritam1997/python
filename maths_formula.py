
#Area of square
n = int(input("Enter value for side of sqaure : "))
side_sq = n ** 2

# Area of Circle
r = float(input("Enter radius_of_circle : "))
radius_of_circle = 3.14 * (r ** 2)

# Area of Rectangle
l = float(input("Enter length of rectangle : "))
b = float(input("Enter breath of rectangle : "))
area_of_rect = l * b

print(f"\nArea of square : {side_sq}\n")
print(f"\nArea of Circle : {round(radius_of_circle,2)}\n")
print(f"\nArea of rectangle : {round(area_of_rect,2)}\n")
