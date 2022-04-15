from players import Player


def test_player():
    sampleplayer = Player("testowy")
    assert sampleplayer.name == "testowy"
    assert sampleplayer.hand == []
    assert sampleplayer.handvalue == 0
    assert sampleplayer.score == 0
