import datetime
from TaskClass.taskClass import Task

class ListTask():
    """docstring for ListTask."""

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
