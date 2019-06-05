import requests
import json
import csv


historical_api_url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&limit=1000&&api_key={}'
social_api_url = 'https://min-api.cryptocompare.com/data/social/coin/histo/day?coinId={}&aggregate=2&limit=1000&api_key={}'
api_token = 'feb8aee0ec017b35c87b054d1022e2660c5aa1fbc24cee9fd9cd7368ab5564f4'


def get_historical_data(token):
    api_full_path = historical_api_url.format(token, api_token)
    data = json.loads(requests.get(api_full_path).content)["Data"]
    output_file = open('Historical_{}.csv'.format(token), 'w')
    output = csv.writer(output_file)
    output.writerow(data[0].keys())
    for data_row in data:
        output.writerow(data_row.values())
        #print(data_row.values())


def get_social_data(coin_id, token):
    api_full_path = social_api_url.format(coin_id, api_token)
    print(api_full_path)
    data = json.loads(requests.get(api_full_path).content)["Data"]
    output_file = open('Social_{}.csv'.format(token), 'w')
    output = csv.writer(output_file)
    headers =[]
    headers.append('token')
    headers.append(data[0].keys())
    output.writerow(headers)

    for data_row in data:
        data = []
        data.append(token)
        data.append(data_row.values())
        output.writerow(data)
        #print(data_row.values())


def main(file_path):
    print("I'm lazy and I'm proud of it")
    try:
        with open(file_path) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line = line.strip()
                if line:
                    print("Line {}: {}".format(cnt, line.strip()))
                    token, coin_id = line.split(";")
                    print(token)
                    get_historical_data(token)
                    print(coin_id)
                    get_social_data(coin_id)
                line = fp.readline()
                cnt += 1
    finally:
        fp.close()

'''
Example
'''

#main("coin_info.csv")
get_historical_data("BTC")
#get_social_data(1182, "BTC")
