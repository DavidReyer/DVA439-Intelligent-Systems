import json

def process_input(edu_tree, input_dict):
    for item in input_dict.keys():
        if item in edu_tree:
            print("Doing node: " + item)
            print("Edu Tree: " + str(edu_tree[item]))
            while len(edu_tree[item]) == 1:
                print("Len too short")
                newitem = [x for x in edu_tree[item].keys()]
                edu_tree = edu_tree[item]
                item = newitem[0]
                print("Using item " + item)
                print("Edu Tree: " + str(edu_tree[item]))
            newtree = edu_tree[item][input_dict[item]]
            if type(newtree) == str: #leafnode
                print("leaf! " + newtree)
                return newtree
            else:
                process_input(newtree, input_dict)