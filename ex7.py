def insertionSort(arr):

    count = 0
    for j in range(1, len(arr)):

        i = 0;
        while (arr[j] > arr[i]):
            i += 1
            count += 1

        count += 1
        m = arr[j];
        for k in range(j - i):
            arr[j - k] = arr[j - k - 1]
        arr[i] = m

    print("Comparison count insertion sort", count)


data = [7, 4, 3, 8, 1, 5, 4, 2]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


def binaryInsertionSort(ar):
    count1 = 0

    for i in range(1, len(ar)):
        l = 0
        r = i - 1
        x = ar[i]

        while (l <= r):
            m = (l + r) // 2
            count1 += 1
            if (ar[m] > x):
                r = m - 1
                count1 += 1
            else:
                l = m + 1
                count1 += 1
        count1 += 1
        for j in range(i, l, -1):
            ar[j] = ar[j - 1]
        ar[l] = x
    print("Comparison count binary insertion sort", count1)

data1 = [7, 4, 3, 8, 1, 5, 4, 2]
binaryInsertionSort(data1)
print('Sorted Array in Ascending Order:')
print(data1)
