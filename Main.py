"""
This is the main class
"""
import datetime
from TaskClass.taskClass import Task
from ListTask.listTask import ListTask
print("Successfully Started")

belajarMD = Task("Belajar Matdas",30, "12 Januari 2020")
Mandi = Task("Mandi",30, "14 Januari 2020")
AljabarLinear = Task("Alin",120, "13 Januari 2021")

lstT = [belajarMD,Mandi,AljabarLinear]

lstRendya = ListTask(lstT)
print(lstRendya)
