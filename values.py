import math

# Выборочное среднее
def sample_mean(series, n):
    ans = 0
    for key in series.keys():
        ans += key * series[key]
    return ans / n

# Выборочная дисперсия
def population_variance(series, sample_mean, n):
    ans = 0
    for key in series.keys():
        ans += (sample_mean - key)**2 * series[key]
    return ans / n

# Исправленная дисперсия
def sample_variance(series, sample_mean, n):
    return (population_variance(series, sample_mean, n)) * n / (n - 1)

# Исправленное СКО
def sample_standard_deviation(sample_variance):
    return math.sqrt(sample_variance)

def mode(series):
    ans = 0
    ans_freq = 0
    for key in series.keys():
        if series[key] > ans_freq:
            ans = key
            ans_freq = series[key]
    return ans