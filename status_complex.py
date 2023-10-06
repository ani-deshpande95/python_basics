import time

def status():
    status_list = [[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20], [21,22,23,24,25,26,27,28,29,30]]
    user_input = input('When do you want to interrupt the status')
    user_hits = input('What do you want to hit? next or back')
    status_loop = True
    
    while status_loop:
        for i in status_list:
            status_loop = False
            for j in i:
                print("status: ", str(j))
                time.sleep(1)
    
                if (user_input == str(j) and user_hits == "next"):
                    break
                
            if (user_input == str(j) and user_hits == "back"):
                    status_loop = True
                    break

status()
