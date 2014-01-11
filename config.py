# USER-DEFINED EMAIL SETTINGS
IMAP_HOST = 'imap.gmail.com' # For Gmail this is imap.gmail.com
IMAP_USER = 'username'
IMAP_PASS = 'password'
EMAIL_HOST = 'Gmail'
MAIL_TO_ANALYSE = 'Sent' # Choose 'Sent' or 'Received'

NUM_DAYS = None # Number of days to go back. To view all emails, set to None.
# Note that sometimes there are errors when the program tries to fetch too many emails
# Hence the need for a date restriction

# Words to exclude from "most common words" plot
EXCLUDE_WORDS = ['re:', 'fwd:', 'fw:', '-', ' ', '', 'the', 'be', 'to', 'of',
				'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not',
				'on', 'with', 'as', 'you', 'do', 'at', 'this', 'by', 'from',
				 'they', 'or', 'an', 'your']

# DO NOT EDIT ANYTHING BELOW HERE --------------------------
if (MAIL_TO_ANALYSE.lower() != 'sent' and MAIL_TO_ANALYSE.lower() != 'received'):
	raise ValueError("MAIL_TO_ANALYSE can only take the values 'Sent' or 'Received'")

if MAIL_TO_ANALYSE == 'Sent':
	if EMAIL_HOST.lower() == 'microsoft exchange':
		MAIL_STRING = 'Sent Items'
	elif EMAIL_HOST.lower() == 'gmail':
		MAIL_STRING = '[Gmail]/Sent Mail'
	else:
		MAIL_STRING = 'Sent'
else:
	MAIL_STRING = 'INBOX'