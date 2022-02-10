import json as simplejson
from collections import OrderedDict
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

    def test_http_get_valid_id(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.get_api(self, 'admin', 'testPassword', id)
        assert response.status_code == 200
        sql = "SELECT * FROM PERSON WHERE ID={id}".format(id=id)
        sql_result = DBConnection.db_select(sql)
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        #compare the HTTP GET result with sql result
        assert response_json['id'] == sql_result[0][0]
        assert response_json['firstName'] == sql_result[0][1]
        assert response_json['lastName'] == sql_result[0][2]
        assert response_json['phoneNumber'] == sql_result[0][3]
        # delete the data you insert into database after test finished
        Tools.delete_from_db(id)

    def test_http_get_with_id_empty(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON"
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.get_api(self, 'admin', 'testPassword', '')
        assert response.status_code != 200
        # delete the data you insert into database after test finished
        Tools.delete_from_db(id)

    def test_http_get_with_id_special_character(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON"
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.get_api(self, 'admin', 'testPassword', '#$')
        assert response.status_code != 200
        # delete the data you insert into database after test finished
        Tools.delete_from_db(id)

    def test_http_get_with_id_not_existing(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON"
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        response = API.get_api(self, 'admin', 'testPassword', '99999')
        assert response.status_code != 200
        # delete the data you insert into database after test finished
        Tools.delete_from_db(id)