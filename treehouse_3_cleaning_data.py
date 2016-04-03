from treehouse_2_describing_data import *

def create_bool_field_from_term(sample_data, search_term):
	new_array = []

	#append a column named the search term to the header
	#and add that to the new_array
	new_array.append(sample_data[0].append(search_term))

	for row in sample_data[1:]:
		new_bool_field = False
		if search_term in row[7]: 	#if search term exists in description
			new_bool_field = True 	#set new_bool_field to True

		row.append(new_bool_field)	#add the new field to the row
		new_array.append(row)		#and append this row to the new_array

	return new_array


def filter_col_by_bool(sample_data, col):
	#matches_term = [ item if item[col] == True for item in sample_data[1:] ]
	matches_term = []
	for item in sample_data[1:]:
		if item[col]:
			matches_term.append(item)

	return matches_term

modified_array = create_bool_field_from_term(data_csv, 'cashmere')
matches_found = filter_col_by_bool(modified_array, 11)
total_found = number_of_records(matches_found)
#print(total_found)

def filter_col_by_string(sample_data, fieldname, conditions):
	matches_found = []
	matches_found.append(sample_data[0])

	#get the integer number of the fieldname
	col = int(sample_data[0].index(fieldname))
	for row in sample_data[1:]:
		if row[col] == conditions:
			matches_found.append(row)

	return matches_found

#silk_tie = filter_col_by_string(data_csv, 'material', '_silk')
#print("Found {} silk ties".format(number_of_records(silk_tie)))


def filter_col_by_float(sample_data, fieldname, direction, condition):
	matches_found = []
	matches_found.append(sample_data[0])

	#get the integer number of the fieldname
	col = int(sample_data[0].index(fieldname))
	float_cond = float(condition)

	for row in sample_data[1:]:
		element = float(row[col])
		if direction == '>' and element > float_cond:
			matches_found.append(row)
		elif direction == '>=' and element >= float_cond:
			matches_found.append(row)
		elif direction == '<' and element < float_cond:
			matches_found.append(row)
		elif direction == '<=' and element <= float_cond:
			matches_found.append(row)
		elif direction == '==' and element == float_cond:
			matches_found.append(row)
		else:
			pass

	return matches_found

#searched_tie = filter_col_by_float(data_csv, 'priceLabel', '<=', 20)
#print(number_of_records(searched_tie))

#create several groups of ties
gucci_ties = filter_col_by_string(data_csv, 'brandName', 'Gucci')
jcrew_ties = filter_col_by_string(data_csv, 'brandName', 'J.Crew')

striped_ties = filter_col_by_string(data_csv, 'print', '_striped')
paisley_ties = filter_col_by_string(data_csv, 'print', '_paisley')
solid_ties = filter_col_by_string(data_csv, 'print', '_solid')
print_ties = filter_col_by_string(data_csv, 'print', '_print')

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max(jcrew_ties[1:], 2)

avg_gucci = find_average(gucci_ties)
avg_jcrew = find_average(jcrew_ties)

message = "{}\t{:03.2f}\t{:03.2f}"
#print("Brand\tMaximum\tAverage")
#print(message.format("Gucci", max_gucci, avg_gucci))
#print(message.format("J.Crew", max_jcrew, avg_jcrew))

