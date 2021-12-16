import linecache

text = ""
end = len(open('test.c').readlines()) #ファイルの行数
for i in range(1, end+1): text+= str(linecache.getline('test.c', int(i)))
text.replace('\n', '')
id = -1

def nextChar():
    global id
    id+=1
    if id>=len(text):
        print("end of file")
        exit()
    else:
        return text[id]
 
def error():
    return "Error"

def state5():
    global id
    id-=1

def state3(s): #数字
    ch = nextChar()
    if ch.isdigit() or ch == '.':
        s+=ch
        return state3(s)
    else:
        state5()
        return s

def state4(s):
    ch = nextChar()
    return s

def Next_Token(s=""):
    ch = nextChar()
    while ch == ' ':
        ch = nextChar() #単語間の空白文字を読み飛ばす
    s+=ch
    if ch.isalpha() or ch == '#' or ch == '%': #名前のとき
        return state2(s)
    elif ch.isdigit(): #数字のとき
        return state3(s)
    elif ch == ',' or ch == ';' or ch == '{' or ch == '}' or ch == '[' or ch == ']' or ch == "'" or ch == '"':
        return state4(s)
    else:
        return error()

def state2(s): #名前
    ch = nextChar()
    if ch.isalpha() or ch.isdigit() or ch == '.' or ch=='_':
        s+=ch
        return state2(s)
    else:
        state5()
        return s

if __name__ == '__main__':
    while True:
        ans = Next_Token()
        if ans == "Error": continue
        print(ans)
