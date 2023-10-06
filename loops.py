# x = 0

# while x < 5:
#     print("Not there yet, x = " + str(x))
#     x += 1

# print("X = ", str(x))

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt = "+str(x))
        x += 1
    print("Loop exited")

# attempts(5)

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def count_down(start_number):
    x = start_number
    while x > 0:
        print("Counting down: " + str(x))
        x -= 1
    print("Zero")

# count_down(10)

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def infinite_loop(number):
    x = number
    while x % 2 == 0 and x != 0:
        x = x/2
        print("x = " +str(x))
    print("x after loop : " + str(x))

# infinite_loop(100)

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def print_countdown(start, end):
    x = start
    while x <= end:
        print("x = "+str(x))
        x += 1
    print("x after loop completed : "+str(x))

print_countdown(1, 10)