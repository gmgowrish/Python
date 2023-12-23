# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#
#     # Use zip to group characters from the same index together
#     for i, char_group in enumerate(zip(*strs)):
#         print(i, char_group)
#         if len(set(char_group)) != 1:
#             # If the characters in the group are not the same, return the common prefix found so far
#             return strs[0][:i]
#
#     # If all characters passed the above check, return the entire first string as the common prefix
#     return strs[0]
#
#
# # Example usage:
# strs1 = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs1))


# str = ['gmg', 'gpp']
#
# for i, char_group in enumerate(zip(*str)):
#     if len(set(char_group)) != 1:
#         # If the characters in the group are not the same, return the common prefix found so far
#         a = str[0][:i]
#         # print(a)
#     print(i, char_group)


def longestCommonPrefix(strs):
    if not strs:
        return ""

    common_prefix = strs[0]
    # print(common_prefix)  # ab

    for s in strs[1:]:
        # print(s)
        i = 0
        while i < len(common_prefix) and i < len(s) and common_prefix[i] == s[i]:
            # print(i)
            # print(len(common_prefix))
            # print(len(s))
            # print(s[i])
            i += 1
            # print(common_prefix[:i])
        common_prefix = common_prefix[:i]

    print(common_prefix)


strs = ["aba", "ab"]
print(longestCommonPrefix(strs))
