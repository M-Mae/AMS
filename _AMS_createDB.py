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


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("created Database")
    except Error as e:
        print(e)

def main():
    #database = "C:\\Users\MAE\Documents\MayaPython\AMS\AssetManagementSystem.db"
    database = "D:\\Student Data\Documents\AMS\AssetManagementSystem.db"

    sql_create_files_table = """CREATE TABLE IF NOT EXISTS files(
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            asset_description text,
                                            asset_pipelineState text,
                                            version text,
                                            file_type text,
                                            file_location text
                                        );"""
    sql_create_tags_table = """CREATE TABLE IF NOT EXISTS tags(
                                                id integer PRIMARY KEY,
                                                name text NOT NULL
                                            );"""
    sql_create_fileTags_table = """CREATE TABLE IF NOT EXISTS fileTags(
                                            files_id NOT NULL, 
                                            tags_id NOT NULL,
                                            FOREIGN KEY (files_id) REFERENCES files(id)
                                            FOREIGN KEY (tags_id) REFERENCES tags(id)
                                            );"""
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_files_table)
        # create tasks table
        create_table(conn, sql_create_tags_table)
        #create fileTag table
        create_table(conn, sql_create_fileTags_table)
    else:
        print("Error! Cannot create the database connection!")


if __name__ == '__main__':
    main()



