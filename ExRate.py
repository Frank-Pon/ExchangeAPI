import requests

target = input("請輸入換匯簡寫 ( 例:TWD )：")
url = 'https://open.er-api.com/v6/latest/USD'
headers = {
    'user-agent':'mozilla/5.0'
}
#now = datetime.strftime(%Y / %m / %d - %H : %M : %S)
res = requests.get(url,headers=headers)
#print(res.json())
rates = res.json()['rates'][f'{target}']
update = res.json()['time_last_update_utc']
status = res.json()['result']
#time_last_update_utc
#rates
#result

if status == 'success':
    print(f'USD to {target} 的匯率約為：{rates:.2f} 新台幣')
    print(f'Update time: {update}')
else:
    print(f'API請求失敗,狀態：{status}')