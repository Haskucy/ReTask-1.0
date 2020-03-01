"""
This is the main class
"""
import datetime
from ReTask.TaskClass.taskClass import Task
from ReTask.ListTask.listTask import ListTask
from ReTask.Database import TaskDB




#Setup : Needed Func
def CheckTask() :
    print("\nThis is your task right now : \n")
    for i in range(len(lstRendya.listTask)):
        c = lstRendya.listTask[i]
        print(str(i+1) + ". " + c.name + " -> Deadline : "+  str(c.deadline))
    print("\n")

def newTask():
    textnew = "\nPlease insert your new task in this format :\n [name],[estimatedSpan],[(deadline)]"
    textexample = 'Belajar Matdas, 30 minutes, today 21:00:00\n'
    newTask = input(textnew + "\nexample : " +textexample)
    separate1 = newTask.split(",")
    separate2 = separate1[1].split(" ")
    separate3 = separate1[2].split(" ")
    taskName = separate1[0]
    for i in separate2:
        if i == '' :
            continue
        else :
            taskspan = int(i)
            if "our" in separate2[-1] :
                taskspan = taskspan * 60
            break
    for i in separate3:
        if i == '':
            continue
        else :
            deddate = i        
            break
    taskDeadline = deddate + ", " + separate3[-1]
    print(separate2) #debug
    CreateTask = Task(taskName, taskspan, taskDeadline)
    lstRendya.listTask.append(CreateTask)
    print("\nSuccessfully added task : " + CreateTask.name)

def selectTask():
    CheckTask()
    selectT = int(input("Select your task based on number:\n"))
    theTask = lstRendya.listTask[selectT-1]
    print(theTask)

def sortTaskbyDeadline():
    lstRendya.sort()
    print("\nSuccessfully sorted!")

def deleteTask():
    CheckTask()
    selectT = int(input("Select task that you want to delete based on number:\n"))
    lstRendya.deleteTask(selectT)
    
    







#Setup : Started
print("\nSuccessfully Started\n")

#belajarMD = Task("Belajar Matdas",30, "today, 21:00:00")
#Mandi = Task("Mandi",30, "2019-11-01, 21:40:00")
#AljabarLinear = Task("Alin",120, "today, 21:40:00")
#lstT = [belajarMD,Mandi,AljabarLinear]

lstDb = TaskDB.ambilSemuaData()
lstRendya = ListTask(lstDb)
stateProgram = True








#Real Stuff
texthello ="Hello User, what do you want me to do?\n"
while stateProgram == True:
    text1 = "1. Check your task\n"
    text2 = "2. Add new task\n"
    text3 = "3. Select task\n"
    text4 = "4. Sort Task By Deadline\n"
    text5 = "5. Delete Task\n"
    text0 = "0. Exit\n"
    textSelect = "Please choose based on number:\n"
    mainApp = str(input(texthello + text1 + text2 + text3 + text4 + text5 + text0 + textSelect))

    if mainApp == "1":
        CheckTask()
    elif mainApp == "2":
        newTask()
    elif mainApp == "3" :
        selectTask()
    elif mainApp == "4":
        sortTaskbyDeadline()
    elif mainApp == "5":
        deleteTask()
    elif mainApp == "0":
        print("\nHave a good day sir")
        exit()

    texthello = "What do you want next?\n"
