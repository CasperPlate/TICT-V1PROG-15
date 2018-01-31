from __future__ import print_function

import pymysql

conn = pymysql.connect(host='89.98.0.50', port='3306', user='Casper', passwd='welkom01', db='sportschool')

cur = conn.cursor()

cur.execute("SELECT * FROM wp_posts")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()
