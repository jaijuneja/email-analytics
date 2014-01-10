import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter as ff
import pylab
from collections import Counter
import numpy as np
import itertools

def min_to_hourmin(minutes, i):
	hrs = int(minutes/60)
	mins = int(minutes%60)
	return '%(h)02d:%(m)02d' % {'h':hrs,'m':mins}

def plot_dates_sent(dates, times):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot_date(dates, times)

	# Rotate x axis labels slightly
	labels = ax.get_xticklabels()
	for label in labels:
	    label.set_rotation(30)
	ax.set_ylim(0,24*60) # 0 to 24 hours
	ax.yaxis.set_major_locator(pylab.MultipleLocator(60))
	ax.yaxis.set_major_formatter(ff(min_to_hourmin))

	plt.title('Times of Message Deliveries')
	plt.xlabel('Date')
	plt.ylabel('Delivery Time (24hr)')
	plt.draw()

def plot_quantity(dates, y_label):
	# dates is a list of strings where each element takes form "mm yy"
	# Convert to unique list
    date_count = Counter(dates)
    date_count = sorted(date_count.items())

    months = [x[0] for x in date_count]
    quantity = [x[1] for x in date_count]

    for ndx, item in enumerate(months):
	 	if ndx%4 != 0:
	 		months[ndx] = ''

    ind = np.arange(len(date_count)) # x locations for the groups
    barwidth = 0.2

    fig, ax = plt.subplots()
    rects = ax.bar(ind, quantity, color='b')
    ax.set_ylabel(y_label)
    ax.set_xlabel('Month')
    ax.set_xticks(ind + barwidth/2)
    ax.set_xticklabels(months)

    # Rotate x labels
    labels = ax.get_xticklabels()

    for label in labels:
    	label.set_rotation(30)

	plt.draw()

def plot_common(words, numwords, x_label, titlestr):
	# Remove spaces between words
	words = [x.lower().split(' ') for x in words]
	words = list(itertools.chain(*words))

	wrd_list = Counter()
	wrd_list.update(words)
	common = wrd_list.most_common()
	common = common[:numwords]

	words = [x[0] for x in common]
	occurrences = [x[1] for x in common]

	# Remove @domain.com from email addresses
	# for ndx, item in enumerate(words):
	# 	name_end = words[ndx].find('@')
	# 	words[ndx] = item[:name_end]

	if len(words) < numwords:
		numwords = len(words)

	ind = np.arange(numwords) # x locations for the groups
	barwidth = 0.35

	fig, ax = plt.subplots()
	rects = ax.bar(ind, occurrences, color='b')
	ax.set_ylabel('Occurrences')
	ax.set_xlabel(x_label)
	ax.set_xticks(ind + barwidth/2)
	ax.set_xticklabels(words)

	# Rotate x labels
	labels = ax.get_xticklabels()
	for label in labels:
	    label.set_rotation(30)

	plt.title('')
	plt.draw()

def done_plotting():
	print 'Execution completed, plotting now!'
	plt.show()