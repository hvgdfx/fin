from clickhouse_driver import Client


class CKClient:
    def __init__(self):
        self.username = "default"
        self.passwd = "click!@#123"

        self.client = Client(host="120.132.33.146", port="9000", user=self.username, password=self.passwd)

    def show_databases(self):
        return self.client.execute("show databases;")

    def create_db(self, db_name):
        pass

    def insert_table(self, table_name):
        pass


client = CKClient()

if __name__ == '__main__':
    client = CKClient()
    result = client.show_databases()
    print(result)
