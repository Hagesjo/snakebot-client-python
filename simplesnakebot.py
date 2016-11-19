from basesnakebot import BaseSnakebot
from collections import namedtuple
from gamemap import GameMap
from random import randint

import logging
import messages

# Utils are useful functions to help you with the implementation of the AI
import utils

class SimpleSnakebot(BaseSnakebot):

    def on_map_update(self, incoming_data):
        # Directions are UP, DOWN, LEFT, RIGHT
        current_map = GameMap(**incoming_data["map"])

        direction = "DOWN";
        logging.info("Snake is making move {} at worldtick: {}".format(direction, current_map.worldTick))
        self.send(messages.register_move(direction, incoming_data))
