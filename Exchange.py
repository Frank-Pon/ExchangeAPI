import requests
'''
使用requests庫
用API的方式將匯率爬下來
並將輸入金額換算成另一種幣別
'''
try:
    target = input("請輸入幣別（例:TWD）：")
    change = float(input("請輸入美金金額："))
    url = 'https://open.er-api.com/v6/latest/USD'
    headers = {
        'user-agent':'mozilla/5.0'
    }

    res = requests.get(url,headers=headers)


    #result
    #time_last_update_utc
    #rates
    rates = res.json()['rates'][f'{target}'] # 匯率金額
    update = res.json()['time_last_update_utc']
    status = res.json()['result']

    change = change * rates

    if status == 'success':
        print(f'匯率計算成功！美金換 {target} 的匯率約為 {rates:.2f}')
        print(f'您此次換匯完的金額約為： {change:.2f} 元 {target}')
        print(f'匯率上次更新時間：{update}')
    else:
        print(f"API請求錯誤,狀態：{status}")
except KeyError:
    print(f'您輸入錯誤的幣別：{target} ,請重新嘗試')
except ValueError:
    print(f'您輸入的金額不是數字,請重新嘗試（可包含小數）')
