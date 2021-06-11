from parsing import Calculate
import re

s = "int a = (8*4)/(3+5);"
s = s.replace(" ", "")
s = s.replace(";", "")
s = re.sub(r"(int|double).+=", '', s)
print(Calculate(s))
	