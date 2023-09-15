#!/usr/bin/python3
"""Defines a method to get states"""

import MySQLdb
from sys import argv
import re

if __name__ == '__main__':
    """Defines a method to get states"""
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], charset="utf8"
        )
    cur = conn.cursor()
    pattern = "[!@£$%^&*'\"]"
    result = re.search(pattern, argv[4])
    if result is not None and result.group():
        pass
    else:
        cur.execute(
            "SELECT c.id, c.name FROM cities c LEFT JOIN states s ON \
            c.state_id = s.id WHERE c.state_id = s.id AND s.name LIKE \
            BINARY '{}' ORDER BY c.id ASC".format(argv[4]).strip("'")
        )
        query_rows = cur.fetchall()
        myset = set()
        for row in query_rows:
            myset.add(row[1])
        print(", ".join(myset))
    cur.close()
    conn.close()
