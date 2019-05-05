import pytest
import datetime
from vector_nba import nba_api

games_date = datetime.date(2019, 3, 7)

@pytest.mark.parametrize('game', nba_api.get_games(games_date))
def test_home_team_name(game):
    
    assert game['HOME_TEAM_NAME'] == nba_api.get_teams()[game['HOME_TEAM_ID']]

@pytest.mark.parametrize('game', nba_api.get_games(games_date))
def test_visitor_team_name(game):
    
    assert game['VISITOR_TEAM_NAME'] == nba_api.get_teams()[game['VISITOR_TEAM_ID']]