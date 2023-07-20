# without recursion
# def get_nth_fibonacci(num: int) -> int:
#     fibonacci_list = [0, 1]
#     for i in range(2, num+1):
#         fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
#     return fibonacci_list[num]

def get_nth_fibonacci(num: int) -> int:         # using recursion
    if num == 0:
        return 0
    if num == 1:
        return 1
    return get_nth_fibonacci(num - 1) + get_nth_fibonacci(num - 2)


try:
    number = int(input("Enter an index value to find its fibonacci number : "))
    print(f"The {number}th fibonacci is : ", get_nth_fibonacci(number))
except ValueError:
    print("Invalid input. Enter only integer")
