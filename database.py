import sqlite3 as sql


def delete_table(table_name):
    """
    Deletes specified table

    :param table_name: name of the table
    :type table_name: str
    """

    conn = sql.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM {}".format(table_name))
    conn.commit()

    cursor.close()
    conn.close()


def insert_data(table_name, values):
    """
    Inserts data into specified table

    :param table_name: name of the table
    :type table_name: str

    :param values: values inserted
    :type values: list or tuple
    """

    conn = sql.connect("data.db")
    cursor = conn.cursor()

    insertion_string = "({})".format(str(values)[1:-1])
    cursor.execute("INSERT INTO {} VALUES {}".format(table_name, insertion_string))
    conn.commit()

    cursor.close()
    conn.close()


def update_data(table_name, type, values):
    """
    Updates data in the table

    :param table_name: name of the table
    :type table_name: str

    :param type: type of the values updated
    :type type: str

    :param values: a dictionary of pairs COLUMN_NAME : NEW_VALUE
    :type values: dict
    """

    conn = sql.connect("data.db")
    cursor = conn.cursor()

    for item in values.items():
        if type == "str":
            cursor.execute("UPDATE {} SET {} = '{}'".format(table_name, str(item[0]), str(item[1])))
        else:
            cursor.execute("UPDATE {} SET {} = {}".format(table_name, str(item[0]), str(item[1])))

    cursor.close()
    conn.close()


def get_data(table_name, column=None, query=None):
    """
    Makes a data request to the database

    :param table_name: name of the table
    :type table_name: str

    :param column: the name of the column selected. if None or "" , turns to * (all columns)
    :type column: str or None

    :param query: a SQL query-request
    :type query: str or None

    :return: the request result
    :rtype: list
    """

    conn = sql.connect("data.db")
    cursor = conn.cursor()

    if column is None or column == "":
        column = "*"
    if query is None:
        cursor.execute("SELECT {} FROM {}".format(column, table_name))
    else:
        cursor.execute("SELECT {} FROM {} WHERE {}".format(column, table_name, query))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
