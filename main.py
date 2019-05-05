import datetime
import vector_nba
from vector_nba import nba_api, console_out, console_in

def main():

    game_id = 0

    #List the games of the day
    games = nba_api.get_games(datetime.datetime.now())
    console_out.list_games(games)

    #Select the game to monitor
    game = 0
    if(len(games) > 1):
        game = console_in.select_game(len(games)) - 1
    game = games[game]
    game_id = game['GAME_ID']
    
    #List the teams within the chosen game
    console_out.list_teams(game)

    #Select the team to root for
    team = console_in.select_team()
    team_id = game['VISITOR_TEAM_ID'] if team == 'v' else game['HOME_TEAM_ID']

    #monitor_game(game_id, team_id)


    #check game start time
    #if game has not started ask to start
    #if start
        #respond with how to exit or 
        #monitor game
    #else exit

    #    

main()