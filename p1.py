def load_lines(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
    return lines

def convert_lines_to_dicts(filepath):
    lines = load_lines(filepath)
    dictionaries = []

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces
        if line:
            key_value_pairs = line.split(':')
            dictionary = {}
            for pair in key_value_pairs:
                key, value = pair.split('=')
                dictionary[key.strip()] = value.strip()
            dictionaries.append(dictionary)

    return dictionaries
file_path = "polldata.fps"
dict_list = convert_lines_to_dicts(file_path)

for dictionary in dict_list:
    print(dictionary)