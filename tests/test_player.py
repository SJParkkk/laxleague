from laxleague.guardian import Guardian
from laxleague.player import Player


def test_construction():
    p = Player('Tatiana', 'Jones')
    assert 'Tatiana' == p.first_name
    assert 'Jones' == p.last_name


def test_add_guardians():
    g = Guardian('Mary', 'Jones')
    p = Player('Tatiana', 'Jones')
    p.add_guardian(g)
    assert [g] == p.guardians
