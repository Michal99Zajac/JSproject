import sqlite3

class TableDatabase(object):
    """
    class TableDatabase create connection
    to SQLite database and that can create
    tables
    """

    def __init__(self, db_file):
        self.conn = None
        
        #create connection
        try:
            self.conn = sqlite3.connect(db_file)
        except sqlite3.Error:
            print(sqlite3.Error)

    def __str__(self):
        return 'Table Database class'

    def create_tab(self, table_sql):
        """
        function execute sql script for database
        :param table_sql: database file
        """
        try:
            cur = self.conn.cursor()
            cur.execute(table_sql)
        except sqlite3.Error:
            print(sqlite3.Error)

    def get_conn(self):
        """
        :return: connection object
        """
        return self.conn

    def close_conn(self):
        """
        function close connection
        """
        self.conn.close()

    def commit_conn(self):
        """
        function commit transaction
        """
        self.conn.commit()

    def cursor_conn(self):
        """
        :return: cursor connection
        """
        return self.conn.cursor()
