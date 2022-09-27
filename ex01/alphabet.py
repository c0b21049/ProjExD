import random
from datetime import datetime
import time

num_of_alphabet = 26 #全アルファベット
num_of_subject_chars = 10 #対象文字数
num_of_defect_chras = 2 #欠損文字数
num_of_trials = 2 #最大繰り返し回数

def shutudai(alphabet):
    all_chars = random.sample(alphabet, num_of_subject_chars)
    print("対象文字:", end="")
    for c in sorted(all_chars):
        print(c, end=" ")
    print()
    
    abs_chars = random.sample(all_chars, num_of_defect_chras)
    print("表示文字:", end="")
    for c in all_chars:
        if c not in abs_chars:
            print(c, end=" ")
    print()
    return abs_chars

def kaito(seikai):
    num_of_ans = int(input("欠損文字はいくつあるでしょうか？:"))
    if num_of_ans == num_of_defect_chras:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
        for i in range(num_of_ans):
            ans = input(f"{i + 1}文字目を入力してください:")
            if ans in seikai:
                seikai.remove(ans)
            else:
                print("不正解です。またチャレンジしてください。")
                return False
        else:
            print("欠損文字も含めて完全正解です")
            return True
            
    else:
        print("不正解です。またチャレンジしてください")
        return False

if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(num_of_alphabet)]
    start = datetime.today()
    for _ in range(num_of_trials):
        abs_chars = shutudai(alphabet)
        ret = kaito(abs_chars)
        if ret:
            break
        else:
            print("-" * 20)
    end = datetime.today()
    fin_time = end - start
    print(f"経過時間:{fin_time}")
