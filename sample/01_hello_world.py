#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""

import anki_vector
import nba_api

def main():
    
    # Select the dictionary for the Pacers, which contains their team ID
    from nba_api.stats.static import teams
    pacers = teams.find_team_by_abbreviation('IND')
    pacers_id = pacers['id']

    # Query for games where the Pacers were playing
    from nba_api.stats.endpoints import leaguegamefinder
    from nba_api.stats.library.parameters import Season
    from nba_api.stats.library.parameters import SeasonType
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=pacers_id,
                                            season_nullable=Season.default,
                                            season_type_nullable=SeasonType.regular)    
    game = gamefinder.get_normalized_dict()
    game_id = game["LeagueGameFinderResults"][0]["GAME_ID"]


    # Query for the play by play of their last game
    from nba_api.stats.endpoints import playbyplay
    plays = playbyplay.PlayByPlay(game_id).get_normalized_dict()['PlayByPlay']
    
    import nba_natural_language
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        for play in plays:
            home = play["HOMEDESCRIPTION"]
            visitor = play["VISITORDESCRIPTION"]
            if home != None:
                robot.say_text(nba_natural_language.translate_playbyplay(home))
            elif visitor != None:
                robot.say_text(nba_natural_language.translate_playbyplay(visitor)) 
            else:
                pass

if __name__ == "__main__":
    main()
