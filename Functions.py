# function called hello.
# we need to define the function using def.
# identation is important here. What ever code we run under def is going to be part of this function hello()
def main():
    name = input("What is your name? ")
    hello()


def hello(to="world"):
    print("hello,", to)


main()
