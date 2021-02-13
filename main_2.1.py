inp = str(input())

item_list = inp.split(' ')

#print('st 3 = ', inp)

if item_list[3] == '2017':

    if item_list[1] == 'click':

        if item_list[0] == 'yang':
            print('1')

        elif item_list[0] == 'sqlpl':
            print('0')

    elif item_list[1] == 'xtend':

        if item_list[0] == 'yang':
            print('3')

        elif item_list[0] == 'sqlpl':
            print('2')


elif item_list[3] == '1958':

    if item_list[1] == 'sqlpl':

        if item_list[0] == 'click':
            print('4')

        if item_list[0] == 'xtend':
            print('5')

    elif item_list[1] == 'yang':
        print('6')
#print(item_list[0])
#print(item_list[1])
#print(item_list[2])
#print(item_list[3])
#print(item_list)