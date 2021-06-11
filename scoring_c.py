import sys
import os
import pandas as pd
import re

def search(file_name):
    f = open(file_name, "r", encoding='UTF-8')
    # print(file_name)
    data = f.read()
    list = data.split('\n')
    rev = []
    Score = 100
    coment_out = False

    for i in range(len(list)):
        if list[i].count("　"): 
            rev.append(str(i+1)+"行目:全角スペース")
            Score-=10

    for i in range(len(list)):
        list[i] = re.sub(r'/\*.*\*/', "", list[i]) # /*～*/を削除
        list[i] = re.sub(r'//.*', "", list[i]) # //～を削除
        s = re.sub(r'/\*.*', "", list[i]) #/*～を削除
        s = re.sub(r'.*\*/', "", s) #～*/を削除
        s = s.rstrip().lstrip() # 先頭と末尾の空白文字を削除
        s = re.sub(r"(int|double|void)\s.*\((int|double|void)*.*\)", "Func", s) #関数宣言を"Func"で置き換える
        if s[:2] == "if" or s[:3] == "for":
            s = s.replace(" ", "")
            s = re.sub(r"if\s*\(.*\)\s*[^\{;]+", "If() do", s)
            s = re.sub(r"for\s*\(.*\)\s*[^\{;]+", "For() do", s)

        end = len(s)-1
        # print(s)
        if list[i].count("*/"): coment_out = False
        if s != "" and s[:8] != "#include" and not coment_out:
            if s[end] != ';' and s[end] !='{' and s[end] !='}' and s[:3] != "for" and s[:2] != "if" and s[:4]!="Func":
                rev.append(str(i+1)+"行目：セミコロンなし")
                Score-=10
        if list[i].count("/*"): coment_out = True

    f.close()
    Review_string = ""
    for e in rev:
        Review_string+=e+', '
    return Score, Review_string


def Main():
    data = {'number' : [x for x in range(1, 11)], #1～10の学籍番号
            'score' : [0]*10,
            'review' : [""]*10}
    data_frame = pd.DataFrame(data)

    for file_number in range(1, 11): #1.c～10.cまで
        Sc, Rev = search("./c_code/"+str(file_number)+".c")
        data_frame["review"][file_number-1] = Rev 
        data_frame["score"][file_number-1] = Sc
        
    print(data_frame)
    data_frame.to_csv("./data.csv", index = False, encoding='shift-jis') #csvファイルに書き込み


if __name__ == "__main__":
  Main()
