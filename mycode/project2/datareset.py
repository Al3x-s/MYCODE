import html
import random
def une(word):
    return html.unescape(word)

def restructure(api):
    new_struct = []
    for i in api["results"]:
        new_dic = {}
        new_arr = []
        new_arr.append(une(i["correct_answer"]))
        correct_answer = une(i["correct_answer"])
        question = une(i["question"])
        for choice in i["incorrect_answers"]:
            new_arr.append(une(choice))
        random.shuffle(new_arr)
        new_dic["question"] = question
        new_dic["options"] = new_arr
        new_dic["correct_answer"] = correct_answer
        new_struct.append(new_dic)
    return(new_struct)

def calc_score(questions, answer_list):
    score = 0
    for i in range(len(questions)):
        if answer_list[i] == questions[i]["correct_answer"]:
            score += 1
    return score
