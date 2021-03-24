def f22(a):
    a = str(a)
    a = a.replace('0x', '')
    # print('A = ', a)

    a = int(a)
    b = bin(a)
    # print('B = ', b)

    a = str(b)
    a = a.replace('0b', '')

    # print('A = ', a)
    # print(a)
    list1 = list(map(list, a))
    # print(list1)

    list_e = []
    list_e.append(list1.pop(0))

    list_d = []
    list_d.append(list1.pop(0))
    # print(list1)
    # print(list_d)

    list_c = []
    for i in range(1, 4):
        list_c.append(list1.pop(0))
    # print(list_c)

    list_b = []
    for i in range(1, 16):
        list_b.append(list1.pop(0))
    # print(list_b)

    list_a = []
    for i in range(1, 13):
        list_a.append(list1.pop(0))
    # print(list_a[0])

    list_final = []

    list_final.append(list_e[0][0])

    for i in range(0, 12):
        list_final.append(list_a[i][0])

    for i in range(0, 15):
        list_final.append(list_b[i][0])

    for i in range(0, 3):
        list_final.append(list_c[i][0])

    list_final.append(list_d[0][0])
    # print(list_final[0][0])
    final = ''.join(list_final)
    final = int(final, 2)
    # print(final)
    final = hex(final)
    return final


print(f22(0xa46740fb))

# 1 0 100 100011001110100 000011111011
# 1 0 100 100011001110100 000011111011
# 1 000011111011 100011001110100 100 0
