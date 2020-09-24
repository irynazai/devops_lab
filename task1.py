def if_positive(func):
    def wrapper(n):
        if not n:
            print('You not input number. Try again.')
        else:
            m = func(n)
            if m > 0:
                for i in range(m):
                    print(i ** 2)
            elif m == 0:
                print(0)
            else:
                print("You have to input non-negative value. Try again.")
    return wrapper


@if_positive
def if_number(n):
    try:
        result = int(n)
    except ValueError:
        print("Not an integer! Try again.")
        exit()
    else:
        return result


N = input()
if_number(N)
