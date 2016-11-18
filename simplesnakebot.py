from basesnakebot import BaseSnakebot

import logging
import messages

class SimpleSnakebot(BaseSnakebot):

    def on_map_update(self, incoming_data):
        # Directions are UP, DOWN, LEFT, RIGHT
        # This is the startpoint of your algorithm.

        direction = "DOWN";
        logging.info("Snake is making move {} at worldtick: {}".format(direction, incoming_data["map"]["worldTick"]))
        self.send(messages.register_move(direction, incoming_data))

