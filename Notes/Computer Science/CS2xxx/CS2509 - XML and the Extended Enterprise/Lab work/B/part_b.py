#!/usr/local/bin/python3

from cgitb import enable
enable()

import pymysql as db

output = """<?xml version="1.0"?>
<!DOCTYPE customers SYSTEM "customers.dtd">
<?xml-stylesheet type="text/xsl" href="customerTable.xsl"?>
<customers>"""

try:
    connection = db.connect('cs1dev.ucc.ie', 'nfb2', 'aiphaehe', '2019_nfb2')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""
    SELECT * FROM customers;
    """)
    cursor.close()
    connection.close()
except db.Error:
    pass
else:
    if cursor.rowcount != 0:
        for row in cursor.fetchall():
            output += """
    <customer>
        <customerID>%s</customerID>
        <name>%s</name>
        <address>
            <addressLine1>%s</addressLine1>
            <addressLine2>%s</addressLine2>
            <addressLine3>%s</addressLine3>
        </address>
        <phoneNumber>%s</phoneNumber>
    </customer>""" % (row['customerID'], row['name'], row['addressLine1'],
                      row['addressLine2'], row['addressLine3'], row['phoneNumber'])

        output += """
</customers>
"""
print("Content-Type: text/xml")
print()
print(output)
