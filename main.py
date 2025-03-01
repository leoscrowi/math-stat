import collections
import math
import re
import codecs
import graphs
import values
from values import sample_standard_deviation


def get_russian_words_len(text):
    return list(map(len, get_russian_words(text)))

def get_russian_words(text):
    return re.findall(r'[а-яА-ЯёЁ]+-*[а-яА-ЯёЁ]*', text)[0:200]

def get_variation_series(data_path):
    try:
        fileObj  = codecs.open(data_path, "r", "utf_8_sig" )
        text = fileObj.read()
        words_len = get_russian_words_len(text)
        series = dict()
        for word_len in words_len:
            series[word_len] = series.get(word_len, 0) + 1
        return series
    except Exception as e:
        print(e)

# 13
def parse_data(data_path, column):
    try:
        fileObj = codecs.open(data_path, 'r', encoding='utf-8')
        text = fileObj.read()
        matrix = list(map(float, [i.strip() for i in text.split()]))
        values = [matrix[i] for i in range(len(matrix)) if i % 13 == column]
        fileObj.close()
        bins = collections.defaultdict(list)

        for v in values:
            interval = math.floor(v)
            bins[interval].append(v)

        series = {sum(v_list) / len(v_list): len(v_list) for v_list in bins.values() if v_list}

        return series
    except Exception as e:
        print(e)

def show_info(series):
    n = sum(series.values())
    print(series)
    histogram = graphs.histogram(series)
    polygon = graphs.polygon(series)
    function_distribution = graphs.function_distribution(series)

    sample_mean = values.sample_mean(series, n)
    population_variance = values.population_variance(series, sample_mean, n)
    sample_variance = values.sample_variance(series, sample_mean, n)
    print(f"Выборочное среднее: {sample_mean}")
    print(f"Выборочная дисперсия: {population_variance}", )
    print(f"Исправленная дисперсия: {sample_variance}")
    print(f"Исправленное СКО: {sample_standard_deviation(sample_variance)}")
    print(f"Мода: {values.mode(series)} ")
    
    print("Итервалы ", len(series))



series1 = get_variation_series('text.txt')
show_info(series1)

# Выборка температур взята с 1825-2024 год (т.к. не все 2025 есть)
# индексация колонок идет с 0
series2 = parse_data('data', 0)
show_info(series2)
