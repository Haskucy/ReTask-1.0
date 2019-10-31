"""
This is the main class
"""
import datetime
from TaskClass.taskClass import Task
from ListTask.listTask import ListTask

#Setup
def CheckTask() :
    for i in lstRendya.listTask:
        print(i.name + " -> Deadline : "+  str(i.deadline))
    print("\n\n")

def newTask():
    textnew = "Please insert your new task in this format :\n [name],[estimatedspan],[(deadline)]"
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
            break
    for i in separate3:
        if i == '':
            continue
        else :
            deddate = i

            break
    taskDeadline = deddate + ", " + separate3[-1]
    print(taskDeadline)
    CreateTask = Task(taskName, taskspan, taskDeadline)
    lstRendya.listTask.append(CreateTask)
    print("Successfully added task : " + CreateTask.name)

print("Successfully Started")
belajarMD = Task("Belajar Matdas",30, "today, 21:00:00")
Mandi = Task("Mandi",30, "2019-11-01, 21:40:00")
AljabarLinear = Task("Alin",120, "today, 21:40:00")
lstT = [belajarMD,Mandi,AljabarLinear]
lstRendya = ListTask(lstT)
x = True

while x == True:
    texthello ="Hello User, what do you want me to do?\n"
    text1 = "1. Check your task\n"
    text2 = "2. Add new task\n"
    text3 = "3. Select task\n"
    text0 = "0. Exit\n"
    textSelect = "Please choose based on number"
    mainApp = str(input(texthello + text1 + text2 + text3 + text0 + textSelect))

    if mainApp == "1":
        CheckTask()
    elif mainApp == "2":
        newTask()
