def mergeSort(start, end):
    if len(end) > 1 or len(start) > 1:

        # Finding the mid of the array
        end_mid = len(end) // 2
        start_mid = len(start) // 2

        # Dividing the array elements
        end_left = end[:end_mid]
        start_left = start[:start_mid]
        end_right = end[end_mid:]
        start_right = start[end_mid:]

        # Sorting
        mergeSort(start_left, end_left)
        mergeSort(start_right, end_right)

        i = j = k = 0

        while i < len(end_left) and j < len(end_right):
            if end_left[i] < end_right[j]:
                end[k] = end_left[i]
                start[k] = start_left[i]
                i += 1
            else:
                end[k] = end_right[j]
                start[k] = start_right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(end_left):
            end[k] = end_left[i]
            start[k] = start_left[i]
            i += 1
            k += 1

        while j < len(start_left):
            end[k] = end_right[j]
            start[k] = start_right[j]
            j += 1
            k += 1


def activitySelection(start, end, n):
    # Sort activities according to end time
    mergeSort(start, end)

    # selected activities
    selected_activities = []
    selected_activities.append(start[0])
    i = 0
    for j in range(1, n):
        if start[j] >= end[i]:
            selected_activities.append(start[j])
            i = j
    return selected_activities


if __name__ == '__main__':
    N = 6
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    print(activitySelection(start, end, N))
