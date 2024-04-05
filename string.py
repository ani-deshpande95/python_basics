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
        if "@" + old in email :
            index = email.index("@" + old)
            new_email = email[:index] + "@" + new
            email = new_email
    print(email)


replace_email()













