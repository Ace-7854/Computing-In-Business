import oracledb

class database_manager:
    def __init__(self, conn_string):
        self.c_string = conn_string