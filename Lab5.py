# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range (n):
        if i == (n-1) or i == 0:
            result += "*" *n + "\n"
        else:
            result += "*" + " " * (n-2) + "*" + "\n"
    
    return result.strip()

print(hollow_square(5))

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range (n):
        for j in range (1, i+2):
            result += str(j)
        result += "\n"
    
    return result.strip()

print(number_pattern(5))
# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    reuslt = ""

    sum = 0
    for i in range (n+1):
        sum += i
    return sum
print(sum_of_natural_numbers(5))

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        spaces = n - i -1
        stars = 2 * i + 1

        result += " " * spaces + "*" * stars + "\n"

    return result.rstrip()
print(centered_star_pyramid(4))
