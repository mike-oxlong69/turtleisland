# Course: CS 30
# Period: 3
# Date created: November 23rd, 2021
# Date modified: November 23rd, 2021
# Name: Anas Munshi
# Description: Map for the game
try:
    import sys
except ModuleNotFoundError:
    print("Error, import failed")
    print("Game ended")
    sys.exit()


game_map = ('''
   ______________________________Exit_________________________________________________
  |  _____________               |   |________________________________________________|
  | |             |______________|                 Main Hall              |        |  |
  | |  Security   |              |____________/\_____________________     |        |  |
  | |    Room     |                                                 |     |        |  |
  | |             |                                                 |     |        |  |
  | |             |                                                 |     |        |  |
  | |_____/\______|                                                 |     |        |  |
  | |             |                                          _______|     |________|  |
  | |             |                                         |                      |  |
  | |   Lounge    |__________________________               |                      |  |
  | |                                        |              |                      |  |
  | |___________/\_____________              |              |                      |  | 
  | |                          |                            |                      |  |
  | |      Kitchen             |                            |     Starting Room    |  |
  | |__________________________|____________________________|                      |  |
  |                                                         |                      |  |
  |                                                         |                      |  |
  |            Outdoor Garden                               |______________________|  |
  |                                                                                   |
  |___________________________________________________________________________________|

''')


def print_map():
    '''Prints world map'''
    print(game_map)
