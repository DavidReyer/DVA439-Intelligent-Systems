import copy
import math


class DecisionTree:

    def __init__(self, data, attributes, target):
        self.data = copy.copy(data)
        self.tree = {}
        values = [d[attributes.index(target)] for d in self.data]
        if not data or (len(attributes) - 1) < 1:
            self.tree = self.majority(attributes, target)
            return
        if values.count(values[0]) == len(values):
            self.tree = values[0]
            return
        best = self.choose_attr(attributes, target)
        self.tree = {best: {}}
        for val in self.get_values(attributes, best):
            examples = self.get_examples(attributes, best, val)
            new_attr = copy.copy(attributes)
            new_attr.remove(best)
            subtree = DecisionTree(examples, new_attr, target).tree
            self.tree[best][val] = subtree

    def majority(self, attributes, target):
        val_freq = {}
        idx = attributes.index(target)
        for d in self.data:
            val_freq[d[idx]] = val_freq.get(d[idx], 0) + 1
        major = ""
        _max = 0
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
        index = attributes.index(best)
        examples = [[]]
        for entry in self.data:
            if entry[index] == val:
                new_entry = []
                for i, element in enumerate(entry):
                    if i != index:
                        new_entry.append(element)
                examples.append(new_entry)
        examples.remove([])
        return examples
