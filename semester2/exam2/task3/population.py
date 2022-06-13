"""var7, task3"""

from linkedbst import LinkedBST
import json
from sys import exit

filepath = 'Kosiv_state.json'

def read_file(file_path):
    """Read file and make list of dicts."""
    file = []
    with open(file_path, "r") as f:
        data = json.load(f)
        data = data["Косівщина"]
        for line in data:
            file.append([line["рік"], line["населений пункт"],
            line["гр-кат."], sum([line["гр-кат."], line['лат.'],
            line['вірм.'], line['жид.'], line['акат.']])])
    a = lambda x: x[1][-2:] == "ти"
    b = lambda x: x[1][-1] == "і"
    c = lambda x: x[1][0] == "Б"
    kutys = {}
    for i in list(filter(a, file)):
        kutys[i[0]] = round((i[2]/i[3])*100, 2)
    oldkutys = {}
    for i in list(filter(b, file)):
        oldkutys[i[0]] = round((i[2]/i[3])*100, 2)
    brustury = {}
    for i in list(filter(c, file)):
        brustury[i[0]] = round((i[2]/i[3])*100, 2)
    return [kutys, oldkutys, brustury]

def create_tree(lst):
    """Create BST of data."""
    tree = LinkedBST()
    for val in set(lst.values()):
        tree.add(val)
    return tree

def find_bigger_list(tree, val):
    """Helper func."""
    list_tree = list(tree.inorder())
    result = []
    for i in list_tree:
        if i > val:
            result.append(i)
    return result

def find_bigger_one(path, i, val):
    """Find list of years with bigger percent."""
    lst = read_file(path)[i]
    tree = find_bigger_list(create_tree(lst), val)
    result = []
    for key, valu in lst.items():
        if valu in tree:
            result.append(key)
    return result

def population_trees(path, percent, num):
    """MAIN FUNCTION"""
    kutys = create_tree(read_file(path)[0])
    old_kutys = create_tree(read_file(path)[1])
    brustury = create_tree(read_file(path)[2])
    print("Відсоткове дерево греко-католиків у Кутах:")
    print(kutys)
    print("Відсоткове дерево греко-католиків у Старих Кутах:")
    print(old_kutys)
    print("Відсоткове дерево греко-католиків у Брустурах:")
    print(brustury)

    ## if you want to use the full functional, uncomment this string of code
    # print(f"Роки, коли у вказаному селищі відсоток католиків був більший, ніж {percent}% :")
    # print(find_bigger_one(path, num, percent))

    return [kutys, old_kutys, brustury]

if __name__ == "__main__":
    ## if you want to use the full functional, uncomment this section of code
    # try:
    #     print("Enter one of three places:")
    #     place = input("Кути, Старі Кути, Брустури: ")
    #     percent = float(input("Enter a percent (with a dot, if not integer): "))
    #     places = {0:"Кути", 1:"Старі Кути", 2: "Брустури"}
    #     if place not in places.values():
    #         raise KeyError
    #     inx = list(places.values()).index(place)
    #     num = list(places.keys())[inx]
    # except (KeyError, ValueError):
    #     print("Sorry, something went wrong, try again.")
    #     exit()

    ## and comment this part (next 2! lines)
    percent = 0
    num = 0

    population_trees(filepath, percent, num)
