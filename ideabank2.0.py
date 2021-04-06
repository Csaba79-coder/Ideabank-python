import sys
from signal import signal, SIGINT
from sys import exit


def read_idea_from_file():
    with open("idea-list.txt", "r") as text_file:
        idea_list = text_file.readlines()
    return idea_list


def list_ideas(idea_list):
    for index in range(len(idea_list)):
        print(f"{index + 1}. {idea_list[index]}")


def get_idea():
    idea = input("What's your new idea? ")
    return idea


def write_ideas_to_file(idea_list):
    with open("idea-list.txt", "w") as idea_file:
        for element in idea_list:
            idea_file.write(element)


ideas = read_idea_from_file()

if len(sys.argv) == 1:
    while True:
        idea = get_idea()
        ideas.append(idea + "\n")
        write_ideas_to_file(ideas)
        list_ideas(ideas)
elif sys.argv[1] == "--list":
    list_ideas(ideas)
elif sys.argv[1] == "--delete":
    if sys.argv[2]:
        a = 0
        for a in sys.argv[2]:
            a = int(a) - 1
            with open("idea-list.txt", "r") as text_file:
                lines = text_file.readlines()
                del lines[a]
                write_ideas_to_file(lines)


def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)