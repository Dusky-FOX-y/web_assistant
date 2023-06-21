import pypyodbc as sql
# from data.config import database_name as name
from datetime import datetime
name = 'DRIVER={SQL Server};' 'Server=localhost\SQLEXPRESS;' 'Database=Sheduler;' 'Trusted_Connection=Yes;'


class DB:

    def __init__(self, ):
        try:

            self.con = sql.connect(name)

        except Exception as e:

            self.database_log(f"Failed to connect to {name}", e)
            self.cur.close()
            self.con.close()
            return

        else:

            self.cur = self.con.cursor()

    def find(self, **kwargs):
        """Accepts
        Table name : table          || STR
        Column names : columns      || STR
        Parameters WHERE: where     || STR
        Many: fetchall/fetchone     || Bool"""
        table = ""
        columns = ""
        where = ""
        many = False

        if "table" in kwargs:
            table = kwargs["table"]

        if "columns" in kwargs:
            columns = kwargs["columns"]
        else:
            columns = "*"

        if "where" in kwargs:
            where = "WHERE " + kwargs["where"]

        if "many" in kwargs:
            many = kwargs["many"]

        self.cur.execute(f"SELECT {columns} FROM {table} {where}")

        if many:
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()

        if data is None:
            pass
        else:
            if len(data) != 0:
                return data

        return False

    def insert(self, **kwargs):
        """Inserting function
        Table name : table|| STR
        Inserting data  : data || list """
        table = ""
        data = ()
        que = "(?"

        if "table" in kwargs:
            table = kwargs["table"]

        # Question marks for sql query
        if "data" in kwargs:
            data = kwargs["data"]
            i = len(data) - 1
            for j in range(i):
                que += ", ?"
            que += ")"
        self.cur.execute(f"INSERT INTO {table} VALUES {que}", data)
        self.con.commit()

    def delete(self, **kwargs):
        """deleting function
        Table name : table      || STR
        Parameters WHERE: where || STR"""
        table = ""
        where = ""
        if "table" in kwargs:
            table = kwargs["table"]

        if "where" in kwargs:
            where = kwargs["where"]

        self.cur.execute(f"DELETE FROM {table} WHERE {where}")
        self.con.commit()

    def update(self, **kwargs):
        """Updating function
        Table name : table                  || STR
        Updating columns : column           || STR
        Parameters WHERE: where             || STR
        Inserting value : new_value         || STR"""

        table = ""
        column = ""
        where = ""
        new_value = ""

        if "table" in kwargs:
            table = kwargs["table"]

        if "column" in kwargs:
            column = kwargs["column"]

        if "where" in kwargs:
            where = kwargs["where"]

        if "new_value" in kwargs:
            new_value = kwargs["new_value"]

        self.cur.execute(f"UPDATE {table} SET {column} = '{new_value}' WHERE {where}")

        self.con.commit()

if __name__ == "__main__":
    asd = DB()
    asd.delete(table="users", where="tid = '481207625'")
