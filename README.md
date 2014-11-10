# Email Analytics
A small tool written in Python which analyses your email behaviour. Features include:
- Visualising times when emails were sent and received
- Viewing most common words in subject titles
- Viewing most common senders and recipients of emails

See the following link for examples of the graphical output:

http://www.jaijuneja.com/blog/2014/01/what-can-learn-from-emails/

Currently has only been tested using Gmail and Microsoft Exchange.

## How to run
- Open config.py and enter the IMAP settings for your email account
- Open terminal, cd into the root directory and type ```python analytics.py```
- Note that this requires Python 2.7 as it uses the Counter class in the collections module. It is NOT compatible with Python 3.x.

## To do
- [x] Implement list of words to exclude from rankings (e.g. 'and', 're:' etc.)
- [x] Analyse message bodies - e.g. most common words/topics discussed
- [ ] Handle multiple email accounts and sent/received emails at once?
- [x] Compute probability over time of day of sending/receiving email