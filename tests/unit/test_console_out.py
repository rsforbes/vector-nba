import pytest
import vector_nba
from vector_nba import console_out

games_none = []
def test_list_games_none(capsys):

    console_out.list_games(games_none)
    captured = capsys.readouterr()

    assert captured.out == "No games are available today.\n"


games_single = [{'GAME_DATE_EST': '2019-05-04T00:00:00', 'GAME_SEQUENCE': 1, 'GAME_ID': '0041800223', 'GAME_STATUS_ID': 1, 'GAME_STATUS_TEXT': '8:30 pm ET', 'GAMECODE': '20190504/GSWHOU', 'HOME_TEAM_ID': 1610612745, 'VISITOR_TEAM_ID': 1610612744, 'SEASON': '2018', 'LIVE_PERIOD': 0, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': 'ABC', 'LIVE_PERIOD_TIME_BCAST': 'Q0       - ABC', 'WH_STATUS': 0, 'HOME_TEAM_NAME': 'Houston Rockets', 'VISITOR_TEAM_NAME': 'Golden State Warriors'}]
def test_list_games_one(capsys):

    console_out.list_games(games_single)
    
    captured = capsys.readouterr()

    assert captured.out == "\nAvailable games:\n\t(1) Golden State Warriors @ Houston Rockets - (8:30 pm ET)\n"

games_multiple = [
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 1, 'GAME_ID': '0021801152', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/DETIND', 'HOME_TEAM_ID': 1610612754, 'VISITOR_TEAM_ID': 1610612765, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Indiana Pacers', 'VISITOR_TEAM_NAME': 'Detroit Pistons'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 2, 'GAME_ID': '0021801153', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/MIABOS', 'HOME_TEAM_ID': 1610612738, 'VISITOR_TEAM_ID': 1610612748, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': 'NBA TV', 'LIVE_PERIOD_TIME_BCAST': 'Q4       - NBA TV', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Boston Celtics', 'VISITOR_TEAM_NAME': 'Miami Heat'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 3, 'GAME_ID': '0021801154', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/MILBKN', 'HOME_TEAM_ID': 1610612751, 'VISITOR_TEAM_ID': 1610612749, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Brooklyn Nets', 'VISITOR_TEAM_NAME': 'Milwaukee Bucks'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 4, 'GAME_ID': '0021801155', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/CHINYK', 'HOME_TEAM_ID': 1610612752, 'VISITOR_TEAM_ID': 1610612741, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'New York Knicks', 'VISITOR_TEAM_NAME': 'Chicago Bulls'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 5, 'GAME_ID': '0021801156', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/ORLTOR', 'HOME_TEAM_ID': 1610612761, 'VISITOR_TEAM_ID': 1610612753, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Toronto Raptors', 'VISITOR_TEAM_NAME': 'Orlando Magic'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 6, 'GAME_ID': '0021801157', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/PORMIN', 'HOME_TEAM_ID': 1610612750, 'VISITOR_TEAM_ID': 1610612757, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Minnesota Timberwolves', 'VISITOR_TEAM_NAME': 'Portland Trail Blazers'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 7, 'GAME_ID': '0021801158', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/PHIDAL', 'HOME_TEAM_ID': 1610612742, 'VISITOR_TEAM_ID': 1610612755, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Dallas Mavericks', 'VISITOR_TEAM_NAME': 'Philadelphia 76ers'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 8, 'GAME_ID': '0021801159', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/CHAUTA', 'HOME_TEAM_ID': 1610612762, 'VISITOR_TEAM_ID': 1610612766, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': None, 'LIVE_PERIOD_TIME_BCAST': 'Q4       - ', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Utah Jazz', 'VISITOR_TEAM_NAME': 'Charlotte Hornets'}, 
    {'GAME_DATE_EST': '2019-04-01T00:00:00', 'GAME_SEQUENCE': 9, 'GAME_ID': '0021801160', 'GAME_STATUS_ID': 3, 'GAME_STATUS_TEXT': 'Final', 'GAMECODE': '20190401/CLEPHX', 'HOME_TEAM_ID': 1610612756, 'VISITOR_TEAM_ID': 1610612739, 'SEASON': '2018', 'LIVE_PERIOD': 4, 'LIVE_PC_TIME': '     ', 'NATL_TV_BROADCASTER_ABBREVIATION': 'NBA TV', 'LIVE_PERIOD_TIME_BCAST': 'Q4       - NBA TV', 'WH_STATUS': 1, 'HOME_TEAM_NAME': 'Phoenix Suns', 'VISITOR_TEAM_NAME': 'Cleveland Cavaliers'}]
def test_list_games_multiple(capsys):

    console_out.list_games(games_multiple)
    
    captured = capsys.readouterr()

    assert captured.out == "\nAvailable games:\n" \
        "\t(1) Detroit Pistons @ Indiana Pacers - (Final)\n" \
        "\t(2) Miami Heat @ Boston Celtics - (Final)\n" \
        "\t(3) Milwaukee Bucks @ Brooklyn Nets - (Final)\n" \
        "\t(4) Chicago Bulls @ New York Knicks - (Final)\n" \
        "\t(5) Orlando Magic @ Toronto Raptors - (Final)\n" \
        "\t(6) Portland Trail Blazers @ Minnesota Timberwolves - (Final)\n" \
        "\t(7) Philadelphia 76ers @ Dallas Mavericks - (Final)\n" \
        "\t(8) Charlotte Hornets @ Utah Jazz - (Final)\n" \
        "\t(9) Cleveland Cavaliers @ Phoenix Suns - (Final)\n"

def test_list_teams_multiple(capsys):

    console_out.list_teams(games_single[0])

    captured = capsys.readouterr()

    assert captured.out == "\nChoose a Team:\n\t(v) Golden State Warriors\n\t(h) Houston Rockets\n"
