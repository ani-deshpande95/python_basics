import time


def status():
    status_one = [1,2,3,4,5,6,7,8,9,10]
    status_two = [11,12,13,14,15,16,17,18,19,20]

    for i in status_one:
        print("status_one: ", str(i))
        time.sleep(1)
        user_touch = input('Do you want to interrpt')
        print(user_touch)
        if(user_touch == ''):
            for i in status_one:
                print("status_one: ", str(i))
                time.sleep(1)
            

    for i in status_two:
        print("status_two: ", str(i))
        time.sleep(1)

status()
