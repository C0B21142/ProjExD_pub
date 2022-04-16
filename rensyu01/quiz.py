import random

NUM_OF_QUES = 3

def shutudai():
    qa = random.choice(qa_dict_list)
    print(q["q"])
    return qa["a"]

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
    qa_dict_list = [{"q": "サザエの旦那の名前は？", "a": ["マスオ", "ますお"]}, {"q": "カツオの妹の名前は？", "a": ["ワカメ", "わかめ"]}, {"q": "タラオはカツオから見てどんな関係？", "a": ["甥", "おい", "甥っ子", "おいっこ"]}]
    main()