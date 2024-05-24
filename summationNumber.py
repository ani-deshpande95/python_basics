def summationNumber() :
    number = 1
    sum = 0 

    sumationNumber =  input("Enter summation number : ")

    while number <= int(sumationNumber) : 
        sum = sum + number
        number += 1

    print("Summation of {} is {}".format(sumationNumber, sum))


summationNumber()