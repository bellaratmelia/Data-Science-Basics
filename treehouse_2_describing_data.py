import csv
import numpy

def open_with_csv(filename, d='\t'):
    data_csv = []
    with open(filename, encoding='utf-8') as tsvin:
        tie_reader = csv.reader(tsvin, delimiter=d)
        for row in tie_reader:
            data_csv.append(row)
    return data_csv

FIELDNAMES = ['', 'id', 'price', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'patterned', 'material']
DATATYPES = [('myint', 'i'), ('myId', 'i'), ('price', 'f8'), ('name', 'a200'), ('brandId', '<i8')
            , ('brandName', 'a200'), ('imageUrl', '|S500'), ('desc', '|S900'), ('vendor', '|S100')
            , ('patterned', '|S50'), ('material', '|S50')]

def open_with_numpy(filename, d='\t'):
    data_numpy = numpy.genfromtxt(filename, delimiter=d, skip_header=1, invalid_raise=False, 
                      names=FIELDNAMES, dtype=DATATYPES)
    
    return data_numpy

data_csv = open_with_csv('data.csv')
data_numpy = open_with_numpy('data.csv')
#print(data_numpy[0])
    
def number_of_records(data_sample):
    return len(data_sample) - 1

number_of_ties = number_of_records(data_csv) - 1
#print("{} ties in the records (csv)".format(number_of_ties))

def num_of_records_numpy(data_sample):
    return data_sample.size

number_of_ties_numpy = num_of_records_numpy(data_numpy)
#print("{} ties in the records (numpy)".format(number_of_ties_numpy))

def calculate_sum(sample_data):
    total = 0
    for row in sample_data[1:]:
        total += float(row[2])
    
    return total

#print(calculate_sum(data_csv))

def calc_sum(sample_data):
    prices = [float(row[2]) for row in sample_data[1:]]
    return sum(prices)

#print(calc_sum(data_csv))

def calc_sum_lambda(sample_data):
    prices = list(map(lambda x: float(x[2]), sample_data[1:]))
    return sum(prices)

#print(calc_sum_lambda(data_csv))

def calc_sum_numpy(sample_data):
    prices = [float(x) for x in sample_data]
    return numpy.sum(prices)

#print(calc_sum_numpy(data_numpy['price']))

def find_average(sample_data):
    the_sum = calculate_sum(sample_data)
    size = number_of_records(sample_data)
    return (the_sum / size)

#avg = calc_avg(data_csv)
#print("average = {:03.2f}".format(avg))

def find_max(sample_data, col):
    temp_list = []
    for row in sample_data:
        price = float(row[col])
        temp_list.append(price)

    return max(temp_list)


def find_max_min(sample_data, col, m='max'):
    temp_list = []
    for row in sample_data:
        price = float(row[col])
        temp_list.append(price)

    if m == 'max':
        return max(temp_list)
    else:
        return min(temp_list)


#print(find_max_min(data_csv[1:], 2, 'max'))
#print(find_max_min(data_csv[1:], 2, 'min'))

#numpy way
price = data_numpy['price']
price_float = [float(x) for x in price]
max_numpy = numpy.amax(price_float)
min_numpy = numpy.amin(price_float)
#print("max = {}, min = {}".format(max_numpy, min_numpy))

