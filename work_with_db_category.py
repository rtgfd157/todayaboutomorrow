import sqlite3
import sys
from time import gmtime, strftime
import os


# sqlite3 Machines_layout.db


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


def add_category(category_data):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    conn = init_db_layout()

    with conn:
        sql = ''' INSERT INTO categories(category , category_description,pic_link )
                  VALUES(?,?,?) '''
        cur = conn.cursor()
        # print ("************machine_layout*******")
        # print(layout)
        # print(sql)
        cur.execute(sql, category_data)
        return cur.lastrowid


def delete_task(id_category):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn = init_db_layout()

    # id=int(id)

    # sql = 'DELETE FROM layout'
    # cur = conn.cursor()
    # print id
    # print sql
    # cur.execute(sql)
    cur = conn.cursor()
    sql = 'DELETE  FROM categories WHERE id_category=?'
    cur = conn.cursor()
    cur.execute(sql, (id_category,))
    conn.commit()
    conn.close()


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM category'
    cur = conn.cursor()
    cur.execute(sql)



def select_all_categories():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    conn = init_db_layout()

    cur = conn.cursor()
    cur.execute("SELECT * FROM categories")

    rows = cur.fetchall()

    ans = []

    for row in rows:
        # print(row)

        #print("-------------------")
        #print(row, row[0])

        dict = {'id_category': row[0], 'category': row[1], 'category_description': row[2], 'pic_link': row[3],
                }

        # print(  dict['dut_card_nvm'][-20:] )
        ans.append(dict)

    #ans = sorted(ans, key=lambda k: k['category'])

    # print (ans)
    return ans




def return_distinct(command):
    conn = init_db_layout()
    # conn=init_db_layout()
    with conn:
        cur = conn.cursor()
        cur.execute(command)

        rows = cur.fetchall()

        card_type = []

        for row in rows:
            print(row)
            # card_type.append()

        return rows


# array parameter to function
def update_record(task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """

    conn = init_db_layout()
    print("from update db " ,  task)

    sql = ''' UPDATE categories
              SET category = ? ,
                  category_description = ? ,
                  pic_link = ?          
              WHERE id_category = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

    conn.commit()
    conn.close()



def return_category_data_by_id(id_category):
    conn = init_db_layout()

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories WHERE id_category=?", (id_category,))

        rows = cur.fetchall()

        print("$$$$$$$$$$$$$$$$$$$")
        print(rows)

        for row in rows:
            print("id:", row[0])
            print("for row:", row)
            return row

        return -1


def return_id_by_category(category):
    conn = init_db_layout()

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories WHERE category=?", (category,))

        rows = cur.fetchall()

        for row in rows:
            #print("id:", row[0])
            #print("for row:", row)
            return int(row[0])

        return -1


def init_db_layout():
    database = "categories.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS categories (
                                        id_category integer PRIMARY KEY,
                                        category text NOT NULL,
                                        category_description text,
                                        pic_link text
                                     

                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")

    return conn


def main():
    conn = init_db_layout()

    print("----print layout---")
    layout = ('ladh1599', 'cvl', 'nvm-z43f-22245222', 'ladh153644', 'fvl')
    print("------------after------------")


if __name__ == '__main__':
    main()



