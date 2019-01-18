import sys
import MeCab

#参考：https://qiita.com/menon/items/2b5ad487a98882289567
class Word:
    string:str
    np:bool

#形態素解析してリストに入れる
def mecab_list(text):
    tagger = MeCab.Tagger("-Ochasen")   #パーサ設定
    tagger.parse('')    #unicodeDecodeError回避
    node = tagger.parseToNode(text) #nodeにsurface(単語)feature(品詞情報)を持つ解析結果を代入
    word_class = []
    #品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
    while node:
        word = node.surface
        wclass = node.feature.split(',')
        if wclass[0] != u'BOS/EOS':
            if wclass[6] == None:  #原型ないとき
                word_class.append((word,wclass[0],wclass[1],wclass[2],""))
            else:                   #単語、品詞、品詞細分類1,2,原型 の順に格納
                word_class.append((word,wclass[0],wclass[1],wclass[2],wclass[6]))
        node = node.next
    return word_class

point=0
data=[]
#日本語評価極性辞書（用言編）ver.1.0
f=open(r'wago.txt','r',encoding="utf-8_sig")
lines1=f.readlines()    #一行毎にファイル終端まで
f.close()
print("np判定用データの読み込み(用言)")
# lines1: リスト。要素は1行の文字列データ
for i,line in enumerate(lines1):
    lines1[i] = line.replace('\r','')
    lines1[i] = line.replace('\n','')
    tmp = line.split()
    tmp.pop(0)
    if('ポジ' in line):   #検索(あるならtrue)
        bl=1
    else:
        bl=-1
    data.append([bl,tmp[0]])
    #print(data[i])

#日本語評価極性辞書（名詞編）ver.1.0
f=open(r'pn.csv','r',encoding="utf-8_sig")
lines2=f.readlines()    #一行毎にファイル終端まで
f.close()
print("np判定用データの読み込み(名詞)")
for i,line in enumerate(lines2):
    lines2[i] = line.replace('\r','')
    lines2[i] = line.replace('\n','')
    tmp = line.split()
    if(tmp[1]=='p'):
        #print('p:')
        #print(tmp)
        bl=1
    elif(tmp[1]=='e'):
        #print('e:')
        #print(tmp)
        bl=0
    elif(tmp[1]=='n'):
        #print('n:')
        #print(tmp)
        bl=-1
    else:
        #print('その他：')
        #print(tmp)
        bl=0
    data.append([bl,tmp[0]])
    #print(data[i])


print("\n解析する文章を入力>>")
input=input()
lst=mecab_list(input)
print(lst)
print("ーーーー分解ーーーー")
for i in lst:
    print(i[0])
print("ーーーー照合ーーーー")
for i,item in enumerate(lst):
    #print(lst[i][4])
    for j,word in enumerate(data):
        if(lst[i][4]==data[j][1]):
            point+=data[j][0]
            print(data[j])
            break   #被りを防ぐ

print('\nネガポジ度')
print(point)
if(point>0):
    print('ポジティブな文章です')
elif(point<0):
    print('ネガティブな文章です')
else:
    print('ネガポジどちらともいえません')