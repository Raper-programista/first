import datetime
now = datetime.datetime.now()
hour = now.hour
if hour == 9 or hour == 12:
  print('Napij się kawy')
else:
  print('aaa już nic')