# USER-DEFINED EMAIL SETTINGS
IMAP_HOST = 'imap.gmail.com' # For Gmail this is imap.gmail.com
IMAP_USER = 'username'
IMAP_PASS = 'password'
EMAIL_HOST = 'Gmail'
MAIL_TO_ANALYSE = 'Sent' # Choose 'Sent' or 'Received'

# DO NOT EDIT ANYTHING BELOW
if (MAIL_TO_ANALYSE != 'Sent' and MAIL_TO_ANALYSE != 'Received'):
	raise ValueError("MAIL_TO_ANALYSE can only take the values 'Sent' or 'Received'")

if MAIL_TO_ANALYSE == 'Sent':
	if EMAIL_HOST == 'Microsoft Exchange':
		MAIL_STRING = 'Sent Items'
	elif EMAIL_HOST == 'Gmail':
		MAIL_STRING = '[Gmail]/Sent Mail'
	else:
		MAIL_STRING = 'Sent'
else:
	if EMAIL_HOST == 'Microsoft Exchange':
		MAIL_STRING = 'Inbox'
	elif EMAIL_HOST == 'Gmail':
		MAIL_STRING = 'INBOX'
	else:
		MAIL_STRING = 'Inbox'