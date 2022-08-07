# from puzzle_question import PuzzleQuestion
from crossword_puzzle_generator import *

max_word_length = 10

def getData():
    with open("words_for_testings.txt", encoding="utf-8") as f:
        temp = list(f.read().upper().splitlines())

    puzzle_questions_list = []
    i = 1
    for word in temp:
        if len(word) > max_word_length:
            continue
        puzzle_question = PuzzleQuestion(i, "question " + str(i), word)
        puzzle_questions_list.append(puzzle_question)
        i += 1
    sorted_list = sorted(puzzle_questions_list, key=lambda x: len(x.word_answer), reverse=True)
    return sorted_list

def eliminate_used_questions_from_data(data, ids):
    new_question_list = []
    for question in data:
        if question.id in ids:
            continue
        new_question_list.append(question)
    return new_question_list


data = getData()

i = 1
max_false_try = 10
false_try_count = 0
while True:
    if false_try_count == max_false_try:
        break

    cwpg = CrossWordPuzzleGenerator(data, 10, 50)
    flag = cwpg.generate()
    if flag == False:
        false_try_count += 1
        continue
    
    false_try_count = 0
    print("puzzle " + str(i))
    print(cwpg.grid)
    data = eliminate_used_questions_from_data(data, cwpg.fitted_ids)
    i += 1
