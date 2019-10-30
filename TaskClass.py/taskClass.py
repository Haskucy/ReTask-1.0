"""
"""
import datetime

class Task():
    """docstring for Task."""

    def __init__(self, name, span, deadline, startline=datetime.datetime.now):
        self.name = name
        self.span = span
        self.deadline=deadline
        self.startline =startline
        self.start = None
        self.end = None

    # Semua method Get() Set()
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSpan(self):
        return self.span

    def setSpan(self, span):
        self.span = span

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, deadline):
        self.deadline = deadline

    def getStartline(self):
        return self.startline

    def setStartline(self, startline):
        self.startline = startline

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end
