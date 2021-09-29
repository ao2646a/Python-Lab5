import matplotlib.pyplot as plt
#importmatplotlib

#def main	
def main ():
	#dictionary
	dict_list= [{'TIME': [1981, 1998, 2005, 2006, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2017], 'VALUE': [34.78335, 55.33052, 65.08658, 69.1658, 71.11291, 70.67627, 71.25962, 70.76933, 72.58342, 71.63622, 72.7954, 74.52638], 'LABEL': 'Pakistan', 'COLOR': 'red', 'MARKER': '*', 'LINEWIDTH': 2}, {'TIME': [1993, 1996, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2014, 2015, 2016, 2018], 'VALUE': [95.48465, 96.995, 97.99131, 97.9584, 97.88317, 97.96863, 97.98927, 97.93743, 98.09842, 98.23938, 98.54095, 98.53473, 98.66831, 98.85165], 'LABEL': 'Colombia', 'COLOR': 'yellow', 'MARKER': 'o', 'LINEWIDTH': 2}]
	
	#for loop
	for x in dict_list:
		# #print value_value
		# print(x["VALUE"])

		# #print Time_value
		# print(x["TIME"])

		# #print Label Value
		# print(x["LABEL"])

		#defining what is x and what is y
		plt.plot(x["TIME"],x["VALUE"], label=x["LABEL"], color=x["COLOR"], marker=x["MARKER"], linewidth=x["LINEWIDTH"])

	#legend
	plt.legend ()
	#show command
	plt.show()

def main ():
	#dictionary
	dict_1 = [{'TIME': [1981, 1998, 2005, 2006, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2017], 'VALUE': [34.78335, 55.33052, 65.08658, 69.1658, 71.11291, 70.67627, 71.25962, 70.76933, 72.58342, 71.63622, 72.7954, 74.52638], 'LABEL': 'Pakistan', 'COLOR': 'pink', 'MARKER': 'o', 'LINEWIDTH': 1}, {'TIME': [1993, 1996, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2014, 2015, 2016, 2018], 'VALUE': [95.48465, 96.995, 97.99131, 97.9584, 97.88317, 97.96863, 97.98927, 97.93743, 98.09842, 98.23938, 98.54095, 98.53473, 98.66831, 98.85165], 'LABEL': 'Colombia', 'COLOR': 'purple', 'MARKER':'*', 'LINEWIDTH': 3}]
	#for loop
	for x in dict_1:
		# #print value_value
		# print(x["VALUE"])

		# #print Time_value
		# print(x["TIME"])

		# #print Label Value
		# print(x["LABEL"])

		#scatter plot
		plt.scatter(x["TIME"],x["VALUE"], label=x["LABEL"], color=x["COLOR"], marker=x["MARKER"], linewidth=x["LINEWIDTH"])

	#legend
	plt.legend ()
	#show command
	plt.show()

#Colombia's literacy rate is much higher than Pakistan's


if __name__ == '__main__':
	main()