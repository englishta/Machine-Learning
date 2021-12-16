# C 言語プログラム自動採点システム 
## 使い方

### コマンド
```math
cat test2.c | grep -v "#include" | grep -v "#define" | python3 pycparser.py > abstract_tree.txt
python3 make_tree.py > result.txt 
```