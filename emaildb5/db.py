import sqlite3
conn= sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    d=email.find('@')
    org=email[d+1:]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    try:
         count = cur.fetchone()[0]
         cur.execute('UPDATE counts SET count=count+1 WHERE org=?',(org, ))
    except:
           cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]
conn.commit()
cur.close()


