
def accept_text(text):
    new = text.split()
    length = len(new)
    return length

def new_text(hello):
    dict_count = {}
    for d in hello:
        d = d.lower()
        if d in dict_count:
           dict_count[d] +=1
        else:
            dict_count[d] = 1

    return dict_count


def new_sorted(dictionary):
    new_list = []
    for k,v in dictionary.items():
        new_list.append({"char": k, "num": v})

    def sort_on(dict):
        return dict["num"]

    new_list.sort(reverse=True, key=sort_on)

    return new_list
