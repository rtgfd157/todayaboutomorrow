
import sqlite3
import sys
from time import gmtime, strftime
import  os


#sqlite3 Machines_layout.db


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


def select_all_category_recorde_by_category_id(id_category):
    """
       Query tasks by priority
       :param conn: the Connection object
       :param priority:
       :return:
       """
    print("id category",id_category)
    conn = init_db_layout()
    # conn=init_db_layout()
    cur = conn.cursor()
    cur.execute("SELECT * FROM records WHERE id_category=?", (id_category,))

    rows = cur.fetchall()

    conn.commit()
    conn.close()

    # for row in rows:
    #     print(row)

    return rows


def add_record_to_category(layout):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    conn=init_db_layout()

    with conn:



        sql = ''' INSERT INTO records(id_category,name_of_record,destenation_date,archive,show_counter,description,link1,link2,link3 )
                  VALUES(?,?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        # print ("************machine_layout*******")
        # print(layout)
        # print(sql)
        cur.execute(sql, layout)
        return cur.lastrowid




def delete_all_records_by_id_category( id_category):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn=init_db_layout()

    #id=int(id)

    # sql = 'DELETE FROM layout'
    # cur = conn.cursor()
    # print id
    # print sql
    # cur.execute(sql)
    cur = conn.cursor()
    sql = 'DELETE  FROM records WHERE   id_category=? '
    cur = conn.cursor()
    cur.execute(sql, (id_category,))
    conn.commit()
    conn.close()


def delete_record_by_name_of_record_and_id_category(name_of_record, id_category):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn=init_db_layout()

    #id=int(id)

    # sql = 'DELETE FROM layout'
    # cur = conn.cursor()
    # print id
    # print sql
    # cur.execute(sql)
    cur = conn.cursor()
    sql = 'DELETE FROM records WHERE name_of_record=?  and id_category=? '
    cur = conn.cursor()
    cur.execute(sql, (name_of_record,id_category,))
    conn.commit()
    conn.close()

def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE * FROM records'
    cur = conn.cursor()
    cur.execute(sql)




def select_all_machines_layout2():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    conn=init_db_layout()

    cur = conn.cursor()
    cur.execute("SELECT * FROM records")

    rows = cur.fetchall()

    ans=[]


    for row in rows:
        #print(row)

        print("-------------------")
        print (row,row[0])

        dict = {'id_record':row[0],'id_category':row[1],'category':row[2],'name_of_record':row[3] ,'destenation_date':row[4],'archive':row[5],'show_counter':row[6],'description':row[7] }

        #print(  dict['dut_card_nvm'][-20:] )
        ans.append(dict)


    ans = sorted(ans, key=lambda k: k['name_of_record'])




    #print (ans)
    return ans



def select_record_by_id(id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn=init_db_layout()
    #conn=init_db_layout()
    cur = conn.cursor()
    cur.execute("SELECT * FROM records WHERE id_record=?", (id,))
    #print("sdafa")
    rows = cur.fetchall()
    #print("rows  - ",rows)
    conn.commit()
    conn.close()

    # for row in rows:
    #     print(row)

    return rows

def looping_record_by_record_name(name_of_record):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn=init_db_layout()
    #conn=init_db_layout()
    cur = conn.cursor()
    cur.execute("SELECT * FROM records ")
    print("sdafa")
    rows = cur.fetchall()
    for row in rows:
        if row[2]  ==name_of_record:
            print( "-",row[2] ,"=",name_of_record,"-")
        else:
            print( "-",row[2] ,"!=",name_of_record,"-")



    #print("rows  - ",rows)
    conn.commit()
    conn.close()

    # for row in rows:
    #     print(row)

    return rows




# array parameter to function
def update_record( task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """


    conn=init_db_layout()

    sql = ''' UPDATE records
              SET name_of_record = ? ,
                  destenation_date = ? , 
                  archive = ? ,                           
                  show_counter = ? ,
                  description = ? ,
                  link1 = ? ,
                  link2 = ? ,
                  link3 = ?
                                
              WHERE id_record = ? and id_category=?   '''
    cur = conn.cursor()
    cur.execute(sql, task)

    conn.commit()
    conn.close()


def return_id_by_name_of_record( name_of_record):

    conn=init_db_layout()

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM records WHERE name_of_record=?", (name_of_record,))

        rows = cur.fetchall()

        for row in rows:
            print("id:" ,row[0])
            print("for row:" ,row)
            return int(row[0])


def init_db_layout():
    database = "records.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS records (
                                        id_record integer PRIMARY KEY,
                                        id_category integer NOT NULL,
                                        name_of_record text NOT NULL,
                                        destenation_date text,
                                        archive text,
                                        show_counter text,
                                        description text,
                                        link1,
                                        link2,
                                        link3
                                        
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

    conn=init_db_layout()


    print("----print layout---")
    layout = ('ladh1599','cvl','nvm-z43f-22245222','ladh153644','fvl')
    print("------------after------------")





if __name__ == '__main__':
    main()



