# Email Analytics
A small tool written in Python which analyse your emails. Features include:
- Visualise times when emails were sent and received
- View most common words in subject titles
- View most common senders and recipients of emails

Currently has only been tested using Gmail and Microsoft Exchange.

## How to run
- Open config.py and enter the IMAP settings for your email account
- Open terminal, cd into the root directory and type ```python analytics.py```
- Note that this requires Python 2.7 or higher as it uses the Counter class in the collections module

## To do
[x] Implement list of words to exclude from rankings (e.g. 'and', 're:' etc.)
[ ] Analyse message bodies - e.g. most common words/topics discussed
[ ] Handle multiple email accounts and sent/received emails at once?