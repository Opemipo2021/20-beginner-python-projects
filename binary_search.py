my_list = [2, 5, 7, 8, 9, 10, 14, 17, 18, 19, 20]

x = input("Enter a nuber: ")
x = int(x)


def binarySearch(my_new_list, l, h, x):
    if h >= l:
        m = (h + l) // 2

        if my_new_list[m] == x:
            return my_new_list
        elif my_new_list[m] > x:
            return binarySearch(my_new_list, l, m-1, x)
        else:
            return binarySearch(my_new_list, m+1, h, x)
    else:
        return -1


r = binarySearch(my_list, 0, len(my_list)-1, x)

if r != -1:
    print("Number is present at index", str(r))

else:
    print("Number is not present in list")
