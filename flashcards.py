from __future__ import print_function
import argparse
import json
import os


def main():
    args = usage()
    if not args.file:
        print("Please provide a json file of questions and answers")
        return
    if not os.path.exists(args.file):
        print("file not found")
        return
    q_and_a = get_data(args.file)
    flash_cards(q_and_a)


def usage():
    """
    Gives the usage commands for this program
    :return the arguments:
    """
    parser = argparse.ArgumentParser(description="Command line flash card program")
    parser.add_argument("-f", "--file", help="Json file with questions and answers in it")
    return parser.parse_args()


def get_data(json_file):
    """
    Given a json file return a dictionary of the data inside
    The format of file should be { q1: a1, q2: a2 }
    :param json_file:
    :return dictionary of the json data:
    """
    with open(json_file, 'r') as q_a:
        q_a_data = json.loads(q_a.read())
    return q_a_data



def flash_cards(qa_dict):
    """
    Given a question and answer dictionary, converts that dictionary over to a list of tuples.
    Runs through that list printing out the question and then after keyboard input the answer.
    If the user says that they answered correctly then it removes that pair from the list.
    This continues until there aren't any pairs in the list
    :param qa_dict:
    """
    qa_list = qa_dict.items()
    i = 0
    while len(qa_list) > 0:
        question = qa_list[i][0]
        print(question)
        raw_input("\nPress any key for answer\n")
        answer = qa_list[i][1]
        print(answer)
        correct_answer = raw_input("\nDid you get the answer? (y)\n")
        if correct_answer is "y":
            qa_list.remove(qa_list[i])
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the command line output
        i += 1
        if i > len(qa_list) - 1:
            i = 0


if __name__ == '__main__':
    main()