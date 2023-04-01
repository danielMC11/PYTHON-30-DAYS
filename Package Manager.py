import re

import requests
from MY_PACKAGE import extract_words as ew
import json
"""
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response)     # return object with status_code
print(response.status_code) # value of the status code ej 404
print(response.headers, end='\n\n\n')  #header types

words = ew.unique_words(response.text)
print(len(words))
"""

url = "https://api.thecatapi.com/v1/breeds"
response = requests.get(url)

from functools import reduce
from statistics import mean, median, stdev
import csv


def extract_numbers(str_numbers):
    pattern = r'\d+'
    lst_numbers = re.findall(pattern, str_numbers)
    sum_result = reduce(lambda x, y: int(x) + int(y), lst_numbers)
    mean_result = sum_result / len(lst_numbers)
    return mean_result


def print_statistics(lst_numbers):
    minimum_w = min(lst_numbers)
    maximum_w = max(lst_numbers)
    mean_w = mean(lst_numbers)
    median_w = median(lst_numbers)
    stand_dev = stdev(lst_numbers)
    print(f'Min: {minimum_w}, Max: {maximum_w}, Mean: {mean_w:.2f}, Median: {median_w}, Standard Deviation: {stand_dev:.2f}')


def breeds_per_country(list_dicts):
    lst_countries = list()
    lst_countries_number = list()
    for dicts in list_dicts:
        if dicts['origin'] not in lst_countries:
            lst_countries.append(dicts['origin'])
            lst_countries_number.append(1)
        else:
            index = lst_countries.index(dicts['origin'])
            lst_countries_number[index] += 1
    sum_of_numbers = reduce(lambda x, y: x + y, lst_countries_number)
    lst_table = [[country,
                  number,
                  reduce(lambda x, y: x + y, lst_countries_number[:lst_countries.index(country)+1]),
                  round(number/sum_of_numbers, 2),
                  round((number/sum_of_numbers) * 100, 2)]
                 for country, number in zip(lst_countries, lst_countries_number)]

    return lst_table


with open('cat_zero.json', mode='w') as f:      # From url, json str
    #list_dicts = json.loads(response.text)     # converting json str (response txt) to list_dicts
    list_dicts_v2 = response.json()             # converting response json to list_dicts
    json.dump(list_dicts_v2, f, indent=4)

with open('cat_zero.json', mode='r') as f:
    list_cats_dicts = json.loads(f.read())
    weights = [extract_numbers(dicts['weight']['metric']) for dicts in list_cats_dicts]
    print_statistics(weights)
    lifespans = [extract_numbers(dicts['life_span']) for dicts in list_cats_dicts]
    print_statistics(lifespans)
    list_of_lists_table = breeds_per_country(list_cats_dicts)

with open('cats_frequency_table.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    header = ['Country', 'Abs Frequency', 'Abs Frequency Acc', 'Rel Frequency', 'Percentage']
    writer.writerow(header)
    writer.writerows(list_of_lists_table)
    sum_abs_freq = 0
    sum_rel_freq = 0
    sum_percent = 0
    for i in list_of_lists_table:
        sum_abs_freq += i[1]
        sum_rel_freq += i[3]
        sum_percent += i[4]
    total_row = ['', round(sum_abs_freq, 2), '', round(sum_rel_freq, 2), round(sum_percent, 2)]
    writer.writerow(total_row)

