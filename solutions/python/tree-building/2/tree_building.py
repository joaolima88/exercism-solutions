class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]

    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('Record id is invalid or out of order.')
        if ordered_id[0] != 0:
            raise ValueError('invalid')

    tree = []
    parent = {}

    for j in records:

        if j.record_id == 0 and j.parent_id != 0:
                raise ValueError('Node parent_id should be smaller than its record_id.')
        if j.record_id < j.parent_id:
            raise ValueError('Node parent_id should be smaller than its record_id.')
        if j.record_id == j.parent_id and j.record_id != 0:
                raise ValueError('Only root should have equal record and parent id.')

        if j.record_id in ordered_id:
            tree.append(Node(ordered_id.index(j.record_id)))

    nodes = [i.node_id for i in tree]


    for i in tree:
        parent = i.node_id
        for j in records:
            if j.record_id == 0:
                continue
            if j.parent_id == parent:
                i.children.append(tree[nodes[j.record_id]])
                

    if len(tree) > 0:
        root = tree[0]
    return root