# inp = str(input())
item_list = []
def f21(item_list):

# print('st 3 = ', inp)

    if item_list[3] == 'pawn':

        if item_list[0] == 'tcsh':

            if item_list[1] == 1994:
                return 0
            elif item_list[1] == 2020:
                return 1
            else:
                return 2

        elif item_list[0] == 'chuck':

            if item_list[2] == 'haml':
                return 3
            elif item_list[2] == 'toml':
                return 4
            else:
                return 5

        else:

            if item_list[1] == 1994:
                return 6
            elif item_list[1] == 2020:
                return 7
            else:
                return 8

    elif item_list[3] == 'csv':

        return 9

    else:

        return 10

# print(item_list[0])
# print(item_list[1])
# print(item_list[2])
# print(item_list[3])
# print(item_list)
#f21(['http', 2019, 'diff', 'pawn'])