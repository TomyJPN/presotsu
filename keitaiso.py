import sys
import MeCab

m = MeCab.Tagger ("-Ochasen")
print(m.parse ("本日はいい天気ですね"))