import datetime
from nba_api.stats.endpoints import Scoreboard
from nba_api.stats.library.parameters import LeagueID
from nba_api.stats.library.data import teams

def get_teams():
    return dict((team[0],team[5]) for team in teams)

def get_games(date):
    teams = get_teams()

    gamefinder = Scoreboard(league_id=LeagueID.nba,
                                day_offset=0,
                                game_date=date)

    games_dict = gamefinder.get_normalized_dict()
    for game in games_dict['GameHeader']:
        game['HOME_TEAM_NAME'] = teams[game['HOME_TEAM_ID']]
        game['VISITOR_TEAM_NAME'] = teams[game['VISITOR_TEAM_ID']]

    return games_dict['GameHeader']