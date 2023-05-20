list1 = []
list2 = []

def get_numbers():
    while True:
        user_input = int(input('Adad ra vared konid :'))
        list1.append(user_input)
        if user_input < 0:
            break

    print('Adade voroodi shoma :' , list1)


def multiple_numbers():
    multiple = int(input('Zarb dar chand beshe? :'))

    for i in list1:
        list2.append(i * multiple)

    print('Inam az list asase zarb shode' , list2)

get_numbers()
multiple_numbers()