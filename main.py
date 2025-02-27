import re
import codecs
import graphs

def get_russian_words_len(text):
    return list(map(len, re.findall(r'[а-яА-ЯёЁ]+-*[а-яА-ЯёЁ]*', text)))

def get_russian_words(text):
    return re.findall(r'[а-яА-ЯёЁ]+-*[а-яА-ЯёЁ]*', text)

def get_variation_series(words_len):
    series = dict()
    for word_len in words_len:
        series[word_len] = series.get(word_len, 0) + 1
    return series

try:
    fileObj  = codecs.open( "text.txt", "r", "utf_8_sig" )
    text = fileObj.read()
    series = get_variation_series(get_russian_words_len(text))
    histogram = graphs.histogram(series)
    polygon = graphs.polygon(series)
    function_distribution = graphs.function_distribution(series)
except Exception as e:
    print(e)
