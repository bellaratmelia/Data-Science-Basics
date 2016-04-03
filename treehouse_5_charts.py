from treehouse_4_exporting_data import *

import matplotlib.pyplot as plt 

def create_line_chart(sample_data, title, img_export_filename):
	fig = plt.figure() 	#new image object
	axis = fig.add_subplot(1, 1, 1) #axis object

	prices = sorted(map(float, sample_data))

	x_axis_ticks = list(range(len(sample_data)))
	axis.plot(x_axis_ticks, prices, linewidth=2) #draw the line chart

	axis.set_title(title)
	axis.set_xlim(0, len(sample_data))
	axis.set_xlabel("The Price($)")
	axis.set_ylabel("Number of Ties")

	fig.savefig(img_export_filename)


#create_line_chart([x[2] for x in kiton_ties[1:]], "Price Distribution of Kiton Ties", 's5_line_chart_kiton.png')

def plot_bar_chart(prices_in_float, img_export_filename):
	prices = list(map(int, prices_in_float))
	x = numpy.arange(len(prices))
	width = 0.25
	plt.bar(x+width, prices, width)
	plt.xlim([0, 5055])
	plt.savefig(img_export_filename)

#plot_bar_chart([float(x[2]) for x in data_csv[1:]], "s5_bar_chart_ungrouped.png")


def create_bar_chart(price_groups, exported_figure_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.style.use('ggplot')
    colors=plt.rcParams['axes.color_cycle']
     
    for group in price_groups:
        ax.bar(group, price_groups[group], color=colors[group%len(price_groups)])

    labels = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"]
    ax.legend(labels)

    ax.set_title('Amount of Ties at price points')
    ax.set_xlabel('Tie Price ($)')
    ax.set_xticklabels(labels, ha='left')
    ax.set_xticks( range(1, len(price_groups)+1) )
    ax.set_ylabel('Number of Ties')

    plt.grid(True)
    fig.savefig(exported_figure_filename)


from collections import Counter
def group_prices_by_range(prices_in_float):
    
    tally = Counter()

    for item in prices_in_float:
        bucket = 0
        rounded_price = round(item, -1)
        if rounded_price >= 0 and rounded_price <= 50:
            bucket = 1
        elif rounded_price >= 50 and rounded_price <= 100:
            bucket = 2
        elif rounded_price >= 100 and rounded_price <= 150:
            bucket = 3
        elif rounded_price >= 150 and rounded_price <= 200:
            bucket = 4
        elif rounded_price >= 200 and rounded_price <= 250:
            bucket = 5
        elif rounded_price >= 250:
            bucket = 6
        else:
            bucket = 7

        tally[bucket] += 1
    return tally

#price_groups = group_prices_by_range([float(x[2]) for x in data_csv[1:]])
#create_bar_chart(price_groups, "s5_bar_chart_grouped.png")

from prettytable import PrettyTable 

def create_simple_table():
	the_table = PrettyTable(['Style', 'Average Price ($)'])
	the_table.add_row(['Print', pretty_average(find_average(print_ties))])
	the_table.add_row(['Paisley', pretty_average(find_average(paisley_ties))])
	the_table.add_row(['Solid', pretty_average(find_average(solid_ties))])
	the_table.add_row(['Striped', pretty_average(find_average(striped_ties))])
	print(the_table)

def pretty_average(the_number):
	return "{:03.2f}".format(the_number)

#create_simple_table()


def create_table(data_sample, price_groups, brand_names, columns, exported_figure_filename):
    tup = build_table_text(data_sample, brand_names)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for group in price_groups:
        plt.bar(group, price_groups[group]) #color=colors[group%len(price_groups)]

    ax.table(cellText=tup[0], colLabels=columns, rowLabels=tup[1], loc='bottom')
    ax.text(-1.3, 0, 'Discounted Ties Brands', size=12, horizontalalignment='left', verticalalignment='top')
    ax.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        labelbottom='off') # labels along the bottom edge are off

    fig.savefig(exported_figure_filename, dpi=400, bbox_inches='tight')


def count_prices_for_brands(data_sample, brand, min_price, max_price):
    count = 0
    for row in data_sample: 
        if str(row[0]) == str(brand):
            if float(row[1]) < max_price:
                if float(row[1]) > min_price:
                    count += 1
    return count


def build_table_text(data_sample, brands):  
    cell_text = []
    row_text = []

    unique_brand_list = sorted(set(brands))
    for b in unique_brand_list:
        b = bytes.decode(b)
        temp_row = [] 
        group1 = count_prices_for_brands(data_sample, b, 0, 50.00)
        group2 = count_prices_for_brands(data_sample, b, 50.00, 100.00)
        group3 = count_prices_for_brands(data_sample, b, 100.00, 150.00)
        group4 = count_prices_for_brands(data_sample, b, 150.00, 200.00)
        group5 = count_prices_for_brands(data_sample, b, 200.00, 250.00)
        group6 = count_prices_for_brands(data_sample, b, 250.00, 1000.00)
        row_list = [group1, group2, group3, group4, group5, group6]
        temp_row.extend(row_list) 
        
        if group1 > 0:
            if any(x >= group1 for x in row_list[1:]):
                cell_text.append(temp_row)
                row_text.append(b)

    return (cell_text, row_text)


def print_brand_avg_min(name, data_from_csv):
    tie_sample = filter_col_by_string(data_from_csv, "brandName", name)
    avg_price = calculate_sum(tie_sample) / len(tie_sample)
    min_price = find_min(tie_sample[1:], 2)
    print("{2} Average: ${0:6.2f}; Min: ${1:.2f}".format(avg_price, min_price, name))

col = int(data_csv[0].index('brandName'))
brands = [ x[col] for x in data_csv ]







