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


def maxMeetings(start, end, n):
    # Sort activities according to end time
    mergeSort(start, end)

    # selected activities
    meetings_count = 1
    i = 0
    for j in range(1, n):
        if start[j] > end[i]:
            meetings_count += 1
            i = j
    return meetings_count


if __name__ == '__main__':
    N = 8
    start = [75250, 50074, 43659, 8931, 11273,
             27545, 50879, 77924]
    end = [112960, 114515, 81825, 93424, 54316,
           35533, 73383, 160252]
    print(maxMeetings(start, end, N))
