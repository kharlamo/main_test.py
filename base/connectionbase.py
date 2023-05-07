import sys
import psycopg2
from sshtunnel import SSHTunnelForwarder
from base.dataconfing import Config


class ConnectionToServer(Config):

    def connect_SSH(self):
        # Подключаемся к серверу
        try:
            server = SSHTunnelForwarder(
                self.SERVER_SSH_HOST,
                int(self.SERVER_SSH_PORT),
                ssh_username=self.SERVER_SSH_USER,
                ssh_password=self.SERVER_SSH_PASSWORD,
                remote_bind_address=('localhost', 5432),
                local_bind_address=('localhost', 22)
            )

            server.start()
            print("Подключились к серверу")

        except EOFError as e:
            print(e)
            print("Не удалось подключиться к серверу")
            sys.exit()

        return server


    def connect_DB(self,server):
        # Подключаемся к БД

        try:
            conn = psycopg2.connect(dbname=self.SERVER_DATABASE_NAME,
                                    user=self.SERVER_DATABASE_USER,
                                    password=self.SERVER_DATABASE_PASSWORD,
                                    host=server.local_bind_host,
                                    port=server.local_bind_port)
            # Проверка на работоспособность запросов в БД
            cur = conn.cursor()
            cur.execute("select * from organization_ limit 1")
            count = cur.fetchall()
            print("Обращение к БД успешно")

        except EOFError as e:
            print(e)
            print("Не удалось подключиться к БД")
            server.stop()
            sys.exit()

        return conn
