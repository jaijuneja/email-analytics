import config
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter as ff
import pylab
from collections import Counter
import numpy as np
import itertools
from scipy.interpolate import spline

def min_to_hourmin(minutes, i):
    hrs = int(minutes/60)
    mins = int(minutes%60)
    return '%(h)02d:%(m)02d' % {'h':hrs,'m':mins}

def roundval(x, roundto=60):
    # Round x to nearest bin, where bin size is given by roundto
    return int(roundto * round(float(x)/roundto))

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

def plot_quantity(dates):
    # dates is a list of strings where each element takes form "mm yy"
    # Convert to unique list
    date_count = Counter(dates)
    date_count = sorted(date_count.items())

    months = [x[0] for x in date_count]
    quantity = [x[1] for x in date_count]

    # Remove some x-labels to reduce clutter in the plot
    if len(quantity) > 40:
        label_spacing = 4
    elif len(quantity) > 15:
        label_spacing = 2

    if len(quantity) > 15:
        for ndx, item in enumerate(months):
            if ndx%label_spacing != 0:
                months[ndx] = ''

    ind = np.arange(len(date_count)) # x locations for the groups
    barwidth = 0.2

    fig, ax = plt.subplots()
    rects = ax.bar(ind, quantity, color='b')

    y_label = 'Emails ' + config.MAIL_TO_ANALYSE + ' per Month'
    ax.set_ylabel(y_label)
    ax.set_xlabel('Month')
    ax.set_xticks(ind + barwidth/2)
    ax.set_xticklabels(months)

    # Rotate x labels
    labels = ax.get_xticklabels()

    for label in labels:
        label.set_rotation(30)

    plt.draw()

def plot_common(words, numwords=10, isemail=False, x_label='', 
                titlestr=''):
    # Remove spaces between words
    words = [x.lower().split(' ') for x in words]
    words = list(itertools.chain(*words))

    wrd_list = Counter()
    wrd_list.update(words)
    common = wrd_list.most_common()

    if not isemail:
        # Restricted words
        bad_words = config.EXCLUDE_WORDS
        words = [x[0] for x in common if x[0] not in bad_words]
        occurrences = [x[1] for x in common if x[0] not in bad_words]
        words = words[:numwords]
        occurrences = occurrences[:numwords]
    else:
        common = common[:numwords]
        words = [x[0] for x in common]
        occurrences = [x[1] for x in common]
        # Remove @domain.com from email addresses
        for ndx, item in enumerate(words):
            name_end = words[ndx].find('@')
            words[ndx] = item[:name_end]

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

def plot_probability(times, smoothfit=True):
    # dates is a list of strings where each element takes form "mm yy"
    times = [roundval(x) for x in times]

    # Convert to unique list
    time_count = Counter(times)
    time_count = sorted(time_count.items())

    times = [x[0] for x in time_count]
    quantity = np.array([float(x[1]) for x in time_count])
    quantity = quantity/sum(quantity)

    if smoothfit:
        times_new = np.linspace(min(times), max(times), 300)
        quantity = spline(times,quantity,times_new)
        times = times_new.tolist()

    fig, ax = plt.subplots()
    plt.plot(times, quantity, 'b', linewidth=2.0, )

    # Remove some x-labels to reduce clutter in the plot
    label_spacing = 60 # 1 label per hour
    for ndx, item in enumerate(times):
        if ndx%label_spacing != 0:
                times[ndx] = ''

    ax.set_xlabel('Time')
    ax.set_xticklabels(times)
    # Rotate x axis labels slightly
    labels = ax.get_xticklabels()
    for label in labels:
        label.set_rotation(30)
    ax.set_xlim(0,24*60) # 0 to 24 hours
    ax.xaxis.set_major_locator(pylab.MultipleLocator(60))
    ax.xaxis.set_major_formatter(ff(min_to_hourmin))

    ax.set_ylabel('Probability')
    ax.set_ylim(0, max(quantity))

    titlestr = 'Probability Over Time of ' + config.MAIL_TO_ANALYSE + ' Mail'
    plt.title(titlestr)
    plt.draw()

def done_plotting():
    print 'Execution completed, plotting now!'
    plt.show()