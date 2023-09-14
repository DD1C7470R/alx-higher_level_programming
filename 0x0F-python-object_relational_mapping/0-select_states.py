#!/usr/bin/python3
"""Defines a method to get states"""

import MySQLdb


def getAllStates():
    """Defines a method to get states"""
    conn = MySQLdb.connect(
            host="localhost", port=3306, user="root", passwd="root",
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
    getAllStates()
