import csv

CONVERT = {
    70: 'A-B',
    60: 'C',
    50: 'D',
    0: 'F'
}


def get_int(x):
    try:
        return int(x)
    except:
        return 0


def main():
    data = []
    with open('datasets/2/training-data-rank-without-rank-total.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data += [row]
    with open('datasets/2/training-data-rank-without-rank-total-by-grades.csv', 'w') as csv_out_file:
        for i, d in enumerate(data):
            if i == 0:
                csv_out_file.write("{}\n".format(','.join(d)))
                continue
            res = map(lambda x: CONVERT[[k for k in sorted(CONVERT.keys(), reverse=True) if get_int(x) >= k][0]],
                      d[:-1])
            csv_out_file.write("{},{}\n".format(','.join(res), d[-1]))


if __name__ == '__main__':
    main()
