from ReTask.TaskClass.taskClass import Task

def ambilSemuaData() : 
    semuaDataTask = []

    with open("ReTask/Database/Database.txt", "r") as data:
        isiData = data.readlines()
        
    for i in range(len(isiData)) :
        cleanedCommaInstance = isiData[i].split(",")

        #cari nama task
        taskName = cleanedCommaInstance[1]

        #cari span task
        uncleanSpanInstance = cleanedCommaInstance[2].split(" ")
        for j in uncleanSpanInstance:
            if j == '' :
                continue
            else :
                taskSpan = int(j)
                if "our" in uncleanSpanInstance[-1] :
                    taskSpan = taskSpan * 60
                break

        #cari deadline task
        uncleanDeadlineInstance = cleanedCommaInstance[3].split(" ")
        for j in uncleanDeadlineInstance:
            if j == '':
                continue
            else :
                deddate = j        
                break
        taskDeadline = deddate + ", " + uncleanDeadlineInstance[-1]
        
        thisTaskInstance = Task(taskName, taskSpan, taskDeadline)
        semuaDataTask.append(thisTaskInstance)

    return semuaDataTask

def saveChanges(taskList):
    lstTask = taskList

    with open("ReTask/Database/Database.txt", "w") as writeD:
        text = ""
        for i in range(len(lstTask)):
            text = text + str(i) +"," + lstTask[i].getName() + ", " + str(lstTask[i].getSpan()) +" minutes, " + str(lstTask[i].getDeadline()) + "\n"
        
        writeD.write(text)


