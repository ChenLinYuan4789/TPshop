import yaml

def dict_yml_file(file_name, key):
    with open("./data/" + file_name + ".yml", "r", encoding="utf-8")as f:
        data = yaml.safe_load(f)[key]
        data_list = []
        for i in data.values():
            data_list.append(i)
        return data_list


def list_yml_file(file_name):
    with open("./data/" + file_name + ".yml", "r", encoding="utf-8")as f:
        data = yaml.safe_load(f)
        return data



# def main():
#     res = dict_yml_file("search", "test_search")
#     list = []
#     for i in res.values():
#         # print(i)
#         list.append(i)
#     print(list)
    # print(res.values())

if __name__ == '__main__':
    # main("test_login")
    # res = yml_file("search", "test_search")
    # list = []
    # for i in res.values():
    #     print(i)
    # print(res)
    # print(res)
    res = list_yml_file("search")
    print(res)