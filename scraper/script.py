from pprint import pprint
from pandas import DataFrame
import csv
import requests
from bs4 import BeautifulSoup


def get_table_heading(table):

    heading = list()
    thead = table.find('thead').find('tr').find_all('th')[1:7]
    for th in thead:
        heading.append(th.text)

    return heading


def extract_crypto_data(table):

    crypto_list = list()
    tbody = table.find('tbody').find_all('tr')
    for tr in tbody:
        tds = tr.find_all('td')[1:7]

        crypto_list.append((
            tds[0].text,
            tds[1].find('span').text,
            tds[2].find('div').text,
            tds[3].text,
            tds[4].text,
            tds[5].text,))

    return crypto_list


if __name__ == '__main__':
    url = 'https://crypto.com/price'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    heading = get_table_heading(table)
    crypto_data = extract_crypto_data(table)

    csv_filename = 'crypto_data.csv'
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.reader(file)
            existing_header = next(reader)
    except FileNotFoundError:
        existing_header = None

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if existing_header is None:
            writer.writerow(heading)

        writer.writerows(crypto_data)
