#!/usr/bin/python3
"""Defines a method to get states"""

import MySQLdb
import re

def getAllStates(username, password, dbname, sp):
    """Defines a method to get states"""
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password,
            db=dbname, charset="utf8"
        )
    cur = conn.cursor()
    query = (
        "SELECT * FROM states WHERE name='{}'".format(sp)
    )
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    import sys
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    search_param = args[4]
    pattern = r"[a-zA-Z]*"
    result = re.match(pattern, search_param)
    if result:
        getAllStates(username, password, dbname, search_param)
