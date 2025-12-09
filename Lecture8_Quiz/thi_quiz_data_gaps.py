# -*- co    ding: utf-8 -*-
"""
thi_quiz_data.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""

import random

def load_questions_from_file(path_to_file):
    """
    Loads a txt file that contains questions in the format from the lecture.

    Args:
        path to file: String that contains the path to the txt file

    Returns:
        A list that contains all questions from the txt file in the following format:
        [(question, answer1, answer2, answer3, answer4, correct_index), 
        ..., 
        (question, answer1, answer2, answer3, answer4, correct_index)]
    """

    file = open(path_to_file, 'r')
    lines = file.readlines()
    file.close()

    # Number of questions is defined in the first line.
    num_overall_questions = int(lines[0])

    all_questions = list()
    
    # each question consists of 5 lines 
    for i in range(1, (num_overall_questions)*5, 5):
        question_text = lines[i]
        all_answers = [lines[i+j] for j in range(1, 5)]
        
        # search answers for CORRECT: tag and extract the question
        # TODO get correct answer
                
        # TODO assemble question tuple  

    return all_questions


def get_random_question_from_complete_list(all_questions, current_question=None):
    """
    Draws one question from a list and place it back to the pool.

    Args:
        all_questions: list that contains all questions
        current_question: the currently displayed question - if none ignore 

    Returns:
        One single question in the following format: 
        (question, answer1, answer2, answer3, answer4, correct_index)
    """
    # TODO!!
    pass
 