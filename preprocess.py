import csv

if __name__ == '__main__':
    headers = ['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'host']
    my_dict = dict()
    hosts = set()
    with open('capture5.csv', 'r') as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            if row['host'] != '':
                if row['Source'] not in my_dict:
                    my_dict[row['Source']] = set()
                my_dict[row['Source']].add(row['host'])
                hosts.add(row['host'])
    hosts = list(hosts)
    hosts.sort()

    with open('processed_capture5.csv', 'w') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=hosts)
        writer.writeheader()

        for value in my_dict.values():
            rowDict = {host: 0 for host in hosts}
            for i in value:
                rowDict[i] = 1
            writer.writerow(rowdict=rowDict)
