import jaydebeapi

class DBConnection:
    def db_select(sql):
        driver = "org.h2.Driver"
        url = "jdbc:h2:tcp://localhost:8091/mem:personDB"

        username = "testDBUsername"
        password = "testDBPassword"
        jar = "D:/DFY/cassie_test/h2-1.4.200.jar"
        conn = jaydebeapi.connect(driver, url, [username, password], jar)
        curs = conn.cursor()
        print("pass")

        try:
            curs.execute(sql)
            result = curs.fetchall()
            print(result)
            return result
        finally:
            curs.close()
            conn.close()

    def db_delete(sql):
        driver = "org.h2.Driver"
        url = "jdbc:h2:tcp://localhost:8091/mem:personDB"

        username = "testDBUsername"
        password = "testDBPassword"
        jar = "D:/DFY/cassie_test/h2-1.4.200.jar"
        conn = jaydebeapi.connect(driver, url, [username, password], jar)
        curs = conn.cursor()
        print("pass")

        try:
            curs.execute(sql)
        finally:
            curs.close()
            conn.close()

