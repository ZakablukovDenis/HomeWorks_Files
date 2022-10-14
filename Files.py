cook_book = {}


def read_file():
    with open('recipes.txt', 'rt', encoding='utf8') as file:
        for value in file:
            dishes = value.strip()
            cook_book[dishes] = []
            quantity = file.readline()
            for i in range(int(quantity)):
                data = file.readline()
                ingredient_name, quantity, measure = data.strip().split(' | ')
                cook_book[dishes].append({'ingredient_name': ingredient_name,
                                          'quantity': int(quantity),
                                          'measure': measure})
            bl = file.readline()


def print_dict():
    for key, value in cook_book.items():
        print(key)
        for i in value:
            print(i)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for val in dishes:
        for elem in cook_book[val]:
            if elem['ingredient_name'] not in result.keys():
                result[elem['ingredient_name']] = \
                    {"measure": elem['measure'], "quantity": elem['quantity'] * person_count}
            else:
                summa = result[elem['ingredient_name']]['quantity'] + (elem['quantity'] * person_count)
                result[elem['ingredient_name']].update({"quantity": summa})

    for key, val in result.items():
        print(key, val)


if __name__ == "__main__":
    read_file()
    # print_dict()
    get_shop_list_by_dishes(["Омлет", 'Фахитос'], 3)
