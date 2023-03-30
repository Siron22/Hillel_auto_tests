import allure


# @allure.title('Delete user')
# def test_delete_user(users_ep, unregistered_user_api, auth_ep):
#     login = auth_ep.sign_in(unregistered_user_api.email, unregistered_user_api.password)
#     print('Status code: ', login.status_code)
#     print('Json: ', login.json())
#     import  time
#     time.sleep(2)
#     response = users_ep.delete_user()
#     print('-' * 100)
#     print('Status code: ', response.status_code)
#     print('-'*100)
#     print('Json: ', response.json())

