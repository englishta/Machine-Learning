# ���������_�萔�̕\�L�Cx.yE(+|-)z�@��������ɒ����v���O����
# s = "12.35E+3"�@��12350�ɕϊ�����

def Error():
    print("Error")
    exit(0)

def Express(b, i, e, sign):
    if sign == '-':
        i*=-1
    num = b*10**(i-e)
    print(num)

s = str(input())
n = len(s) #������̒���
idx = 0 #�Q�Ƃ��镶���̓Y�����ԍ�
b = 0 #xy�𐮐��ɂ������� ex(3.45->345)
i = 0 # z�̐�
e = 0 # y�̌���

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
