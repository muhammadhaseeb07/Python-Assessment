

def equilibriumPoint(A, n):
    if n == 1:
        return A[0]
    elif n != 0 and n != 2:
        for i in range(1, n - 1):
            left_values_sum = sum(A[0:i])
            right_values_sum = sum(A[i + 1:n])
            if left_values_sum == right_values_sum:
                return A[i]
    return -1


if __name__ == '__main__':
    A = [4, 3, 2, 2]
    n = 5
    print(equilibriumPoint(A, n))

