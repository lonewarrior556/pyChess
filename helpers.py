def list_split(l, element):
    delimiter = l.index(element)+1
    return l[:delimiter]

def get_elements(ls, ls_index):
    array = []
    for x in ls_index:
        array.append(ls[x])
    return array
