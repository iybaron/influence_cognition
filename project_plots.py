import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns; sns.set(style="whitegrid", color_codes=True)
import random
import itertools

# Custom colors for plots
c_green = '#59C23F'
c_blue = '#3F9AC2'
c_orange = '#F8A71A'
c_purple = '#B600FF'
c_red = '#FF8D8D'
c_pink = '#FF0060'

def label_pies(labels):
	''' Create collection of pie charts for DPx labels '''

	fig = plt.figure()

	# Get info for DPLETTER ready
	letter_labels = 'All', 'Most', 'Some', 'None'
	_, letter_sizes = np.unique(labels['DPLETTER'], return_counts=True)
	letter_colors = [c_green, c_blue, c_orange, c_purple]
	ax = plt.subplot(2, 5, 2)
	ax.axis('equal')
	ax.set_title('DPLETTER')
	ax.pie(letter_sizes, labels=letter_labels, colors=letter_colors, startangle=90,
	       radius=2, center=(0,0))

	# Add info for DPCOUNT
	count_labels = '', 'Five', 'Ten', 'Twenty', 'Fifty', 'Hundred'
	_, count_sizes = np.unique(labels['DPCOUNT'], return_counts=True)
	count_colors = [c_green, c_blue, c_orange, c_purple, c_red, c_pink]
	ax = plt.subplot(2, 5, 8)
	ax.axis('equal')
	ax.set_title('DPCOUNT')
	ax.pie(count_sizes, labels=count_labels, colors=count_colors, startangle=90,
	       radius=2, center=(0,0))

	# Add info for DPNAME
	name_labels = 'Yes', 'No'
	_, name_sizes = np.unique(labels['DPNAME'], return_counts=True)
	name_colors = [c_green, c_blue]
	ax = plt.subplot(2, 5, 4)
	ax.axis('equal')
	ax.set_title('DPNAME')
	ax.pie(name_sizes, labels=name_labels, colors=name_colors, startangle=90,
	       radius=2, center=(0,0))

	# Add info for DPRHYME
	rhyme_labels = 'Yes', 'No'
	_, rhyme_sizes = np.unique(labels['DPRHYME'], return_counts=True)
	rhyme_colors = [c_green, c_blue]
	ax = plt.subplot(2, 5, 6)
	ax.axis('equal')
	ax.set_title('DPRHYME')
	ax.pie(rhyme_sizes, labels=rhyme_labels, colors=rhyme_colors, startangle=90,
	       radius=2, center=(0,0))

	# Add info for DPFIDGET
	fidget_labels = 'Never', 'Rarely', 'Sometimes', 'Often', 'Always'
	_, fidget_sizes = np.unique(labels['DPFIDGET'], return_counts=True)
	fidget_colors = [c_green, c_blue, c_orange, c_purple, c_red]
	ax = plt.subplot(2, 5, 10)
	ax.axis('equal')
	ax.set_title('DPFIDGET')
	ax.pie(fidget_sizes, labels=fidget_labels, colors=fidget_colors, startangle=90,
	       radius=2, center=(0,0))

	plt.show()

