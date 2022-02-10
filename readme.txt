1. I'm using pytest to test the api.
2. Using pycharm to setup the project.
3. There is "Windows fatal exception: access violation" when I running the program, but not blocking the program execution. The exception is caused by my computer system windows 10,
I can't change the system so we can ignore the exception.
4. You should run the test method under TestHttpMethod.py, select the test method, such as test_http_post, then right click, then run by pytest.
5. Delete api is not working well, although it can be executed and gets 200 response, but in the database, the data is still existing. so def test_http_delete(self) failed in last step.
I think this is a API bug.