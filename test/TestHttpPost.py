import json as simplejson
from collections import OrderedDict
from api_method import API
from db_connection import DBConnection
from tools import Tools


class TestHttpMethod:

    def test_http_post_with_valid_data(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        sql = "SELECT * FROM PERSON "
        #get the db result before post data
        sql_result =DBConnection.db_select(sql)
        original_lenth = len(sql_result)
        print('original_lenth: ' + str(original_lenth))
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '1234567890')
        assert response.status_code == 201
        sql_result = DBConnection.db_select(sql)
        result_lenth = len(sql_result)
        print('result_lenth: ' + str(result_lenth))
        assert result_lenth == original_lenth+1
        sql_first_name = sql_result[len(sql_result)-1][1]
        sql_last_name = sql_result[len(sql_result) - 1][2]
        sql_phone_number = sql_result[len(sql_result) - 1][3]
        assert sql_first_name == first_name
        assert sql_last_name == 'dong'
        assert sql_phone_number == '1234567890'
        #delete the data you insert into database after test finished
        id = sql_result[len(sql_result)-1][0]
        print('id= ' + str(id))
        Tools.delete_from_db(id)

    def test_http_post_with_first_name_special_character(self):
        print("start to run...")
        first_name = '123REW%$&'
        sql = "SELECT * FROM PERSON "
        #get the db result before post data
        sql_result =DBConnection.db_select(sql)
        original_lenth = len(sql_result)
        print('original_lenth: ' + str(original_lenth))
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '1234567890')
        assert response.status_code == 201
        sql_result = DBConnection.db_select(sql)
        result_lenth = len(sql_result)
        print('result_lenth: ' + str(result_lenth))
        assert result_lenth == original_lenth+1
        sql_first_name = sql_result[len(sql_result)-1][1]
        sql_last_name = sql_result[len(sql_result) - 1][2]
        sql_phone_number = sql_result[len(sql_result) - 1][3]
        assert sql_first_name == first_name
        assert sql_last_name == 'dong'
        assert sql_phone_number == '1234567890'
        # delete the data you insert into database after test finished
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        Tools.delete_from_db(id)

    def test_http_post_with_empty_first_name(self):
        print("start to run...")
        first_name = ''
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '1234567890')
        assert response.status_code != 201
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        assert response_json[0] == "JSON Error: firstName 不能为空"

    def test_http_post_with_last_name_special_character(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        sql = "SELECT * FROM PERSON "
        #get the db result before post data
        sql_result =DBConnection.db_select(sql)
        original_lenth = len(sql_result)
        print('original_lenth: ' + str(original_lenth))
        response = API.post_api(self, 'admin', 'testPassword', first_name, '#@$!~&*', '1234567890')
        assert response.status_code == 201
        sql_result = DBConnection.db_select(sql)
        result_lenth = len(sql_result)
        print('result_lenth: ' + str(result_lenth))
        assert result_lenth == original_lenth+1
        sql_first_name = sql_result[len(sql_result)-1][1]
        sql_last_name = sql_result[len(sql_result) - 1][2]
        sql_phone_number = sql_result[len(sql_result) - 1][3]
        assert sql_first_name == first_name
        assert sql_last_name == '#@$!~&*'
        assert sql_phone_number == '1234567890'
        # delete the data you insert into database after test finished
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        Tools.delete_from_db(id)

    def test_http_post_with_empty_last_name(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_select(sql)
        original_lenth = len(sql_result)
        print('original_lenth: ' + str(original_lenth))
        response = API.post_api(self, 'admin', 'testPassword', first_name, '', '1234567890')
        assert response.status_code == 201
        sql_result = DBConnection.db_select(sql)
        result_lenth = len(sql_result)
        print('result_lenth: ' + str(result_lenth))
        assert result_lenth == original_lenth + 1
        sql_first_name = sql_result[len(sql_result) - 1][1]
        sql_last_name = sql_result[len(sql_result) - 1][2]
        sql_phone_number = sql_result[len(sql_result) - 1][3]
        assert sql_first_name == first_name
        assert sql_last_name == ''
        assert sql_phone_number == '1234567890'
        # delete the data you insert into database after test finished
        id = sql_result[len(sql_result) - 1][0]
        print('id= ' + str(id))
        Tools.delete_from_db(id)

    def test_http_post_with_phone_number_special_character(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '$#@!123')
        assert response.status_code != 201
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        assert response_json[0] == "JSON Error: phoneNumber phoneNumber must be 10 digits."

    def test_http_post_with_phone_number_less_than_10(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '123')
        assert response.status_code != 201
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        assert response_json[0] == "JSON Error: phoneNumber phoneNumber must be 10 digits."

    def test_http_post_with_phone_number_more_than_10(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '12345678900')
        assert response.status_code != 201
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        assert response_json[0] == "JSON Error: phoneNumber phoneNumber must be 10 digits."

    def test_http_post_with_phone_number_empty(self):
        print("start to run...")
        first_name = Tools.generate_random_string(5) + '_cassie'
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '')
        assert response.status_code != 201
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        assert response_json[0] == "JSON Error: phoneNumber phoneNumber must be 10 digits."
