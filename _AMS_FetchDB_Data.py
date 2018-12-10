import maya.cmds as cmds
import sqlite3
from sqlite3 import Error
from os import listdir
from os.path import isfile, join, isdir
from types import *
import sys
import re



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


def fetch_QueryDB (searchTerm):
    database = "D:\\Student Data\Documents\AMS\AssetManagementSystem.db"
    conn = create_connection(database)
    Term = ["%"+ str(searchTerm) +"%", "%"+ str(searchTerm) +"%"]
    print(searchTerm)
    sql = "SELECT * FROM files WHERE name LIKE (?) OR asset_pipelineState LIKE (?)"
    if conn is not None:
        with conn:
            cur = conn.cursor()
            cur.execute(sql, Term)
            results = cur.fetchall()
            print(Term)
            print(sql)
            print (results)
            return results
    else:
        print("unable to connect to Database")

def fetchDB_AsArray ():
    database = "D:\\Student Data\Documents\AMS\AssetManagementSystem.db"
    conn = create_connection(database)

    #prep lists for array
    file_id = []
    name = []
    asset_description = []
    asset_pipelineState = []
    version = []
    file_type = []
    file_location = []

    item = []

    sql = "SELECT * FROM files"

    try:
        cur = conn.cursor()
        cur.execute(sql)


        #rowcount = int(cursor.rowcount())
        results = cur.fetchall()

        for row in results:
            #row = cur.fetchone()

            file_id.append(row[0])
            name.append(row[1])
            asset_description.append(row[2])
            asset_pipelineState.append(row[3])
            version.append(row[4])
            file_type.append(row[5])
            file_location.append(row[6])

            item.append(file_id)
            item.append(name)
            item.append(asset_description)
            item.append(asset_pipelineState)
            item.append(version)
            item.append(file_type)
            item.append(file_location)

            print (item)

    except Error as (e):
        print(str(e) + ": was the error or could not connect to Database")



if __name__ == '__main__':
    main()



