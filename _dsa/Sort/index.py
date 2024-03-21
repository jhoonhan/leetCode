def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


# print(bubble_sort([2, 3, 15, 3, 46, 35, 6, 8]))


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list


# print(selection_sort([2, 3, 15, 3, 46, 35, 6, 8]))


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list


# print(insertion_sort([2, 3, 15, 3, 46, 35, 6, 8]))


def __merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)

    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return __merge(left, right)


def __swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def __pivot(my_list, pivot_index, end_index):
    if len(my_list) == 1:
        return my_list
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        print("aaaaagn!")

        if my_list[pivot_index] > my_list[i]:
            swap_index += 1
            print(f"---Inner Swapping: {my_list[swap_index]} | {my_list[i]}")
            __swap(my_list, swap_index, i)
            print(my_list)
            print("")

    print(f"swapping {my_list[pivot_index]} | {my_list[swap_index]}")
    __swap(my_list, pivot_index, swap_index)
    print(my_list)
    print("")

    return swap_index


def __quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = __pivot(my_list, left, right)
        __quick_sort_helper(my_list, left, pivot_index - 1)
        __quick_sort_helper(my_list, pivot_index + 1, right)

    return my_list


def quick_sort(my_list):
    return __quick_sort_helper(my_list, 0, len(my_list) - 1)


x = [4, 2, 1, 3]

print(quick_sort(x))
