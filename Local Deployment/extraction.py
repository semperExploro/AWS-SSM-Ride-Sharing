import csv


RIDER_CSV_FILE = 'riders.csv'
DRIVER_CSV_FILE = 'drivers.csv'

def getCSVHeaders():
    with open(RIDER_CSV_FILE) as csv_file:

        # creating an object of csv reader
        # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter = ',')
    
        # list to store the names of columns
        list_of_column_names = []
    
        # loop to iterate through the rows of csv
        for row in csv_reader:
    
            # adding the first row
            list_of_column_names.append(row)
    
            # breaking the loop after the
            # first iteration itself
            break
        return list_of_column_names

def readRidersCSVFile(csvFileName):
    userInformation = []
    with open(csvFileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            userInformation.append(row)
    return userInformation


def addDrivers(category, driverDict, user):
    if (user[category] == 'Not Going'):
        return 0
    else:
        user[category] = user[category].split(",")
    if (category in driverDict):
        # If category exists
        for subTimes in user[category]:
            if subTimes not in driverDict[category]:
                # create a new subTime if none exists
                driverDict[category][subTimes] = [
                    (user["Name"], user['What is your carry capacity?'])]
            else:
                # append to existing subTime
                driverDict[category][subTimes].append((
                    user["Name"], user['What is your carry capacity?']))
    else:
        # If category doesn't exists
        subTimeDict = {}
        for subTimes in user[category]:
            subTimeDict[subTimes] = [
                (user["Name"], user['What is your carry capacity?'])]
        driverDict[category] = subTimeDict


def addRiders(category, ridersDict, user):
    if (user[category] == 'Not Going'):
        dud = 0
    elif category not in ridersDict:
        entry = {}
        entry[user[category]] = [user["Name"]]
        ridersDict[category] = entry
    elif user[category] not in ridersDict[category]:
        ridersDict[category][user[category]] = [user["Name"]]
    else:
        ridersDict[category][user[category]].append(user["Name"])


def compileDictionary(userInformation, typeDict):
    for user in userInformation:

        for category in user:

            if category == 'Timestamp' or category == 'Email' or category == 'Name' or category == 'What is your carry capacity?':

                continue
            if 'What is your carry capacity?' in user.keys():
                # Drivers
                addDrivers(category, typeDict, user)
            else:
                # Riders
                addRiders(category, typeDict, user)
