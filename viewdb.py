import pickle

db = open('aguda.db', 'rb')
db1 = open('psyclub.db', 'rb')
db2 = open('empathogens.db', 'rb')
db3 = open('boom.db', 'rb')
db4 = open('sultan.db', 'rb')
db5 = open('isra-nabis.db', 'rb')
users = []
for q in (pickle.load(db)):
	users.append(q)
for q in (pickle.load(db1)):
	users.append(q)
for q in (pickle.load(db2)):
	users.append(q)
for q in (pickle.load(db3)):
	users.append(q)
for q in (pickle.load(db4)):
	users.append(q)
for q in (pickle.load(db5)):
	users.append(q)
for x in users:
	print(x)
