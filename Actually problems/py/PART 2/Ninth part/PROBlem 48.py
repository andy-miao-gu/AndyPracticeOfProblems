# x**2 + 3x+2
## you have to find roots using quadratic formula
## make a function that takes a,b,c and input
# that function should return root1 and root2
# formula for roo1 is root1 = (-b+(((b**2 )- 4*a*c)**1/2 )/2*a
# foruma for root2 is root2 = (-b-(((b**2 )- 4*a*c)**1/2 )/2*a
import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (both roots are the same)
        root = -b / (2*a)
        return root, root
    else:
        # Complex roots (no real roots)
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Example usage:
a = 1
b = 3
c = 2

roots = quadratic_roots(a, b, c)
print("Root 1:", roots[0])
print("Root 2:", roots[1])
