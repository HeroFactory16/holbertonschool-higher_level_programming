#!/usr/bin/python3
"""Lists all cities for a given state, sorted by city id."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    stmt = ("SELECT cities.name "
            "FROM cities "
            "JOIN states ON states.name = %s "
            "AND cities.state_id = states.id "
            "ORDER BY cities.id ASC")

    cur.execute(stmt, (sys.argv[4],))

    print(", ".join(row[0] for row in cur.fetchall()))

    cur.close()
    db.close()
