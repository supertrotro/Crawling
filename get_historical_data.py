import requests
import json
import csv


url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&limit=1000&&api_key={}'
api_token = 'feb8aee0ec017b35c87b054d1022e2660c5aa1fbc24cee9fd9cd7368ab5564f4'


def get_historical_data(token):
    api_full_path = url.format(token, api_token)
    data = json.loads(requests.get(api_full_path).content)["Data"]
    with open('{}.csv'.format(token), mode='w') as csv_file:
        fieldnames = ['time', 'close', 'high', 'low', 'open', 'volumefrom', 'volumeto']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    for data_item in data:
        print(data_item)
        '''
        Example to write to CSV file
        writer.writerow({'time': data_item['time'],
                         'close': data_item['close'],
                         'high': data_item['high'],
                         'low': data_item['low'],
                         'open': data_item['open'],
                         'volumefrom': data_item['volumefrom'],
                         'volumeto': data_item['volumeto']

                         })
        '''

'''
Example
'''
get_historical_data("BTC")
