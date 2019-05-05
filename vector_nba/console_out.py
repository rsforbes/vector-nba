import datetime
from vector_nba import nba_api

def list_games(games):
    
    count = 0
    if len(games) > 0:
        print('\nAvailable games:')
    
    for game in games:
        count += 1
        print(f"\t({count}) {game['VISITOR_TEAM_NAME']} @ {game['HOME_TEAM_NAME']} - ({game['GAME_STATUS_TEXT']})")
    
    if count == 0:
        print("No games are available today.")
        exit

def list_teams(game):
    print("\nChoose a Team:")
    print(f"\t(v) {game['VISITOR_TEAM_NAME']}")
    print(f"\t(h) {game['HOME_TEAM_NAME']}")