from api_method import API
from db_connection import DBConnection
from tools import Tools

class TestHttpMethod:

    def setup_class(self):
        print("Insert data into database...")
        # precondition: post data into database first
        first_name = Tools.generate_random_string(5) + '_cassie'
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '1234567890')
        assert response.status_code == 201

    def test_http_delete_with_valid_id(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.delete_api(self,'admin', 'testPassword', id)
        assert response.status_code == 200
        #verify the data should not existing in database after HTTP delete
        sql = "SELECT * FROM PERSON WHERE ID={id}".format(id=id)
        sql_result = DBConnection.db_select(sql)
        assert sql_result[0] is None
        Tools.delete_from_db(id)

    def test_http_delete_with_id_special_character(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.delete_api(self,'admin', 'testPassword', '@!11')
        assert response.status_code != 200
        #verify the data should not existing in database after HTTP delete
        sql = "SELECT * FROM PERSON WHERE ID={id}".format(id=id)
        sql_result = DBConnection.db_select(sql)
        assert sql_result[0] is not None
        Tools.delete_from_db(id)

    def test_http_delete_with_id_empty(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.delete_api(self,'admin', 'testPassword', '')
        assert response.status_code != 200
        #verify the data should not existing in database after HTTP delete
        sql = "SELECT * FROM PERSON WHERE ID={id}".format(id=id)
        sql_result = DBConnection.db_select(sql)
        assert sql_result[0] is not None
        Tools.delete_from_db(id)

    def test_http_delete_with_id_not_existing(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.delete_api(self,'admin', 'testPassword', '9999')
        assert response.status_code != 200
        #verify the data should not existing in database after HTTP delete
        sql = "SELECT * FROM PERSON WHERE ID={id}".format(id=id)
        sql_result = DBConnection.db_select(sql)
        assert sql_result[0] is not None
        Tools.delete_from_db(id)