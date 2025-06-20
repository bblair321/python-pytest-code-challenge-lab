def longest_palindromic_substring(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    n = len(s)
    if n == 0:
        return ""
    if n == 1:
        return s

    start = 0
    max_len = 1

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(n):
        left1, right1 = expand_around_center(i, i)
        length1 = right1 - left1 + 1
        if length1 > max_len:
            start = left1
            max_len = length1

        left2, right2 = expand_around_center(i, i + 1)
        length2 = right2 - left2 + 1
        if length2 > max_len:
            start = left2
            max_len = length2

    return s[start:start + max_len]
