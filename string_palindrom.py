input_string = "madam issi madam"

# print(input_string[-1])

def reverse(input) : 
    str = ""
    for i in input:
        str = i + str
    
    return str


def is_palindrom(input_string) : 
    j = reverse(input_string)
    if input_string == j :
        print('Its palindrom')
    else:
        print('Its no palindrom')
    


# reverse(input_string)
is_palindrom(input_string)