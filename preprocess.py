import csv

host_dict = dict()


def txt_to_dict(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip('\n')
            host, feature = line.split(' ')
            host_dict[host] = feature


def host_in_dict(host):
    for key in host_dict:
        if key in host:
            return host_dict[key]
    return -1


def pre_process():
    my_dict = dict()
    with open('http-requests.csv', 'r') as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            if row['host'] != '':
                if row['Source'] not in my_dict:
                    my_dict[row['Source']] = set()
                feature = host_in_dict(row['host'])
                if feature != -1:
                    my_dict[row['Source']].add(feature)

    features = list(set(host_dict.values()))
    features.sort()
    print(features)
    with open('processed_requests.csv', 'w') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=features)
        writer.writeheader()

        for value in my_dict.values():
            row_dict = {feature: '' for feature in features}
            for i in value:
                row_dict[i] = 'TRUE'
            writer.writerow(rowdict=row_dict)


if __name__ == '__main__':
    txt_to_dict('host_dict.txt')
    pre_process()
