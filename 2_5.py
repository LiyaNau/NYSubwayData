import csv
def read_scv(filename):
    in_file = open('c:\\Leah\\udacity\\P1\\' + filename, 'rb')
    out_file = open('c:\\Leah\\udacity\\P1\\updated_' + filename,'wb')
    #print out_file
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)
    #print reader
    for row in reader:
        #print row
        prefix = row[0:3]
        i = 3
        while i < len(row)-1:
            new_row = []
            new_row += prefix + row[i:i+5]
            writer.writerow(new_row)
            #print new_row
            i += 5

read_scv('turnstile_110507.txt')
