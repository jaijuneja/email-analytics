# TODO:
# Implement list of words to exclude from rankings (e.g. 'and', 're:' etc.)
# Analyse message bodies - e.g. most common words/topics

import config
import plot_mail
import imaplib
import email
from datetime import datetime
import time
import matplotlib.pyplot as plt

def convert_to_datetime(date):
	date = email.utils.parsedate(date)

	try:
		date = time.mktime(date)
		newdate = datetime.fromtimestamp(date)
	except (ValueError):
		return None, None, None

	# Convert date to datetime object
	# newdate = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S")
	monthyear = newdate.strftime("%Y %m")

	# Time is set to an integer value between 0 and 24*60
	newtime = newdate.strftime("%H %M")
	hour = int(''.join(newtime[0:2]))
	minute = int(''.join(newtime[3:]))
	newtime = hour * 60 + minute

	return newdate, newtime, monthyear

# CONNECT TO EMAIL VIA IMAP
mail = imaplib.IMAP4_SSL(config.IMAP_HOST)
mail.login(config.IMAP_USER, config.IMAP_PASS)
mail.list() # List of "folders" aka labels in email account
mail.select(config.MAIL_STRING) # connect to mailbox

status, email_uids = mail.uid('search', None, "ALL") # search and return uids instead
all_email_uids = ','.join(email_uids[0].split())

status, data = mail.uid('fetch', all_email_uids, '(BODY.PEEK[HEADER])')
if status != 'OK':
	raise Exception("Error running imap search for spinvox messages: "
					"%s" % status)

# COLLECT EMAIL DATA
dates = []
monthyears = []
times = []
recipients = []
senders = []
subjects = []
for i in range(len(email_uids[0].split())):
	email_header = data[i * 2][1]
	header_message = email.message_from_string(email_header)

	# Get Date
	date = header_message['Date']
	newdate, newtime, monthyear = convert_to_datetime(date)
	
	# Get recipient's email address
	recipient = header_message['To']
	recipient = email.utils.parseaddr(recipient)[1].lower()

	sender = header_message['From']
	sender = email.utils.parseaddr(sender)[1].lower()

	# Get subject
	subject = header_message['Subject']

	if (newdate != '' and newdate is not None):
		dates.append(newdate)
		times.append(newtime)
		monthyears.append(monthyear)
	if (recipient != '' and recipient is not None):
		recipients.append(recipient)
	if (sender != '' and sender is not None):
		senders.append(sender)
	if (subject != '' and subject is not None):
		subjects.append(subject)

# PLOT RESULTS
# Plot times at which emails have been sent
plot_mail.plot_dates_sent(dates, times)
# Plot most common words in email subjects
plot_mail.plot_common(subjects, 10, 'Subject Words')
# Plot the number of emails sent/received per month
plot_mail.plot_quantity(monthyears, 'Emails ' + 
						config.MAIL_TO_ANALYSE + ' per Month')

# Plot the 10 most common email senders or recipients
if config.MAIL_TO_ANALYSE == 'Sent':
	plot_mail.plot_common(senders, 10, 'Senders', 'Common Senders')
else:
	plot_mail.plot_common(recipients, 10, 'Recipients', 'Common Recipients')

plot_mail.done_plotting()