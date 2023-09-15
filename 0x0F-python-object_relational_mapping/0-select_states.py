#!/usr/bin/python3
"""Defines a method to get states"""

import MySQLdb


def getAllStates(user, password, db):
    """Defines a method to get states"""
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=password,
            db="hbtn_0e_0_usa", charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    import sys
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    getAllStates(user, password, db)
