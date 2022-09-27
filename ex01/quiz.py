import random
def shutudai(qa_list):
    qa= random.choice(qa_lst)
    print("問題:"+qa["q"])
    return qa["a"]

def kaito(ans_lst):
    ans = input("答えるんだ")
    if ans in ans_lst:
        print("正解！！！")
    else:
        print("出直してこい")

if _name_ == "_main_":
    qa_lst = [
    {"q":"サザエさんの旦那の名前は？","a":["マスオ", "ますお"]},
    {"q":"カツオの妹の名前は？","a":["ワカメ", "わかめ"]},
    {"q":"タラオはカツオから見てどんな関係？","a":["甥", "おい", "甥っ子", "おいっこ"]},
    ]
    ans_lst = shutudai(qa_lst)
    kaito(ans_lst)