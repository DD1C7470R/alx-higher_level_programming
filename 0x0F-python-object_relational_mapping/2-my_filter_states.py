#!/usr/bin/python3
"""Defines a method to get states"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Defines a method to get states"""
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"
        .format(argv[4]).strip("'")
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        if row is not None:
            print(row)
    cur.close()
    conn.close()
