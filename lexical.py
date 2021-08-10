import linecache
line_number = 1 #行番号
lineIndex = -1
end = len(open('sample.c').readlines()) #ファイルの行数

def nextChar():
    global line_number
    global lineIndex

    line = linecache.getline('sample.c', int(line_number))
    if lineIndex == -1:
        if line_number<=end:
            lineIndex = 0
        else:
            print("end of file")
            exit()
    ch = line[lineIndex]
    lineIndex+=1
    if ch == '\n':
        lineIndex = -1
        line_number+=1
        return ' '
    return ch

def error():
    return "Error"

def state5():
    global lineIndex
    lineIndex-=1

def state3(s): #数字
    ch = nextChar()
    if ch.isdigit():
        s+=ch
        return state3(s)
    else:
        state5()
        return s

def state4(s):
    ch = nextChar()
    if ch == ',' or ch == ';':
        s+=ch
        return state4(s)
    else:
        state5()
        return s

def state1(s):
    ch = nextChar()
    while ch == ' ':
        ch = nextChar() #単語間の空白文字を読み飛ばす
    s+=ch
    if ch.isalpha(): #名前のとき
        return state2(s)
    elif ch.isdigit(): #数字のとき
        return state3(s)
    elif ch == ',' or ch == ';': #区切り記号
        return state4(s)
    else:
        return error()

def state2(s): #名前
    ch = nextChar()
    if ch.isalpha() or ch.isdigit():
        s+=ch
        return state2(s)
    else:
        state5()
        return s

if __name__ == '__main__':
    while True:
        ans = state1("")
        if ans == "Error": continue
        print(ans)