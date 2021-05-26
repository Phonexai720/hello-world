import datetime as dt

format ='%Y-%m-%dT*H:%M:%S'

t1= dt.datetime.strptime('2008-10-12T14:45:52',format)

print('day'+str(t1.day))

print('month'+str(t1.month))

print('minute'+str(t1.minute))

print('second'+str(t1.second))



# Define todays date and time

t2 = dt.datetime.now()

diff =t2-t1

print('Hơ many dáy diference?'+str(diff.day))