# This function was based on an article written by Chris Albon 
# http://chrisalbon.com/python/matplotlib_percentage_stacked_bar_plot.html
def plot_categorical_features(data, label):
	''' Plots bar graphs of 4 categorical features.  These
	charts represent the percentage of children in each category
	that can write their own name.
	
	'''
	
	data = pd.concat([data, label], axis=1)

	# Create a figure with a single subplot
	f, ax = plt.subplots(1, figsize=(14,8))

	# Set bar width at 1
	bar_width = 1

	# Positions of the left bar-boundaries
	bar_l = [0, 1, 3, 4, 6, 7, 8, 10, 11, 12]

	# Positions of the x-axis ticks (center of the bars)
	tick_pos = [0.5, 1, 1.5, 3.5, 4, 4.5, 6.5, 7.5, 7.51, 8.5, 10.5, 11.5, 11.51, 12.5]

	# Create the total score for each participant
	totals = [len(data[data['ENROLL'] == 1]), len(data[data['ENROLL'] == 2]), \
			  len(data[data['CPNNOW'] == 1]), len(data[data['CPNNOW'] == 2]), \
			  len(data[data['FOCHREAD'] == 1]), len(data[data['FOCHREAD'] == 2]), \
			  len(data[data['FOCHREAD'] == 3]), \
			  len(data[data['FOLETTR'] == 1]), len(data[data['FOLETTR'] == 2]), \
			  len(data[data['FOLETTR'] == 3])]

	# Create totals of those who can write name from each category (Enrolled/Not Enrolled, etc)
	dpname_totals = [len(data[(data['ENROLL'] == 1) & (data['DPNAME'] == 1)]), \
					 len(data[(data['ENROLL'] == 2) & (data['DPNAME'] == 1)]), \
					 len(data[(data['CPNNOW'] == 1) & (data['DPNAME'] == 1)]), \
					 len(data[(data['CPNNOW'] == 2) & (data['DPNAME'] == 1)]), \
					 len(data[(data['FOCHREAD'] == 1) & (data['DPNAME'] == 1)]), \
					 len(data[(data['FOCHREAD'] == 2) & (data['DPNAME'] == 1)]), \
					 len(data[(data['FOCHREAD'] == 3) & (data['DPNAME'] == 1)]), \
					 len(data[(data['FOLETTR'] == 1) & (data['DPNAME'] == 1)]), \
					 len(data[(data['FOLETTR'] == 2) & (data['DPNAME'] == 1)]), \
					 len(data[(data['FOLETTR'] == 3) & (data['DPNAME'] == 1)])]

	# Create a bar chart in position bar_l
	total_rects = ax.bar(bar_l,
		   # using totals data
		   totals,
		   # labeled
		   label='features',
		   # with alpha
		   alpha=0.8,
		   # with color
		   color=c_green,
		   # with bar_width
		   width=bar_width,
		   # with border color
		   edgecolor='white'
		)

	# Create a bar chart in position bar_l
	dpname_rects = ax.bar(bar_l,
		   # using totals data
		   dpname_totals,
		   # labeled
		   label='DPNAME',
		   # with alpha
		   alpha=0.8,
		   # with color
		   color=c_blue,
		   # with bar_width
		   width=bar_width,
		   # with border color
		   edgecolor='white'
		)

	# Set the ticks labels
	plt.xticks(tick_pos, ['Yes', 'Enrolled In School', 'No', 'Yes', 'Attends Center-Based Program', 'No', \
						  'Usually', 'Sometimes', 'Reads With Family', 'Never', \
						  'Usually', 'Sometimes', 'Asks About Letters', 'Never'])
	ax.set_ylabel('Children')
	ax.set_xlabel('')
	ax.grid('off', axis='x')

	# vertical alignment of xtick labels
	va = [0, -0.03, 0, 0, -0.03, 0, 0, 0, -0.03, 0, 0, 0, -0.03, 0]
	
	for t, y in zip(ax.get_xticklabels(), va):
		t.set_y(y)


	# Set the borders of the graphic
	plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
	plt.ylim(-10, 1600)

	# Include percentage values in visual
	for dpname_rect, total_rect in zip(dpname_rects, total_rects):
		dpname_height = dpname_rect.get_height()
		total_height = total_rect.get_height()
		ax.text(dpname_rect.get_x() + dpname_rect.get_width()/2., \
			dpname_height + 0.01, '%.*f%%' % (2, 100*float(dpname_height)/total_height), \
			ha='center', va='bottom')
	
	# Add Legend to plot
	ax.legend((dpname_rects[0], total_rects[0]), ('Can Write Name', 'Total'))
	# Show plot
	plt.show()



# This function was based on an article written by Chris Albon 
# http://chrisalbon.com/python/matplotlib_percentage_stacked_bar_plot.html
def plot_parent_education(data, label):
	''' Plots bar graphs of parents educational level, overlaid
	by their child's ability to write his/her own name.
	
	'''
	
	data = pd.concat([data, label], axis=1)
	
	# Create a figure with a single subplot
	f, ax = plt.subplots(1, figsize=(14,8))

	# Set bar width at 1
	bar_width = 1

	# Positions of the left bar-boundaries
	bar_l = range(13)

	# Positions of the x-axis ticks (center of the bars)
	tick_pos = [a+0.5 for a in range(13)]

	# Create lists of total counts for each grade level for each parent
	mg_unique, totals = np.unique(data['MOMGRADE1'], return_counts=True)

	# Create totals of those who can write name from each category
	dpname_totals = []
	for mg_category in mg_unique:
		dpname_totals.append(len(data[(data['MOMGRADE1'] == mg_category) & (data['DPNAME'] == 1)]))

	# Create a bar chart in position bar_l
	total_rects = ax.bar(bar_l,
		   # using totals data
		   totals,
		   # labeled
		   label='categories',
		   # with alpha
		   alpha=0.8,
		   # with color
		   color=c_red,
		   # with bar_width
		   width=bar_width,
		   # with border color
		   edgecolor='white'
		)

	# Create a bar chart in position bar_l
	dpname_rects = ax.bar(bar_l,
		   # using totals data
		   dpname_totals,
		   # labeled
		   label='DPNAME',
		   # with alpha
		   alpha=0.8,
		   # with color
		   color=c_orange,
		   # with bar_width
		   width=bar_width,
		   # with border color
		   edgecolor='white'
		)

	# Set the ticks labels
	tick_labels = ['8th', '9th-11th', '12th', 'HSD', 'VOC/NO HSD', 'VOC/HSD', \
				   'Some College', 'Associate\'s', 'Bachelor\'s', 'Grad School', \
				   'Master\'s', 'PHD', 'Professional Degree']
	plt.xticks(tick_pos, tick_labels)
	ax.set_ylabel('Children')
	ax.set_xlabel('Mother\'s Level of Education')
	ax.grid('off', axis='x')

	# Let the borders of the graphic
	plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
	plt.ylim(-10, 700)

	# rotate axis labels
	plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

	# Include percentage values in visuals
	for dpname_rect, total_rect in zip(dpname_rects, total_rects):
		dpname_height = dpname_rect.get_height()
		total_height = total_rect.get_height()
		ax.text(dpname_rect.get_x() + dpname_rect.get_width()/2., \
			dpname_height + 0.01, '%.*f%%' % (2, 100*float(dpname_height)/total_height), \
			ha='center', va='bottom')

	# Add legend to plot
	ax.legend((dpname_rects[0], total_rects[0]), ('Can Write Name', 'Total'))
	# Show plot
	plt.show()


