from module.state import State
from random import randrange


player_name = ""
other_name = ""

def run_turn(turn):
    print("What would you like to do? (Turn: "+str(turn)+")")
    print("1. Host Event")
    print("Quit")
    return input()


def debate(debate_num):
    hosts = []
    names = open("data\hosts.txt")
    for name in names:
        hosts.append(name.strip())
    host_name = hosts[randrange(len(hosts))]
    print("Welcome to debat number " + str(int(debate_num)))
    input()
    print("My name is " + host_name + ", and I will be hosting tonights discussion")
    print("The candidates are "+player_name+" and "+other_name)
    input()


def election_sim():
    global player_name
    global other_name
    print("WELCOME TO ELECTION SIMULATOR: AMERICAN STYLE")
    player_name = input("What is your name: ")
    other_name = input("Who are you faceing off against: ")
    inp = None
    turn = 1
    while inp != quit:
        if turn % 10 == 0:
            debate(turn / 10)
            turn += 1
        else:
            inp = run_turn(turn)
            turn += 1


if __name__ == "__main__":
    election_sim()
