import maya.cmds as cmds
import sqlite3
from sqlite3 import Error
from os import listdir
from os.path import isfile, join, isdir
from types import *
import sys
import re

homePath = os.path.expanduser('~')
scriptsFolder = os.path.join(homePath, 'maya/2018/scripts/')
#temporary location
tempScriptsFolder = 'D:\\Student Data\Documents\AMS'
#print(str(scriptsFolder))
sys.path.append(str(tempScriptsFolder))
import _AMS_CustomFileManager as CFM
import _AMS_AddToDB as Add_DB
reload(Add_DB)

#pull in and set custom lists if they exist
local_DescList = CFM.getFile("DescriptionList")
local_StateList = CFM.getFile("StateList")

versionModifiers = [
    'test', 'final', 'testing', 't'
]

def create_connection(db_file):
    #create a database connection to a SQLite database
    """
    create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def searchDirectory(directoryPath):
    #search a directory and return a tuple of lists, files, folders and extraneous files.
    allResults = listdir(directoryPath)
    print(str(allResults))

    justFiles = [f for f in allResults if isfile(join(directoryPath,f))]
    print(str(justFiles))

    justDirectories = [fi for fi in allResults if isdir(join(directoryPath,fi))]
    print(str(justDirectories))

    return justFiles

def sortFiles(fileList):
    #sort files from list by file type to determine what should go into the database and what is to be ignored.
    acceptableItems = ['ma', 'mb', 'zpr']
    sortedFiles = []
    for item in fileList:
        itemSuffix = item.split(".")
        errorMessage = None
        try:
            if itemSuffix[1] in acceptableItems:
                sortedFiles.append(item)
            #print(str(sortedFiles))
            elif itemSuffix[1] not in acceptableItems:
                print(str(item) + " was not in acceptableList")
            else:
                errorMessage = "index error with: " + str(item)
                print(errorMessage)
        except IndexError:
            if errorMessage is not None:
                print(str(errorMessage))
    return sortedFiles

def checkForConventions (trimmedFileName):
    #check name for regular conventions
    print ("checking: " + str(trimmedFileName))

    #split name down again to it's pieces
    nameParts = trimmedFileName.split("_")

    #set counter
    partsCount = len(nameParts)
    i = 0
    print(str(partsCount))

    results = dict();
    #check each section of the name if it exists to see if it contains any keywords
    while i < partsCount :

        if i is 0:
            #check if anything in this matches anything in any of the lists
            print("First! "+str(nameParts[0]))
            if nameParts[0].lower() in local_DescList:
                print("add "+ str(nameParts[0])+ " to Description!")
                results['Desc'] = str(nameParts[0])
            elif nameParts[0].lower() in local_StateList:
                print("add this to State!")
                results['State'] = str(nameParts[0])
            else:
                match = re.search("([a-zA-Z]+)(\d*)", str(nameParts[0]))
                if match:
                    if len(match.group(1)) == 0 and len(match.group(2)) == 0:
                        print("no match")
                    elif len(match.group(2)) == 0:
                        #check if the first part is a test or final, if so add to dictionary and break out
                        if match.group(1).lower() in versionModifiers:
                            results['Version'] = nameParts[0]

                    else:
                        print(str(match.group(1)))
                        print(str(match.group(2)))
                        results['Version'] = nameParts[0]
        elif i is 1:
            print("Second! "+str(nameParts[1]))
            if nameParts[1].lower() in local_DescList:
                print("add "+ str(nameParts[1])+ " to Description!")
                results['Desc'] = str(nameParts[1])
            elif nameParts[1].lower() in local_StateList:
                print("add this to State!")
                results['State'] = str(nameParts[1])
            else:
                match = re.search("([a-zA-Z]+)(\d*)", str(nameParts[1]))
                if match:
                    if len(match.group(1)) == 0 or len(match.group(2)) == 0:
                        print("no match")
                    elif len(match.group(2)) == 0:
                        #check if the first part is a test or final, if so add to dictionary and break out
                        if match.group(1).lower() in versionModifiers:
                            results['Version'] = nameParts[1]
                    else:
                        print(str(match.group(1)))
                        print(str(match.group(2)))
                        results['Version'] = nameParts[1]

        elif i is 2:
            print("Third! " + str(nameParts[2]))
            if nameParts[2].lower() in local_DescList:
                print("add "+ str(nameParts[2])+ " to Description!")
                results['Desc'] = str(nameParts[2])
            elif nameParts[2].lower() in local_StateList:
                print("add this to State!")
                results['State'] = str(nameParts[2])
            else:
                match = re.search("([a-zA-Z]+)(\d*)", str(nameParts[2]))
                if match:
                    if len(match.group(1)) == 0 or len(match.group(2)) == 0:
                        print("no match")
                    elif len(match.group(2)) == 0:
                        #check if the first part is a test or final, if so add to dictionary and break out
                        if match.group(1).lower() in versionModifiers:
                            results['Version'] = nameParts[2]
                    else:
                        print(str(match.group(1)))
                        print(str(match.group(2)))
                        results['Version'] = nameParts[2]

        elif i is 3:
            print("Fourth! " + str(nameParts[3]))
            if nameParts[3].lower() in local_DescList:
                print("add "+ str(nameParts[3])+ " to Description!")
                results['Desc'] = str(nameParts[3])
            elif nameParts[3].lower() in local_StateList:
                print("add this to State!")
                results['State'] = str(nameParts[3])
            else:
                match = re.search("([a-zA-Z]+)(\d*)", str(nameParts[3]))
                if match:
                    if len(match.group(1)) == 0 or len(match.group(2)) == 0:
                        print("no match")
                    elif len(match.group(2)) == 0:
                        #check if the first part is a test or final, if so add to dictionary and break out
                        if match.group(1).lower() in versionModifiers:
                            results['Version'] = nameParts[3]
                    else:
                        print(str(match.group(1)))
                        print(str(match.group(2)))
                        results['Version'] = nameParts[3]

        i = i + 1
    print (str(results))
    return results

def fileDB_Prep(sortedFile, currentPath):
    #take in a single sorted file and from that extrapolate information to put into the database
    #Info must be in THIS order: Name, asset_Description, asset_PipelineState, Version, FileType, FileLocation
    preppedFile = []
    #Take name file and split off file extension
    mainNameSplit = sortedFile.split('.')
    #print(str(mainNameSplit[0]))

    #add the normal name
    preppedFile.append(mainNameSplit[0])
    try:
        nameParts = mainNameSplit[0].split("_")
        if len(nameParts) > 1:
            #if there is multiple parts, then send whole name into convention checker
            print("we've got underscores!")
            resultsDict =checkForConventions(mainNameSplit[0])

            #add the asset_Description
            try:
                if resultsDict['Desc'] is not NoneType:
                    preppedFile.append(resultsDict['Desc'])
            except KeyError:
                preppedFile.append('Null')

            #add the asset_PipelineState
            try:
                if resultsDict['State'] is not NoneType:
                    preppedFile.append(resultsDict['State'])
            except KeyError:
                preppedFile.append('Null')

            #add the version
            try:
                if resultsDict['Version'] is not NoneType:
                    preppedFile.append(resultsDict['Version'])
            except KeyError:
                preppedFile.append('Null')

        elif len(nameParts) < 2:
            print("No underscores!")
            i = 1
            while i < 4:
                preppedFile.append('Null')
                i += 1



    except ValueError:
        print("Index Error: Can't break down this name!")

    #add the FileType
    preppedFile.append(str(mainNameSplit[1]))

    #add the file location
    preppedFile.append(str(currentPath))
    #is it better to have the folder it's in, or the full call to the exact file?
    #fileLocation = os.path.join(currentPath, )

    print(str(preppedFile))


    return preppedFile

def checkDB_Duplicates(conn,currentItem):
    """
    check if the record already exists
    :param conn:
    :param currentItem:
    :return:
    """
    #itemStuff = [str(currentItem[0]),str(currentItem[5])]
    itemName = [str(currentItem[0]),]
    print(itemName)
    sql = '''SELECT * FROM files WHERE name=?'''
    cur = conn.cursor()
    cur.execute(sql,itemName)
    results = cur.fetchall()
    return results

def main():
    #database = "C:\\Users\MAE\Documents\MayaPython\AMS\AssetManagementSystem.db"
    database = "D:\\Student Data\Documents\AMS\AssetManagementSystem.db"

    #tempTestPath = "D:\\Student Data\Downloads"
    tempTestPath = "D:\\Student Data\Desktop\GROVE\Raw Assets\MayaGroveArt\scenes"
    currentTestPath = tempTestPath
    fileList = searchDirectory(tempTestPath)
    sortedFiles = sortFiles(fileList)
    print("final sorted List: " + str(sortedFiles))

    preppedFiles = []
    #take each file for db and prep it
    for sortedFile in sortedFiles:
        preppedFile = fileDB_Prep(sortedFile, currentTestPath)
        preppedFiles.append(preppedFile)

    print("PreppedFiles: " + str(preppedFiles))

    print("adding " + str(preppedFiles[0]) + " to database" )
    print("adding " + str(preppedFiles[2]) + " to database")
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        print("Database available")
    else:
        print("Error! Cannot create the database connection!")

    # take each prepped file and feed it into the database one at a time
    for F in preppedFiles:
        with conn:
            # check if there is an entry for this data already
            matching_result = checkDB_Duplicates(conn, F)
        print("Match results: " + str(matching_result))

        if len(matching_result) == 0:
            with conn:
                file_id = Add_DB.create_file(conn, F)
            print(file_id)

if __name__ == '__main__':
    main()



