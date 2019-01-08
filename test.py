import sys
import MeCab

f=open(r'wago.txt','r',encoding="utf-8_sig")
lines2=f.readlines()    #一行毎にファイル終端まで
f.close()
# lines2: リスト。要素は1行の文字列データ
for line in lines2:
    print(line),
print

#m = MeCab.Tagger ("-Ochasen")
#print(m.parse ("どこしか昨日まずこの意味方という点の時を取らなけれで。もし生涯を批評者ぞもしそんな話たますかもでいうていうをはぼんやり思いうなから、こうにはもつませですなな。女にするうのははなはだ事実の現にませですまし。"))