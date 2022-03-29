from clickhouse_driver import Client


class CKClient:
    def __init__(self):
        self.username = "default"
        self.passwd = "click!@#123"
        self.client = Client(host="localhost", port="3306", user=self.username, password=self.passwd)

    def show_databases(self):
        return self.client.execute("show databases;")

    def create_db(self, db_name, db_fields_map):
        pass

    def insert_table(self, table_name):
        pass


if __name__ == '__main__':
    client = CKClient()
    result = client.show_databases()
    print(result)
