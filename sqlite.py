#!/usr/bin/env python3
import sqlite3
from psycopg2 import sql
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def dump_data():
    database = r"./db/test.sqlite"

    # create a database connection
    conn = create_connection(database)

    # Fetch all UAC data
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM UAC")
        print(cur.fetchall())
    else:
        print("Error! cannot create the database connection.")


def write_account(database, name, hash):

    global sql

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        sql = sql.SQL('''INSERT INTO UAC(name,password_hash) VALUES ({name}, {hash})''').format(name=sql.Identifier(name), hash=sql.Identifier(hash))
        cur = conn.cursor()
        cur.execute(sql.as_string(cur))
        conn.commit()
        return cur.lastrowid
    else:
        print("Error! cannot create the database connection.")


def read_account_pwd(database, name):
    
    global sql

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        sql = sql.SQL('''SELECT hash from UAC where name = {name}''').format(name=sql.Identifier(name))
        cur = conn.cursor()
        cur.execute(sql.as_string(cur))
        return cur.fetchall()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    write_account(r"./db/test.sqlite", 'admin', 'ligm@')
