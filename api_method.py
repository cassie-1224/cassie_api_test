import requests



class API:

    def post_api(self, username, password, first_name, last_name, phone_number):
        base_url = 'http://localhost:8083'
        post_data = '{"firstName":"' + first_name + '","lastName":"' + last_name + '","phoneNumber":"' + phone_number + '"}'
        post_url = base_url + "/v1/post-person"
        headers = {'Content-Type': "application/json"}
        print(post_url)
        print(post_data)
        response = requests.post(post_url, auth=(username, password), data=post_data, headers=headers)
        print(response.status_code)
        return  response


    def get_api(self, username, password, persion_id):
        base_url = 'http://localhost:8083'
        get_url = base_url + "/v1/get-person/{personId}".format(personId=persion_id)
        headers = {'Content-Type': "application/json"}
        print(get_url)
        response = requests.get(get_url, auth=(username, password), headers=headers,)
        print(response.status_code)
        print(response.text)
        return response


    def delete_api(self, username, password, persion_id):
        base_url = 'http://localhost:8083'
        delete_url = base_url + "/v1/delete-person/{personId}".format(personId=persion_id)
        headers = {'Content-Type': "application/json"}
        print(delete_url)
        response = requests.delete(delete_url, auth=(username, password), headers=headers,)
        print(response.status_code)
        print(response.text)
        return response
