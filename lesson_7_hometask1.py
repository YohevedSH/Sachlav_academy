emails = {}
emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'
print(emails)
emails.pop('craig')
print(emails)
emails['dalton'] = 'dalton@example.com'
print(emails)
users = list(emails.keys())
print('users =', users)
email_list = list(emails.values())
print('email_list =', email_list)
pairs = list(emails.items())
print('pairs =', pairs)