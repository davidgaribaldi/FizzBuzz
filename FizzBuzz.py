for i in range(101):
    if i % 5 == 0:
        if i % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
