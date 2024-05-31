# ------------------------------------------------------------------------------------------------------------------------------------------------------- #
def whileLoops() : 
    i = 1
    while i < 5 :                               #This will execute till 1-4 
        print("...... inside loop ......", i)   # While loop will keep executing until while condtion becomes false
        i = i + 1

    print(">>>>>> outside loop >>>>>>", i)

#whileLoops()

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def whileLoops_1() :
    i = 1
    while i <= 5 :                                  # This will execute till 1-5
        print("...... inside loop ......", i)
        i = i + 2

    print(">>>>>> outside loop >>>>>>", i)

# whileLoops_1()


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def whileloop_3() :
    x = 0                                   # Intialization
    while x <= 5 :                          # Condition
        print("Hello", x)                   # Body of the loop
        x = x + 1                           # increment condition                
    print("End..",x)                        # End / return condition

# whileloop_3()

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def whileloop_4() :
    a = 5
    while a < 10 :
        print("Hello.....")
        a += 1


# whileloop_4()

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def whileloop_5() :
    x = 1
    sum = 0

    while x <= 10 :                                    # This loop will execute first and will set the x value to 10
        sum = sum + x
        x += 1

    
    product = 1     
    # x = 1                                         
    print("x in product...........", x)                 # Here x value is already 10
    while x <= 10 :                                      # This loop will not get executed as while condition becomes false
        print("x in product...........", x)             # user may need to initialize variable again if want to use same variable
        product = product * x
        x += 1

    print(sum , product)


# whileloop_5()


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def infiniteLoop() : 
    x = 0
    while x % 2 == 0 :  
        x = x / 2                       # 0 / 2 = 0 
        print("H")                      # Hence this will go into infinite loop to avoid this we can use if conditions
                                        # Or mat be we can another condition to this while e.g. while x != 0 and x % 2 == 0


# infiniteLoop()


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

def print_range(start, end) : 
    n = start
    while n <= end : 
        print(n)
        n += 1

print_range(1, 5)


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #















# ------------------------------------------------------------------------------------------------------------------------------------------------------- #











# ------------------------------------------------------------------------------------------------------------------------------------------------------- #











# ------------------------------------------------------------------------------------------------------------------------------------------------------- #











# ------------------------------------------------------------------------------------------------------------------------------------------------------- #











# ------------------------------------------------------------------------------------------------------------------------------------------------------- #












# ------------------------------------------------------------------------------------------------------------------------------------------------------- #













# ------------------------------------------------------------------------------------------------------------------------------------------------------- #