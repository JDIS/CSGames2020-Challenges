from app import db
import sqlite3

# Helper
def execute_query(query):
    try:
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()    
        
        output = dict()
        for i, row in enumerate(rows):
            output[str(i)] = dict(row)

        return output
    except sqlite3.Error as e:
        raise e

def compare_query_output(q1, q2):
    """Compare query outputs. Column order is not important, but row order is."""

    # Row count
    if len(q1) != len(q2): return False

    # Column count, row keys are strings.
    if len(q1["0"]) != len(q2["0"]): return False

    for row in q1:
        for col in q1[row]:
            if col not in q2[row] or q1[row][col] != q2[row][col]: return False

    return True
