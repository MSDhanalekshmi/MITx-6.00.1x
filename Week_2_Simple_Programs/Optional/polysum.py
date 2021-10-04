# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is:
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

# Hint: What to import?
# Which library should you be importing at the beginning of your code in order to call the tan function and to get the pi constant?

# This is an optional exercise, but great for extra practice!


import math


def polysum(n, s):

    def areaOfpolygun(n, s):
        area = (0.25 * n * s ** 2) / (math.tan(math.pi / n))
        return area

    def perimeterOfpolygun(n, s):
        perimeter = n * s
        return perimeter
    sum = areaOfpolygun(n, s) + (perimeterOfpolygun(n, s) ** 2)
    return round(sum, 4)


# correct
