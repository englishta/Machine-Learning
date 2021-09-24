# 浮動小数点定数の表記，x.yE(+|-)z　から実数に直すプログラム
# s = "12.35E+3"　を12350に変換する

def Error():
    print("Error")
    exit(0)

def Express(b, i, e, sign):
    if sign == '-':
        i*=-1
    num = b*10**(i-e)
    print(num)

s = str(input())
n = len(s) #文字列の長さ
idx = 0 #参照する文字の添え字番号
b = 0 #xyを整数にしたもの ex(3.45->345)
i = 0 # zの数
e = 0 # yの桁数

while idx<n and s[idx].isdigit():
    ch = s[idx]
    b = 10*b+(ord(ch)-ord('0'))
    idx+=1

if s[idx] != '.':
    Error()

idx+=1

while idx<n and s[idx].isdigit():
    ch = s[idx]
    b = 10*b+(ord(ch)-ord('0'))
    e+=1
    idx+=1

if s[idx] != 'E':
    Error()

idx+=1
if s[idx] == '+' or s[idx] == '-':
    sign = s[idx]
else:
    Error()

idx+=1
while idx<n and s[idx].isdigit():
    ch = s[idx]
    i = 10*i+(ord(ch)-ord('0'))
    idx+=1

Express(b, i, e, sign)
