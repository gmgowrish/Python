def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']


def reverseString(s):

    for i in range(len(s) // 2):
        s[i], s[-i - 1] = s[-i - 1], s[i]


s = ['hello']
reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
