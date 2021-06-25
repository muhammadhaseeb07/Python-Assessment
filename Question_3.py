def longestSubstrDitinctChars(S):
    max_characters = 0
    end_length = dict()
    j = 0
    for i in range(0, len(S)):
        value = S[i]
        if value in end_length:
            if j < (end_length.get(value) + 1):
                j = end_length.get(value) + 1
        if max_characters < (i - j + 1):
            max_characters = i - j + 1
        end_length[S[i]] = i
    return max_characters


if __name__ == '__main__':
    S = "geeksforgeeks"
    print(longestSubstrDitinctChars(S))
