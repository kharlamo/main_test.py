from base.connectionbase import ConnectionToServer


class ConnectionMethods:

    def __init__(self):
        self.server = ConnectionToServer().connect_SSH()
        self.connect = ConnectionToServer().connect_DB(self.server)
        self.cursor = self.connect.cursor()

    def cadastr_fields_count(self, conditions: dict):
        cur = self.cursor
        request = "select count(*) from resp2_0_land_field where "
        first = True
        for keys in conditions:
            if first is False:
                request += ' and '
            else:
                first = False
            request += str(keys) + " = "
            value = conditions.get(keys)
            if (type(value) is int) or (type(value) is bool):
                request += str(value) + " "
            elif type(value) is str:
                request += "'" + str(value) + "' "
            else:
                return 2

        cur.execute(request)
        count = cur.fetchall()
        return str(count[0][0])
