url="/home/manjeetre/workspace/github.com/manjeetre/bookbot/book/frankenstein.txt"



def read():
    with open(url) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(read())

main()