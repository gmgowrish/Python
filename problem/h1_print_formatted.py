number = 17
width = len(bin(number)[2:])
for i in range(1, number + 1):
    hex_c = hex(i)
    final = hex_c.upper()
    print(str(i).rjust(width), oct(i)[2:].rjust(width), final[2:].rjust(width), bin(i)[2:].rjust(width), )
