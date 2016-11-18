from websocket import create_connection

import config
import constants
import json
import logging
import messages
import utils

class BaseSnakebot(object):
    def __init__(self, loglevel):
        logging.basicConfig(format="%(asctime)s %(levelname)s  %(message)s", level=getattr(logging, loglevel.upper()))
        self.server = config.SERVER_NAME
        self.port = config.SERVER_PORT
        self.autostart = config.AUTO_START_GAME
        self.name = config.SNAKE_NAME
        self.mode = config.GAME_MODE
        self.sock = None
        self.commands = {
            constants.GAME_ENDED : self.on_game_ended,
            constants.TOURNAMENT_ENDED : self.on_tournament_ended,
            constants.MAP_UPDATE : self.on_map_update,
            constants.SNAKE_DEAD : self.on_snake_dead,
            constants.GAME_STARTING : self.on_game_starting,
            constants.PLAYER_REGISTERED : self.on_player_registered,
            constants.INVALID_PLAYER_NAME : self.on_invalid_player_name,
            constants.HEART_BEAT_RESPONSE : self.on_heart_beat_response,
            constants.GAME_LINK_EVENT : self.on_game_link_event,
            constants.GAME_RESULT_EVENT : self.on_game_result_event
        }


    def connect(self):
        logging.info("Connecting to {}:{}/{}".format(self.server, self.port, self.mode))
        self.sock = create_connection("ws://{}:{}/{}".format(self.server, self.port, self.mode))
        logging.info("Connected to server")

    def send(self, msg):
        logging.debug("Sending {} to server".format(msg))
        self.sock.send(msg)

    def receive(self):
        received = self.sock.recv()
        parsed_data = json.loads(received)
        logging.debug("\nReceived message: {}\n".format(parsed_data))
        # Execute command if exists
        try:
            self.commands[parsed_data["type"]](parsed_data)
        except KeyError, e:
            logging.warning("Couldn't find command for received game event: {}".format(parsed_data["type"]))

    def register_player(self):
        logging.info("Registering player to game")
        self.send(messages.register_player(self.name))

    def on_game_ended(self, incoming_data):
        logging.info("Game has ended")

        if self.mode == "training":
            exit()

    def on_tournament_ended(self):
        logging.info("Tournament has ended, exiting")
        exit()

    def on_map_update(self, incoming_data):
        raise NotImplementedError

    def on_snake_dead(self, incoming_data):
        logging.info("A snake {} died by {}".format(incoming_data["playerId"], incoming_data["deathReason"]))

    def on_game_starting(self, incoming_data):
        pass

    def on_player_registered(self, incoming_data):
        logging.info("Player registered.\n\tGame settings:\n{}".format(utils.logging_format(incoming_data)
))
        game_mode = incoming_data["gameMode"]

        if game_mode == "TRAINING":
            self.send(messages.start_game())
            logging.info("Requesting a game start")


    def on_invalid_player_name(self, incoming_data):
        logging.info("Invalid player name. Please configure a valid player name")
        exit()

    def on_heart_beat_response(self, incoming_data):
        pass

    def on_game_link_event(self, incoming_data):
        logging.info("The game can be viewed at: {}".format(incoming_data["url"]))

    def on_game_result_event(self, incoming_data):
        rankdata = sorted(incoming_data["playerRanks"], key=lambda x: x['rank'])
        for data in rankdata:
            logging.info("{}. {} pts {} ({})".format(
                data["rank"], 
                data["points"], 
                data["playerName"], 
                "alive" if data["alive"] else "dead"
                )
            )
