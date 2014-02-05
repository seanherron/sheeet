from xlrd import open_workbook
import csv 

wb = open_workbook('data.xlsx', on_demand=True)
for s in wb.sheets():
    print 'Sheet:',s.name
    with open('%s.csv' % s.name, 'wb') as f:
        writer = csv.writer(f)
        for rownum in xrange(s.nrows):
            writer.writerow(s.row_values(rownum))