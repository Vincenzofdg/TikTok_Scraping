import requests

url = 'https://m.tiktok.com/api/challenge/item_list/?aid=1988&count=30&challengeID=298322&cursor=0&lang=en&verifyFp='
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    user_list = json_data['userList']
    for user in user_list:
        print(user['uniqueId'])
else:
    print('Falha ao fazer solicitação. Código de status:', response.status_code)