def tv_heatmap(data, label):
	''' Create heatmap with hours of tv watched in a week
	as columns and ability to write name as index
	'''

	features = ['Hours of TV each week', 'Proportion Of Children', 'percent']
	data = pd.concat([data['TVHOURS'], label], axis=1)

	# Put TVHOURS data into 12 bins
	max_tvhours = int(data['TVHOURS'].max())
	bucket_size = max_tvhours / 11
	buckets = range(bucket_size, bucket_size*13, bucket_size)
	
	for bucket in buckets:
		data.loc[(data['TVHOURS'] <= bucket) & (data['TVHOURS'] > bucket-bucket_size), 'TVHOURS'] = bucket

	# Create pivot table to be used with seaborn heatmap
	data.loc[data['DPNAME'] == 1, 'DPNAME'] = 'Can Write'
	data.loc[data['DPNAME'] == 2, 'DPNAME'] = 'Cannot Write'	
	pivot_dict_list = []
	
	for tv_val, dpname_val in itertools.product(np.unique(data['TVHOURS']), np.unique(data['DPNAME'])):
		count = len(data.loc[(data['TVHOURS'] == tv_val) & (data['DPNAME'] == dpname_val)])
		total = len(data.loc[(data['TVHOURS'] == tv_val)])
		percent = float(count) / total
		pivot_dict_list.append(dict(zip(features, [tv_val, dpname_val, percent])))

	data = pd.DataFrame(pivot_dict_list)				
	pivot_data = data.pivot(columns='Hours of TV each week', index='Proportion Of Children', values='percent')
	
	# Plot figure
	plt.figure(figsize=(9,3))
	ax = sns.heatmap(pivot_data)


def momnew_heatmap(data, label):
	''' Create heatmap with age mom first had a child
	as columns and ability to write name as index
	'''

	features = ['Age When Mother First Had a Child', 'Proportion Of Children', 'percent']
	data = pd.concat([data['MOMNEW1'], label], axis=1)

	# Put TVHOURS data into 12 bins
	max_momnew = int(data['MOMNEW1'].max())
	min_momnew = int(data['MOMNEW1'].min())

	bucket_size = (max_momnew - min_momnew) / 10
	buckets = range(min_momnew+bucket_size, min_momnew+(bucket_size*12), bucket_size)
	
	for bucket in buckets:
		data.loc[(data['MOMNEW1'] <= bucket) & (data['MOMNEW1'] > bucket-bucket_size), 'MOMNEW1'] = bucket

	# Create pivot table to be used with seaborn heatmap
	data.loc[data['DPNAME'] == 1, 'DPNAME'] = 'Can Write'
	data.loc[data['DPNAME'] == 2, 'DPNAME'] = 'Cannot Write'	
	pivot_dict_list = []
	
	for momnew_val, dpname_val in itertools.product(np.unique(data['MOMNEW1']), np.unique(data['DPNAME'])):
		count = len(data.loc[(data['MOMNEW1'] == momnew_val) & (data['DPNAME'] == dpname_val)])
		total = len(data.loc[(data['MOMNEW1'] == momnew_val)])
		percent = float(count) / total
		pivot_dict_list.append(dict(zip(features, [momnew_val, dpname_val, percent])))

	data = pd.DataFrame(pivot_dict_list)			
	pivot_data = data.pivot(columns='Age When Mother First Had a Child', index='Proportion Of Children', values='percent')
	
	# Plot figure
	plt.figure(figsize=(9,3))
	ax = sns.heatmap(pivot_data, cmap='YlGn')




