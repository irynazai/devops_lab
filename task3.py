my_list = []


def work_with_list(command):
    if not command:
        print("You input empty command! Try again.")
        return 'try_again'
    if command.split(' ')[0] == 'insert':
        try:
            my_list.insert(int(command.split(' ')[1]), command.split(' ')[2])
        except IndexError:
            print("You have to enter the position and value of element! Try again.")
            return 'try_again'
        else:
            return my_list
    if command.split(' ')[0] == 'print':
        try:
            print(my_list)
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    if command.split(' ')[0] == 'remove':
        try:
            my_list.remove(int(command.split(' ')[1]))
        except IndexError:
            print("You have to enter the value of element! Try again.")
            return 'try_again'
        else:
            return my_list
    if command.split(' ')[0] == 'append':
        try:
            my_list.append(int(command.split(' ')[1]))
        except IndexError:
            print("You have to enter the value of element! Try again.")
            return 'try_again'
        else:
            return my_list
    if command.split(' ')[0] == 'sort':
        try:
            my_list.sort()
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    if command.split(' ')[0] == 'pop':
        try:
            my_list.pop()
        except IndexError:
            print('You entered an unsupported command. Try again.')
            return 'try_again'
        else:
            return my_list
    if command.split(' ')[0] == 'reverse':
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


print("Let's start work with list.\n")


while True:
    count = input('Enter how many commands you will use in total:\n')
    try:
        count = int(count)
        break
    except ValueError:
        print('Please enter the number.')


print('Input your command: \n'
      ' insert "position" "value" (example: insert 0 23),\n'
      ' print,\n'
      ' remove "value" (example: remove 5),\n'
      ' append "value", (example: append 13)\n'
      ' sort,\n'
      ' pop,\n'
      ' reverse \n')

i = 0
while i < int(count):
    print("You have " + f'{int(count) - i}' + " commands.\n")
    res = work_with_list(input())
    if res == 'try_again':
        i = i
    else:
        i += 1
