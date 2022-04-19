import random

def shutudai():
    qa = random.choice(qa_list)
    print("じゃじゃん：", qa["q"])
    return qa["a"]

def kaito(a_lst):
    kai = input("答えを入力してください：")
    print("入力した答えは：", kai)
    if kai in a_lst:
        print("正解でーす！！！！")
    else:
        print("出直してこい")


if __name__ == "__main__":
    qa_list = [{"q": "サザエさんの旦那の名前は？", "a": ["ますお", "マスオ"]}, {"q": "カツオの妹の名前は？", "a": ["わかめ", "ワカメ"]}, {"q": "タラオはカツオから見てどんな関係？", "a": ["甥", "おい", "おいっこ", "甥っ子"]}]
    a_list = shutudai()
    kaito(a_list)