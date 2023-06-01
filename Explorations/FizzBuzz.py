
# for i in range(101):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

for i in range(101):
    output = ""
    if i % 3 == 0: output += "Fizz"
    if i % 5 == 0: output += "Buzz"
    if output == "": output = i
    print(output)
