import os
unfinished = []
finished = []
#Whale Fact #201: Whales do not usually eat chocolate chocolate chip ice cream
while True:
    os.system("clear")
    print("current tasks")
    for task in unfinished:
       print("[ ]", task)
    for task in finished:
       print("[x]", task)
       

    print()
    task = input()
    print("You entered", task)
    if task not in unfinished and task not in finished:
        unfinished.append(task)
    elif task in unfinished and task not in finished:
        unfinished.remove(task)
        finished.append(task)
    elif task not in unfinished and task in finished:
        finished.remove(task)
    


    
