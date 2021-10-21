import psycopg2
from queries import drop_tables_list, create_tables_list

def create_db():
    """
    Connects to a local postgres server and creates a database 'awsome-db'

    Returns:
        cur: cursor object
        conn: connection to new database
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS awesome-db")
    cur.execute("CREATE DATABASE awesome-db")
    conn.close()

    conn = psycopg2.connect("host=127.0.0.1 dbname=awesome-db user=student password=student")
    cur = conn.cursor()
    return cur, conn


def drop_tables(cur, conn):
    """
    Executes queries in drop_tables_list to drop tables in database of conn.

    Args:
        cur: cursor object
        conn: connection to database
    """
    for query in drop_tables_list:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates tables in database conn with queries in create_tables_list.

    Args:
        cur: cursor object
        conn: connection to database
    """
    for query in create_tables_list:
        cur.execute(query)
        conn.commit()


def main():
    """
    Creates new database awesome_db with necessary tables and closes connection at the end.
    """
    cur, conn = create_db()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
