def skip_header(f):
    line = f.readline()
    while line.startswith("#"):
        line = f.readline()
    return line


def process_file(f):
    line = skip_header(f).strip()
    print(line)
    for line in f:
        if line.startswith("-") or line.startswith("#"):
            line = f.readline()
        line = line.strip()
        print(line)


input_file = open("泰戈尔的诗.txt", 'r')
process_file(input_file)
input_file.close()
