import random
from string import ascii_lowercase, ascii_uppercase, digits
from db_connection import DBConnection

class Tools:
    def generate_random_string(length=8, chars='[LETTERS][NUMBERS]'):
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

    def delete_from_db(id):
        print('Start to delete data from db')
        print('id= ' + str(id))
        sql_delete = 'DELETE FROM PERSON WHERE ID={id}'.format(id=id)
        DBConnection.db_delete(sql_delete)