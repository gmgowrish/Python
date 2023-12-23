from array import array

theCounter = array('i', [0] * 256)
theFile = open('../Tools/java_program_coding_ninjas.bat', 'rb')

for line in theFile:
    for letter in line:
        theCounter[letter] += 1

theFile.close()

for i in range(26):
    print("%c - %4d   %c - %4d" % (chr(65 + i), theCounter[65 + i], chr(97 + i), theCounter[97 + i]))

# when i is 0, chr(65 + 0) is 'A'. When i is 1, chr(65 + 1) is 'B', and so on. This allows you to print characters
# from 'A' to 'Z' (uppercase letters) in your loop.

# Similarly, you can use chr(97 + i) to print characters from 'a' to 'z' (lowercase letters) because 'a' corresponds
# to the numeric value 97 in the ASCII encoding.
