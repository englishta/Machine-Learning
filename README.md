# C 言語プログラム自動採点システム 
## 使い方

### コマンド
```math
cat test.c | grep -v "#include" | grep -v "#define" | python3 cparser.py > abstract_tree.txt
```
```math
python3 make_tree.py < detail.txt > result.txt
```