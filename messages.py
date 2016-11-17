import constants
import platform
import json

def get_client_info():
    client_info = {}
    client_info_msg["type"] = constants.CLIENT_INFO
    client_info_msg["language"] = "python"
    client_info_msg["languageVersion"] = "2"
    client_info_msg["operatingSystem"] = platform.system()
    client_info_msg["operatingSystemVersion"] = platform.release()
    client_info_msg["clientVersion"] = "1.0"
    return json.dumps(client_info_msg)


def default_game_settings():
    game_settings = {}
    game_settings["maxNoofPlayers"] = 5
    game_settings["startSnakeLenth"] = 1
    game_settings["timeInMsPerTick"] = 250
    game_settings["obstaclesEnabled"] = True
    game_settings["foodEnabled"] = True
    game_settings["headToTailConsumes"] = True
    game_settings["tailConsumeGrows"] = False
    game_settings["addFoodLikelihood"] = 15
    game_settings["removeFoodLikelihood"] = 5
    game_settings["spontaneousGrowthEveryNWorldTick"] = 3
    game_settings["trainingGame"] = False
    game_settings["pointsPerLength"] = 1
    game_settings["pointsPerFood"] = 2
    game_settings["pointsPerCausedDeath"] = 5
    game_settings["pointsPerNibble"] = 10
    game_settings["noofRoundsTailProtectedAfterNibble"] = 3

    return game_settings

def register_move(next_move, incoming_data):
    register_move_msg = {}
    register_move_msg["type"] = constants.REGISTER_MOVE
    register_move_msg["direction"] = next_move
    register_move_msg["gameTick"] = incoming_data["gameTick"]
    register_move_msg["receivingPlayerId"] = incoming_data["receivingPlayerId"]
    register_move_msg["gameId"] = incoming_data["gameId"]
    
    return json.dumps(register_move_msg)

def start_game():
    start_game_msg = {}
    start_game_msg["type"] = constants.START_GAME

    return json.dumps(start_game_msg)

def register_player(name):
    reg_msg = {}
    reg_msg["type"] = constants.REGISTER_PLAYER_MESSAGE_TYPE
    reg_msg["playerName"] = name
    reg_msg["gameSettings"] = default_game_settings()

    return json.dumps(reg_msg)
