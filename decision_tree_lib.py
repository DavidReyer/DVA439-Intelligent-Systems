import copy
import math


class DecisionTree:

    def __init__(self, data, attributes, target, recursion):
        recursion += 1
        self.data = copy.copy(data)
        self.tree = {}
        vals = [record[attributes.index(target)] for record in self.data]
        default = self.majority(attributes, target)

        if not data or (len(attributes) - 1) <= 0:
            self.tree = default
        elif vals.count(vals[0]) == len(vals):
            self.tree = vals[0]
        else:
            best = self.choose_attr(attributes, target)
            self.tree = {best: {}}

            for val in self.get_values(attributes, best):
                examples = self.get_examples(attributes, best, val)
                new_attr = copy.copy(attributes)
                new_attr.remove(best)
                subtree = DecisionTree(examples, new_attr, target, recursion).tree
                self.tree[best][val] = subtree

    def majority(self, attributes, target):
        val_freq = {}
        idx = attributes.index(target)
        for d in self.data:
            val_freq[d[idx]] = val_freq.get(d[idx], 0) + 1
        _max = 0
        major = ""
        for key in val_freq.keys():
            if val_freq[key] > _max:
                _max = val_freq[key]
                major = key
        return major

    def entropy(self, data, attributes, target_attr):
        val_freq = {}
        data_entropy = 0.0
        i = 0
        for entry in attributes:
            if target_attr == entry:
                i -= 1
                break
            i += 1
        for entry in data:
            val_freq[entry[i]] = val_freq.get(entry[i], 0) + 1.0
        for freq in val_freq.values():
            data_entropy += (-freq / len(data)) * math.log(freq / len(data), 2)
        return data_entropy

    def gain(self, attributes, attr, target_attr):
        val_freq = {}
        subset_entropy = 0.0
        i = attributes.index(attr)
        for entry in self.data:
            val_freq[entry[i]] = val_freq.get(entry[i], 0) + 1.0
        for val in val_freq.keys():
            val_prob = val_freq[val] / sum(val_freq.values())
            data_subset = [entry for entry in self.data if entry[i] == val]
            subset_entropy += val_prob * self.entropy(data_subset, attributes, target_attr)
        return self.entropy(self.data, attributes, target_attr) - subset_entropy

    def choose_attr(self, attributes, target):
        best = attributes[0]
        max_gain = 0
        for attr in attributes:
            new_gain = self.gain(attributes, attr, target)
            if new_gain > max_gain:
                max_gain = new_gain
                best = attr
        return best

    def get_values(self, attributes, attr):
        index = attributes.index(attr)
        values = []
        for entry in self.data:
            if entry[index] not in values:
                values.append(entry[index])
        return values

    def get_examples(self, attributes, best, val):
        examples = [[]]
        index = attributes.index(best)
        for entry in self.data:
            if entry[index] == val:
                new_entry = []
                for i in range(0, len(entry)):
                    if i != index:
                        new_entry.append(entry[i])
                examples.append(new_entry)
        examples.remove([])
        return examples
