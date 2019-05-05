import pytest
from vector_nba import nba_api
from nba_api.stats.library.data import teams

@pytest.fixture
def team_dict():
    return nba_api.get_teams()

@pytest.mark.parametrize('team', teams)
def test_get_teams(team, team_dict):
    
    assert team_dict[team[0]] == team[5]