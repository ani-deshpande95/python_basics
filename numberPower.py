
def generatePower() :
    input = [2,3,4,5]
    output = []
    for i in range(len(input)) :
        j = input[i] ** (i+2)
        output.append(j)
    
    print(output)

generatePower()