def bubblesort(list1):
    for i in range (len(list1)-1,0,-1):
        for j in range (i):
            if list1[j] < list1[j+1]:
                temp= list1[j+1]
                list1[j+1]=list1[j]
                list1[j] = temp


def mergesort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    middle = len(unsorted)//2
    left = unsorted[:middle]
    right = unsorted[middle:]

    left = mergesort(left)
    right= mergesort(right)
    return (merge(left,right))

def merge(left,right):
    res = []

    while (len(left) !=0) and (len(right) != 0):
        if (left[0] < right[0]):
            res.append(left[0])
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])
    if (len(left) ==0):
        res = res+right
    else:
        res = res+left
    return res
def insertion(list1):
    for i in range(1,len(list1)):
        j=i-1
        next_elem = list1[i]

        while (list1[j] < next_elem) and (j >= 0) :
            list1[j+1] = list1[j]
            j=j-1
        list1[j+1] = next_elem
def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

# Reduce the gap for the next element

        gap = gap//2
def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

                   
list = [19,2,31,45,6,11,121,27]


insertion(list)
print list
