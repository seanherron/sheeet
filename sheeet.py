import csv
import os
from xlrd import open_workbook

# Get files in current directory
path = './'
listing = os.listdir(path)

# Iterate through each file
for filename in listing:
    # Check to make sure the file is at least apparently excel
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        wb = open_workbook(filename, on_demand=True)
        for s in wb.sheets():
            print 'Sheeeting %s %s' % (filename, s.name)
            with open('%s-%s.csv' % (filename.split(".")[0], s.name), 'wb') as f:
                writer = csv.writer(f)
                for rownum in xrange(s.nrows):
                    writer.writerow(s.row_values(rownum))
    else:
        pass