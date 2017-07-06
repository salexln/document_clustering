import csv




def load_data(path):
    data = []
    with open(path) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for i, line in enumerate(tsvreader):
            header = line[0].split('~')[1]
            body = line[0].split('~')[2]

            data.append((header, body))
        return data




if __name__ == '__main__':
    data = load_data('../data/seriesx_clause.tsv')


    print data[0]
    print data[1]
    print len(data)
