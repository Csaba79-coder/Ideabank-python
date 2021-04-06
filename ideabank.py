# Put your code here
from signal import signal, SIGINT
from sys import exit


def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


def reading_txt():
    file = open("ideas.txt", "r", encoding = "utf-8")

    sor = file.readline()

    file.close()


def writing_txt():
    index = 1
    with open ("ideas.txt", "a", encoding = "utf-8") as file:
        ujsor = input("What is your new idea? ")
        file.write(str(index) +". " + ujsor + "\n")


#    if ujsor in ideas.txt:
  #          file.append(ujsor)
        print(ujsor)
# with open ("ideas.txt","r", encoding = "utf-8") as file:


if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

    while True:
        # Do nothing and hog CPU forever until SIGINT received.
        ujsor = input("What is your new idea? ")