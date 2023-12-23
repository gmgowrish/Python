import ctypes

arrayType = ctypes.py_object * 5

slots = arrayType()
# print (slots[0])
for i in range(5):
    slots[i] = None
    slots[1] = 12
    slots[4] = 45
    slots[3] = 9

    print(slots[i])
