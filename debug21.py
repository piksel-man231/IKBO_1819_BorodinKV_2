inp = str(input())

item_list = inp.split(' ')

if item_list[3] == 'pawn':

    if item_list[0] == 'tcsh':

        if item_list[1] == '1994':
            print(0)
        elif item_list[1] == '2020':
            print(1)
        else:
            print(2)

    elif item_list[0] == 'chuck':

        if item_list[2] == 'haml':
            print(3)
        elif item_list[2] == 'toml':
            print(4)
        else:
            print(5)

    else:

        if item_list[1] == '1994':
            print(6)
        elif item_list[1] == '2020':
            print(7)
        else:
            print(8)


elif item_list[3] == 'csv':

    print(9)

elif item_list[3] == 'kit':

    print(10)