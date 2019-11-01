import datetime

from ReTask.TaskClass.taskClass import Task
from ReTask.UsefulFunc.datetimefunc import DatetimeCount

class ListTask():
    """ini menyimpan task-task yang ada"""

    def __init__(self, listofTask=None):
        self.listTask = []
        if listofTask is not None:
            for i in listofTask:
                self.listTask.append(i)

    def __str__(self):
        allTask = ""
        for i in self.listTask:
            textPerTask = i.__str__()
            allTask = allTask + textPerTask
        return allTask

    def sort(self):
        beforeSort = self.listTask

        for i in range(1, len(beforeSort)):
            key = beforeSort[i]

            j = i-1
            while j>=0 and DatetimeCount(key.deadline) < DatetimeCount(beforeSort[j].deadline):
                beforeSort[j+1] = beforeSort[j]
                j-=1
            beforeSort[j+1]= key

        self.listTask = beforeSort