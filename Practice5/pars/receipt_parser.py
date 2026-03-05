import re
import json
#1
text = open("raw.txt","r", encoding="utf-8").read()
text = text.replace('\n', ' ')
cost = (re.findall(r"Стоимость\s\d+,\d{2}", text))
#2
text2 = open("raw.txt","r", encoding="utf-8").read()
names=re.findall(r"^\d+\.\n(.+)$", text2, re.MULTILINE)
#3
text3 = open("raw.txt","r", encoding="utf-8").read()
text3 = text.replace("\n", " ")
OVERall = (re.findall(r"ИТОГО:\s*\d{2}\s\d{3}[,]\d{2}", text3))
#4
text4 = open("raw.txt","r", encoding="utf-8").read()
date = re.findall(r"Время:\s\d{2}[.]\d{2}[.]\d{4}\s\d{2}[:]\d{2}[:]\d{2}", text4, re.MULTILINE)
#5
text5 = open("raw.txt","r", encoding="utf-8").read()
sposoboplaty = re.findall(r"Банковская карта:", text5, re.MULTILINE)
#6
dict1 = {
    "Cost": cost,
    "Names": names,
    "Overall": OVERall,
    "Date": date,
    "Payment method": sposoboplaty
}
print(json.dumps(dict1, ensure_ascii=False, indent=2))