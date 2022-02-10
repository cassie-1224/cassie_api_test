import random
import pytest
import json as simplejson
from collections import OrderedDict
from string import ascii_lowercase, ascii_uppercase, digits
from api_method import API
from db_connection import DBConnection


class TestHttpMethod:

    def test_http_post(self):
        print("start to run...")
        first_name = self.generate_random_string(5) + '_cassie'
        sql = "SELECT * FROM PERSON "
        #get the db result before post data
        sql_result =DBConnection.db_action(sql)
        original_lenth = len(sql_result)
        print('original_lenth: ' + str(original_lenth))
        response = API.post_api(self, 'admin', 'testPassword', first_name, 'dong', '1234567890')
        assert response.status_code == 201
        sql_result = DBConnection.db_action(sql)
        result_lenth = len(sql_result)
        print('result_lenth: ' + str(result_lenth))
        #verify if fisrt name in database is inserted correctly
        assert result_lenth == original_lenth+1
        sql_first_name = sql_result[len(sql_result)-1][1]
        assert sql_first_name == first_name


    def test_http_get(self):
        print("start to run...")
        response = API.get_api(self, 'admin', 'testPassword', 2)
        assert response.status_code == 200
        sql = "SELECT * FROM PERSON WHERE ID=2"
        sql_result = DBConnection.db_action(sql)
        response_json = simplejson.loads(response.text, object_pairs_hook=OrderedDict)
        #compare the HTTP GET result with sql result
        assert response_json['id'] == sql_result[0][0]
        assert response_json['firstName'] == sql_result[0][1]
        assert response_json['lastName'] == sql_result[0][2]
        assert response_json['phoneNumber'] == sql_result[0][3]


    def test_http_delete(self):
        print("start to run...")
        sql = "SELECT * FROM PERSON "
        # get the db result before post data
        sql_result = DBConnection.db_action(sql)
        original_lenth = len(sql_result)
        print('original_lenth: ' + str(original_lenth))
        id_list = []
        for i in sql_result:
            id_list.append(i[0])
        print(id_list)
        #get a random id that existing in database, then delete it
        id = random.choice(id_list)
        response = API.delete_api(self,'admin', 'testPassword', id)
        #verify the data should not existing in database after HTTP delete
        sql = "SELECT * FROM PERSON WHERE ID={id}".format(id=id)
        sql_result = DBConnection.db_action(sql)
        assert response.status_code == 200
        assert sql_result[0] == None


    def generate_random_string(self, length=8, chars='[LETTERS][NUMBERS]'):
        """Generates a string with a desired ``length`` from the given ``chars``.

        The population sequence ``chars`` contains the characters to use
        when generating the random string. It can contain any
        characters, and it is possible to use special markers
        explained in the table below:

        |  = Marker =   |               = Explanation =                   |
        | ``[LOWER]``   | Lowercase ASCII characters from ``a`` to ``z``. |
        | ``[UPPER]``   | Uppercase ASCII characters from ``A`` to ``Z``. |
        | ``[LETTERS]`` | Lowercase and uppercase ASCII characters.       |
        | ``[NUMBERS]`` | Numbers from 0 to 9.                            |

        Examples:
        | ${ret} = | Generate Random String |
        | ${low} = | Generate Random String | 12 | [LOWER]         |
        | ${bin} = | Generate Random String | 8  | 01              |
        | ${hex} = | Generate Random String | 4  | [NUMBERS]abcdef |
        """
        if length == '':
            length = 8
        # length = self._convert_to_integer(length, 'length')
        for name, value in [('[LOWER]', ascii_lowercase),
                            ('[UPPER]', ascii_uppercase),
                            ('[LETTERS]', ascii_lowercase + ascii_uppercase),
                            ('[NUMBERS]', digits)]:
            chars = chars.replace(name, value)
        maxi = len(chars) - 1
        return ''.join(chars[random.randint(0, maxi)] for _ in range(length))

