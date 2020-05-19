# from math import floor
#
# s1 = 1.5
#
# s2 = 2
# if s1<s2:
#     print(type(s1))
#
# import csv
#
# with open('data.csv','w') as f:
#     w = csv.writer(f)
#     w.writerow(['1','2','3'])
#     w.writerow(['a','b','c'])
import cymysql
conn = cymysql.connect(host='localhost',port=3306,user='root',passwd='nishengri')
cur = conn.cursor()
cur.execute('select version()')
data = cur.fetchone()

print(data)

