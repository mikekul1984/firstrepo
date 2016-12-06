test_list = [{'a': '1', 'b': '4'}, {'a': '2', 'b': '6'}, {'a': '1', 'b': '8'},{'a': '2', 'b': '89'}]

temp_dict = {}

for _i in test_list:
    temp_dict[_i['a']] = _i

print(temp_dict.values())
