# TODO:
# Take input arguments from user
# Automate figuring out Send text
# Graphical output
# Start and end date

import imaplib
import email
from datetime import datetime
from matplotlib.ticker import FuncFormatter as ff

def convert_to_datetime(date):
	# Remove timezone
	date_end = date.find(' +')
	date = date[:date_end]

	date_start = date.find(',') + 2
	# Convert day from %e to %d format so we can pass it into strptime
	if date.find(' ', date_start) == date_start + 1:
		date = date[:date_start] + '0' + date[date_start:]

	# Convert date to datetime object
	newdate = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S")
	# Time is set to an integer value between 0 and 24*60
	newtime = newdate.strftime("%H %M")
	newtime = int(newtime[0:1]) * 60 + int(newtime[3:4])

	return newdate, newtime

def min_to_hourmin(minutes)
	hrs = int(minutes/60)
	mins = int(mins%60)
	return '%(h)02d:%(m)02d' % {'h':hrs,'m':mins}

mail = imaplib.IMAP4_SSL('imap.nexus.ox.ac.uk')
mail.login('user', 'pass')
mail.list()
# Out: list of "folders" aka labels in gmail.
# For gmail this is "[Gmail]/Sent Mail"
mail.select("Sent Items") # connect to inbox.

status, email_uids = mail.uid('search', None, "ALL") # search and return uids instead
all_email_uids = ','.join(email_uids[0].split())

status, data = mail.uid('fetch', all_email_uids, '(BODY.PEEK[HEADER])')
if status != 'OK':
	raise Exception("Error running imap search for spinvox messages: "
					"%s" % status)

dates = []
times = []
for i in range(len(email_uids[0].split())):
	email_header = data[i * 2][1]
	header_message = email.message_from_string(email_header)
	date = header_message['Date']
	newdate, newtime = convert_to_datetime(date)
	dates.append(newdate)
	times.append(newtime)