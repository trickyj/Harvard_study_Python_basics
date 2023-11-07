def main():
    x = int(input("What's X? "))
    print("x squred is", square(x))


def square(n):
    return n * n  # n multiplied by 2
    return n ** 2  # this way we can do n raise to power of 2
    return pow(n, 2)  # we can use this as n raise to power of 2


main()


# # x = int(input("Enter number 1 to add?: "))
# # y = int(input("Enter number 2 to add?: "))

# # # Here we are converting the String to int.
# # print(x + y)


# # data type floats & rounding.

# x = float(input("what's x? "))
# y = float(input("what's y? "))
# z = round(x + y)
# # we can now add , in the digit example 1,000 we use f to format the string.
# print(f"{z:,}")
