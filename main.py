import csv
import json
from decision_tree_lib import DecisionTree


def main():
    attributes = []
    data = []
    with open('datasets/2/training-data-rank-without-rank-total-by-grades.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                attributes = row
                line_count += 1
            line_count += 1
            data += [row]
    target = "Gpa"
    tree = DecisionTree(data, attributes, target)
    with open('decision_tree.json', 'w') as decision_tree_out_file:
        decision_tree_out_file.write(json.dumps(tree.tree))


if __name__ == '__main__':
    main()
