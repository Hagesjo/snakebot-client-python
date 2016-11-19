# snakebot-client-python 
Snakebot python client for cygni:s competition (https://cygni.se/snake/)

# Prerequisities
pip install -r requirements.txt

# Run
python main.py [--log DEBUG|INFO|WARNING|ERROR|CRITICAL]

# Implementing your algorithm
* Change config.py to your liking
* Start at simplesnakeclient.py. Also, take a look at all the utility functions
available in utils.py, they can be helpful.
* For each game tick, the client has parsed the map into `current_map` for you. To list
the available data in the map, use `current_map.data_available()`
