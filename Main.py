"""
This is the main class
"""
import datetime
from TaskClass.taskClass import Task
from ListTask.listTask import ListTask
print("Successfully Started")

belajarMD = Task("Belajar Matdas",30, "today, 21:00:00")
Mandi = Task("Mandi",30, "2019-11-01 , 21:40:00")
AljabarLinear = Task("Alin",120, "today , 21:40:00")

lstT = [belajarMD,Mandi,AljabarLinear]

lstRendya = ListTask(lstT)
print(lstRendya)
