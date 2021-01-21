import pdb
import api.src.adapters as adapters


def test_find_game_engine_hit():
    # check Among Us game with search
    ig = adapters.IGDB_Client()
    engine = ig.find_game_engine('Among Us')
    assert engine == 'Unity'

def test_find_game_engine_no_game():
    # check Roblox game with search and gets [] and returns unknown
    ig = adapters.IGDB_Client()
    engine = ig.find_game_engine('Roblox')
    assert engine == None

def test_find_game_engine_hit_no_engine():
    # check Candy Crush Saga game with search and finds game with no game engine info and returns unknown
    ig = adapters.IGDB_Client()
    engine = ig.find_game_engine('Candy Crush Saga')
    assert engine == None


# overall I'm unclear what these tests do for you.  what's the point in checking a game is not there?  
# Is it that your checking the connection? Then perhaps just test that get status code of 200.
