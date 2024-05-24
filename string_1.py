'''
Strings are immutable in Python
'''


def string_len() :
    name = "Anirudha"
    print(len(name))
    print(name[1])
    print(name[-2])


def string_slice() :
    fullName = "Anirudha Deshpande"
    print(fullName[7:])  # This will include 7
    print(fullName[:2])  # This will not include 2 it will display till 1
    print(fullName[2:5]) # This will include 2 but not 5

    # String slice through [] never include last character i.e. number that
    # user specified


def string_indexing() :
    fullString = "I an Anirudha Deshpande"
    newFullString = fullString[:3] + "m" + fullString[4:] # For string replacement use this
    print(newFullString)
    print(newFullString.index("m"))
    print(newFullString.index("Ani"))
    print(newFullString.index("a")) # index will always return index of only first matching character
    # print(newFullString.index("x")) # will return value error : substring not found
    print("D" in newFullString)     # "string" in "string" will return true or false
    print("x" in newFullString)


def replace_email(old="gmail.com", new="python.com"):
    email = ["anirudha@gmail.com", "ani@gmail.com"]
    for e in email:
        if "@" + old in e :
            index = e.index("@" + old)
            new_email = e[:index] + "@" + new
            e = new_email
            email = e 
    print(email)

# replace_email()


def stringMethods() : 
    a = "LOWER"
    print(a.lower())

    a.upper()

    b = "Test slice       ...      "
    print(b.strip())            # Will remove the spaces at both ends of the string

    b.startswith("t")              # return boolean according to the value provide
    b.endswith("E")                # return boolean according to the value provide

    b.isnumeric()                   # return boolena if it contains numbers entirely

    print(" a ".join(["bb", "cc", "dd", "ee"]))               # join string with each string present in join requires list if passing multiple strings

    print("Test, test, test".split(","))            # It will split the string using geven parameter, by default it will take space  
    

stringMethods()

