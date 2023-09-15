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
        "SELECT c.id, c.name, s.name FROM cities c LEFT JOIN states s ON \
        c.state_id = s.id WHERE c.state_id = s.id ORDER BY c.id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        if row is not None:
            print(row)
    cur.close()
    conn.close()
