def summationNumber() :
    number = 1
    sum = 0 

    sumationNumber =  input("Enter summation number : ")

    while number <= int(sumationNumber) : 
        sum = sum + number
        number += 1

    print("Summation of {} is {}".format(sumationNumber, sum))


summationNumber()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def summation(number):
    sum = 0
    for x in range(number+1):
        sum = sum + x

    print(sum)


summation(5) 
