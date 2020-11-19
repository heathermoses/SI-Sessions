filename = ""

def file_writer(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(line)

def print_value(dictionary):
    for key in dictionary:
        print(dictionary[key])