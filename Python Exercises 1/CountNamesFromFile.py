def read_file():
    with open (".\Txt Files\listofnames.txt" , "r") as names_file:
        name = names_file.readline()
        while(name):
            print (name)
            name = names_file.readline()

def count_names():
    name_count = {}
    with open(".\Txt Files\listofnames.txt", "r") as names_file:
        name = names_file.readline().strip()
        while(name):
            if name not in name_count:
                name_count[name] = 1
            else:
                name_count[name] += 1
            name = names_file.readline().strip()
    print (name_count)

def main():
    read_file()
    count_names()


if __name__ == "__main__":
    main()