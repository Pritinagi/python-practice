from main_01 import get_weather


def test_get_weather():
    assert get_weather(21)=='hoot'
    assert get_weather(21)=='hot'


# commands are there to run look at notes for specific commands the one most useful one is 
# pytest -v {runs all the tests }
# pytest specific_file_path(runs the exact file of pytest )