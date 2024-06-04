import os,sys,re

def finder(regex):
    txt_files = [file for file in os.listdir() if file.endswith(".txt")]

    for file_name in txt_files:
        with open(file_name, "r") as file:
            print(f"File: {file_name}")
            for line in file:
                if re.search(regex, line):
                    print(line.strip())

if len(sys.argv) < 2:
    print("python3 finder.py 正規表現")
    sys.exit(1)

regex = sys.argv[1]

finder(regex)

