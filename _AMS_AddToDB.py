import maya.cmds as cmds
import sqlite3
from sqlite3 import Error


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

def create_file(conn, newFile):
    """
    create a new file entry
    :param conn: The connection object
    :param newFile: The file object
    :return:
    """
    print("inside create function: "+str(newFile))
    sql = '''INSERT INTO files(name,asset_description,asset_pipelineState,version,file_type,file_location)
              VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, newFile)
    #bring back the generated id
    return cur.lastrowid

def create_tag(conn, tag):
    """
    create a new tag entry
    :param conn: The connection object
    :param tag: the tag object
    :return:
    """
    sql = '''INSERT INTO tags(name) VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, tag)
    #bring back the id
    return cur.lastrowid

def create_fileTag(conn, newFileTag):
    """
    create a new file tag association
    :param conn:
    :param newFileTag:
    :return:
    """
    sql = '''INSERT INTO fileTags(files_id,tags_id) VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql,newFileTag)
    #bring back the generated id?
    return cur.lastrowid


#def main():
    #database = "C:\\Users\MAE\Documents\MayaPython\AMS\AssetManagementSystem.db"
    #database = "D:\\Student Data\Documents\AMS\AssetManagementSystem.db"

    # create a database connection
    #conn = create_connection(database)
    #with conn:
        #create a new file
        #newFile = ('EDA','character','modeling','v06','.ma','C:\\Users\MAE\Desktop\EDA_Char_modeling_v06.ma')
        #file_id = create_file(conn, newFile)
        #print("added: " + str(file_id))

        #create a new tag
        #newTag = ('helloWorld',)
        #tag_id = create_tag(conn, newTag)
        #print("Added: " + str(tag_id))

        #create association between tag and file
        #newFileTag = (file_id, tag_id)
        #newFileTag_id = create_fileTag(conn, newFileTag)
        #print("added: " + str(newFileTag_id))

if __name__ == '__main__':
    main()



