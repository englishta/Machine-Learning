import linecache
line_number = 1 #�s�ԍ�
lineIndex = -1
end = len(open('sample.c').readlines()) #�t�@�C���̍s��

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

def state3(s): #����
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
        ch = nextChar() #�P��Ԃ̋󔒕�����ǂݔ�΂�
    s+=ch
    if ch.isalpha(): #���O�̂Ƃ�
        return state2(s)
    elif ch.isdigit(): #�����̂Ƃ�
        return state3(s)
    elif ch == ',' or ch == ';': #��؂�L��
        return state4(s)
    else:
        return error()

def state2(s): #���O
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