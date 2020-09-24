my_list = []


def work_with_list(command):
    if not command:
        print("You input empty command! Try again.")
        return 'try_again'
    if command[0] == 'insert':
        try:
            my_list.insert(int(command[1]), int(command[2]))
        except IndexError:
            print("You have to enter the position and value of element! Try again.")
            return 'try_again'
        else:
            return my_list
    if command[0] == 'print':
        try:
            print(my_list)
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    if command[0] == 'remove':
        try:
            my_list.remove(int(command[1]))
        except IndexError:
            print("You have to enter the value of element! Try again.")
            return 'try_again'
        else:
            return my_list
    if command[0] == 'append':
        try:
            my_list.append(int(command[1]))
        except IndexError:
            print("You have to enter the value of element! Try again.")
            return 'try_again'
        else:
            return my_list
    if command[0] == 'sort':
        try:
            my_list.sort()
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    if command[0] == 'pop':
        try:
            my_list.pop()
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    if command[0] == 'reverse':
        try:
            my_list.reverse()
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    else:
        print('You entered an unsupported command. Try again.')
        return 'try_again'


while True:
    count = input()
    try:
        count = int(count)
        break
    except ValueError:
        print('Please enter the number.')


i = 0
while i < int(count):
    res = work_with_list(input().split())
    if res != 'try_again':
        i += 1
