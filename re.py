# class animals():
#     def __init__(self):
#         print("animal is created :")
#     def name(self):
#         print("animals")
#     def do (self):
#         print("runs")
#
#
# class Kangaroo(animals):
#     def __init__(self):
#         super().__init__()
#         print("kangroo is created ")
#     def name(self):
#         print("kangaroo")
#     def jumps (self):
#         print("jumps")
#
#
# kan = Kangaroo()
# kan.__init__()
# kan.name()
# kan.jumps()
# kan.do()                                   import re
#
# #Check if the string starts with "The" and ends with "Spain":
#
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
#
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

x = 'coder'
for i in range(len(x)):
    x[i].upper()
print(x)
