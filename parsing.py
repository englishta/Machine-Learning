# 再帰降下型構文解析
# https://dai1741.github.io/maximum-algo-2012/docs/parsing/

# BNF
# expr->加減式，term->乗除式，factor->(式)，number->数
# expr := <term> | <expr> + <term> | <expr> - <term>
# term := <factor> | <term> * <factor> | <term> / <factor>
# factor := (<expr>) | <number>
# number := [0 - 9]*
import re

i = 0

def expr(s):
  global i
  val = term(s)
  while i<len(s) and (s[i] == '+' or s[i] == '-'):
    op = s[i]
    i+=1
    val2 = term(s)
    if op == '+': val += val2
    else: val -= val2

  return val
 

def term(s):
  global i
  val = factor(s)
  while i<len(s) and (s[i] == '*' or s[i] == '/'):
    op = s[i]
    i+=1
    val2 = factor(s)
    if op == '*': val *= val2
    else: val //= val2
  return val
    

def factor(s):
  global i
  if s[i].isdigit():
    return number(s)
  i+=1 # (を読み飛ばす
  ret = expr(s)
  i+=1 # )を読み飛ばす
  return ret


def number(s):
  global i
  n = int(s[i])
  i+=1
  while i<len(s) and s[i].isdigit():
    n = n*10 + int(s[i])
    i+=1
  return n

def Calculate(st):
  global i
  i=0
  st = st.replace(" ", "")
  return expr(st)


# --------------<is_str func>--------
def is_str(v):
    return type(v) is str

# --------------<deformate func>--------
def search_var(Str, t, d):
    q = len(t)
    n = len(Str)
    S = ""
    i = 0
    while i < n:
        if i<=n-q and Str[i:i+q] == t:
            if (i+q<n and Str[i+q] == t[0]) or (i-1>=0 and Str[i-1] == t[q-1]):
                S+=Str[i]
                i+=1
            else:
                S+=str(d[t])
                i+=q
        else:
            S+=Str[i]
            i+=1
    return S    

def deformate(Str, d):
    for var in d.keys():
        Str = search_var(Str, var, d)
    return Str

def func(String, d):
    for Str in String.split(","):
        var = ""
        Str = Str.replace(" ", "").replace(";", "")
        Str = re.sub(r"(int|double)", "", Str)
        for e in Str:
            if e == '=': break
            var+=e
        if not Str.count("="):
            d[Str] = "yet"
            continue
        
        Str= re.sub(r".+=", '', Str)
        Str = deformate(Str, d)

        if bool(re.search(r'[a-zA-Z_]', Str)):
            Error_word = re.sub(r'[0-9\(\)\*\+\-\/.]', "", Str)
            print("宣言されていない変数名が使われています -->", Error_word)
            for e in d.keys():
                if e.count(Error_word):
                    print(Error_word, "ではなく", e, "ではありませんか？")
        else:
            Num = Calculate(Str)
            print(var, "<--", Str,"=", Num)
            d[var] = Num



