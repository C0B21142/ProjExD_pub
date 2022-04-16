import random

NUM_OF_QUES = 3

def shutudai():
    q, a_list = random.choice(list(qa_dict.items()))
    print(q)
    return a_list

def kaito(a_list):
    kaito = input()
    if kaito in a_list:
        print("正解")
    else:
        print("不正解")

def main():
    a_list = shutudai()
    kaito(a_list)

if __name__ == "__main__":
    qa_dict = {"サザエの旦那の名前は？": ["マスオ", "ますお"], "カツオの妹の名前は？": ["ワカメ", "わかめ"], "タラオはカツオから見てどんな関係？": ["甥", "おい", "甥っ子", "おいっこ"]}
    main()