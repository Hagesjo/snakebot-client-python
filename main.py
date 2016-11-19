from simplesnakebot import SimpleSnakebot
import argparse

def main():
    parser = argparse.ArgumentParser(description="Snakebot for cygni")
    parser.add_argument("-l", "--log", dest="loglevel",  help="Loglevel. DEBUG|INFO|WARNING|ERROR|CRITICAL", default="INFO")
    args = parser.parse_args()

    bot = SimpleSnakebot(args.loglevel)
    bot.connect()
    bot.register_player()

    while True:
        bot.receive()

if __name__=="__main__":
    main()
