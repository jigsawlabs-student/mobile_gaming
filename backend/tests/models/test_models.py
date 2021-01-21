import datetime
import psycopg2
import pytest

import api.src.adapters as adapters
import api.src.db as db
import api.src.models as models
from  tests.data.builder_data import (s3d_rating, s3d_earnings, s3d_details, s3d_record_date, s3d_rank_type, s3d_input, s3d_lower, s3d_higher, TS_details, amongus_ios)

# seems like these functions are testing more the adapter than the model, let's discuss
# the get_sibling functions are not tested here, and they deserve to be

@pytest.fixture()
def test_conn():
    # reference in  user and pasword from .env/settings.py
    test_conn = psycopg2.connect(dbname = 'mobilegaming_test', 
            user = 'postgres', password = 'postgres')
    cursor = test_conn.cursor()
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)
    yield test_conn
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)


def test_Game_object_attributes():
    s3d_game = models.Game(**s3d_input)

    assert s3d_game.name == 'Sushi Roll 3D'
    assert s3d_game.genre == 'simulation' 

def test_Rating_object_attributes():
    s3d_r = models.Rating(**s3d_rating)

    assert s3d_r.ranking == 1
    assert s3d_r.date_created == datetime.date(2021, 1, 6)

def test_Earnings_object_attributes():
    s3d_e = models.Earnings(**s3d_earnings)

    assert s3d_e.inapp == False
    assert s3d_e.shows_ads == True 
    assert s3d_e.revenue == 1000 
    assert s3d_e.downloads == 21000000 

def test_update_revenue_downloads_equal_lower_value_no_update(test_conn):
    test_cursor = test_conn.cursor()
    builder = adapters.Builder()
    game_objs = builder.run(s3d_details, s3d_record_date, s3d_rank_type, test_conn, test_cursor)
    game = game_objs['game']
    same_earnings = game.earnings(s3d_lower, test_conn, test_cursor)

    assert same_earnings.revenue == 1000
    assert same_earnings.downloads == 21000000

def test_update_revenue_downloads_bigger_value_update(test_conn):
    test_cursor = test_conn.cursor()
    builder = adapters.Builder()
    game_objs = builder.run(s3d_details, s3d_record_date, s3d_rank_type, test_conn, test_cursor)
    game = game_objs['game']
    same_earnings = game.earnings(s3d_higher, test_conn, test_cursor)

    assert same_earnings.revenue == 2000
    assert same_earnings.downloads == 22000000

def test_try_sibling_params_if_None_update(test_conn):
    test_cursor = test_conn.cursor()
    builder = adapters.Builder()
    amongus_ios_objs_1st = builder.run(amongus_ios, '2020-12-20', 'top free', test_conn, test_cursor)

    assert amongus_ios_objs_1st['game'].genre == '[6014, 7001, 7015]'
    assert amongus_ios_objs_1st['game'].game_engine == None
    assert amongus_ios_objs_1st['game'].release_date == None   

    amongus_android_objs = builder.run(TS_details, '2020-12-28', 'top free', test_conn, test_cursor)
    amongus_ios_objs_2nd = builder.run(amongus_ios, '2020-12-20', 'top free', test_conn, test_cursor)


    # just retrieve from dict once -> game = game_objs['game']
    assert amongus_ios_objs_2nd['game'].genre == 'action'
    assert amongus_ios_objs_2nd['game'].game_engine == 'Unity'
    assert amongus_ios_objs_2nd['game'].release_date == datetime.date(2018, 7, 25)