def change_cpnnow_values(data):
	''' Changes values of CPNNOW for use with compare_pies'''

	length = len(data[data['CPNNOW'] == 1])
	half_length = length / 2
	sample = random.sample((data[data['CPNNOW'] == 1]).index.values, half_length)
	data.loc[sample, 'CPNNOW'] = 0
	return data

def change_fochread_values(data):
	''' Changes values of FOCHREAD for use with compare_pies'''

	data.loc[data['FOCHREAD'] == 1, 'FOCHREAD'] = 0
	return data

def change_sedowell_values(data):
	''' Changes values of SEDOWELL for use with compare_pies'''

	data.loc[data['SEDOWELL'] <= 0.3, 'SEDOWELL'] += 0.3
	return data

def change_tvhours_values(data):
	''' Changes values of TVHOURS for use with compare_pies'''

	data.loc[data['TVHOURS'] >= 0.6, 'TVHOURS'] -= 0.3
	return data

def compare_pies(clf, data, y_true):
	''' Creates six pie charts in one plot.
	One pie chart represents actual values of DPNAME
	One represents the results in DPNAME from the supervised
	learner.  The last 4 represent the predictions of the
	supervised learner with values in the important features
	altered 
	'''

	# Get classifier prediction
	y_pred = clf.predict(data)
	
	# Adjust values of CPNNOW and make new prediction
	cpnnow_data = data.copy()
	cpnnow_data = change_cpnnow_values(cpnnow_data)
	cpnnow_y_pred = clf.predict(cpnnow_data)

	# Adjust values of FOCHREAD
	fochread_data = data.copy()
	fochread_data = change_fochread_values(fochread_data)
	fochread_y_pred = clf.predict(fochread_data)

	# Adjust values of SEDOWELL
	sedowell_data = data.copy()
	sedowell_data = change_sedowell_values(sedowell_data)
	sedowell_y_pred = clf.predict(sedowell_data)

	# Adjust values of TVHOURS
	tvhours_data = data.copy()
	tvhours_data = change_tvhours_values(tvhours_data)
	tvhours_y_pred = clf.predict(tvhours_data)

	# Add info for actual values
	name_labels = 'Yes', 'No'
	_, name_sizes = np.unique(y_true, return_counts=True)
	actual_colors = [c_green, c_blue]
	ax = plt.subplot(2, 3, 1)
	ax.axis('equal')
	ax.set_title('ACTUAL DISTRIBUTION', y=1.1)
	ax.pie(name_sizes, labels=name_labels, colors=actual_colors, startangle=90,
	       radius=1.4, center=(0,0))

	# Add info for predicted values
	_, pred_sizes = np.unique(y_pred, return_counts=True)
	pred_colors = [c_orange, c_red]
	ax = plt.subplot(2, 3, 2)
	ax.axis('equal')
	ax.set_title('BASE PREDICTION', y=1.1)
	ax.pie(pred_sizes, labels=name_labels, colors=pred_colors, startangle=90,
	       radius=1.4, center=(0,0))

	# Add info for predicted values with CPNNOW updated
	_, cpnnow_sizes = np.unique(cpnnow_y_pred, return_counts=True)
	new_colors = [c_purple, c_pink]
	ax = plt.subplot(2, 3, 3)
	ax.axis('equal')
	ax.set_title('UNENROLLMENT HALVED', y=1.1)
	ax.pie(cpnnow_sizes, labels=name_labels, colors=new_colors, startangle=90,
	       radius=1.4, center=(0,0))

	# Add info for predicted values with FOCHREAD updated
	_, fochread_sizes = np.unique(fochread_y_pred, return_counts=True)
	ax = plt.subplot(2, 3, 4)
	ax.axis('equal')
	ax.set_title('MORE FAMILY READING', y=1.05)
	ax.pie(fochread_sizes, labels=name_labels, colors=new_colors, startangle=90,
	       radius=1.4, center=(0,0))

	# Add info for predicted values with SEDOWELL updated
	_, sedowell_sizes = np.unique(sedowell_y_pred, return_counts=True)
	ax = plt.subplot(2, 3, 6)
	ax.axis('equal')
	ax.set_title('INCREASED TEACHER CONTACT', y=1.05)
	ax.pie(sedowell_sizes, labels=name_labels, colors=new_colors, startangle=90,
	       radius=1.4, center=(0,0))

	# Add info for predicted values with TVHOURS updated
	_, tvhours_sizes = np.unique(tvhours_y_pred, return_counts=True)
	ax = plt.subplot(2, 3, 5)
	ax.axis('equal')
	ax.set_title('REDUCED TV TIME', y=1.05)
	ax.pie(tvhours_sizes, labels=name_labels, colors=new_colors, startangle=90,
	       radius=1.4, center=(0,0))

	# Plot figure with tight_layout to prevent overlap of titles
	plt.tight_layout()