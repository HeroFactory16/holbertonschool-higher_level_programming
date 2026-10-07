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
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        f"JOIN states ON state.name = {sys.argv[4]} "
        "AND cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
