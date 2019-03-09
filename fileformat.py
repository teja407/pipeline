import re
import sys
import json

#f = open("test.out", 'w')
#errorJSON = {}

with open ("/var/lib/jenkins/workspace/hive-python/stderr", "r") as myfile:
    data = myfile.readlines()
    str = ''.join(data)
    #sys.stdout = f
    tablename= re.search("(tableName:\w+)",str)
    tablenamesplit = re.split(":",tablename.group(1),1)
    dbname = re.search("(dbName:\w+)", str)

    dbnamesplit = re.split(":", dbname.group(1), 1)
    #errorData = {}
    #errorData["Database"] = dbname
    #errorJSON["DateTimeSTamp"] = errorData
    #print(tablename)
    #print(dbname)
    #print(tablename.group(1))
    #print(dbname.group(1))
    #print(tablenamesplit[1])
    global textRead
    global statusRead
    for x in data:

        if x.__contains__("Caused by"):
            textRead = x
            #print(textRead)
            break
        if x.__contains__("Status"):
            statusRead = x
            #print(statusRead)
    #sys.stdout = f
    errorData = {
        "Database": dbnamesplit[1],
        "table": tablenamesplit[1],
        "status": statusRead,
        "caused by": textRead

    }

    # convert into JSON:
    y = json.dumps(errorData)

    # the result is a JSON string:
    print(y)


#f.close()




#f.close()

