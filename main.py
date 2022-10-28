url="/home/manjeetre/workspace/github.com/manjeetre/bookbot/book/frankenstein.txt"



def read(url):
    with open(url) as f:
        file_contents = f.read()
    return file_contents
def count_word(url):
    str=read(url)
    words=str.split()
    count=len(words)
    return count
# def count_letter(str):
#     count_l={}
#     arr=['a','b','c','d','e','f','g','h','i','j','h','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
#     text_raw=str.lower()
#     text=list(text_raw)
#     for a in arr:
#         count=0
#         for t in text:
#             if a==t:
#                 count+=1
#         count_l[a]=count
#     return count_l
def count_letter(str):
    count_i={}
    text_raw=str.lower()
    for text in text_raw:
        if text in count_i:
            count_i[text]+=1
        else:
            count_i[text]=1

    return count_i
def lettr_cprint(dics):
    arr=[]
    for d in dics:
        if d.isalpha():
            arr.append(dics[d])
    arr.sort()
    print(arr)
    for i in range(len(arr)-1,-1,-1):
        for d in dics:
            if arr[i]==dics[d]:
                print(f"The {d} character was found {dics[d]} times")

def main():
    text = read(url)
    print(text)
    count=count_word(url)
    print(count)
    count_ltr = count_letter(text)
    lettr_cprint(count_ltr)

main()