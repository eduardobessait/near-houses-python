import mysql.connector


class Database:
    port = 3306
    host = "urbiwise.c99cwbn4v1fu.eu-west-3.rds.amazonaws.com"
    username = "urbiwise_db"
    password = "8cKPDKkYZBqEhv6W"
    database = "urbiwise"
    connection = ""
    cursor = ""
    table = ""
    query = ""

    # Initialize
    def __init__(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.username, passwd=self.password)
        self.cursor = self.connection.cursor()

    # Show databases
    def show(self):
        self.cursor.execute("show databases")

        for database in self.cursor:
            print(database)

    def table(self, table):
        self.table = table

    def select(self, columns):
        self.query = "SELECT {} FROM `{}`.`{}`".format(columns, self.database, self.table)
        self.cursor.execute("SELECT count(*) FROM urbiwise.users".format(self.database, self.table))

        for user in self.cursor:
            print(user[0])

    def count(self):
        rows = self.cursor.execute("SELECT count(*) FROM urbiwise.users".format(self.database, self.table))
        print(rows)


database = Database()

database.table("users")
database.select("*")
