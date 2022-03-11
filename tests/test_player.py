import pytest

from src.laxleague.guardian import Guardian
from src.laxleague.player import Player


def test_construction():
    p = Player('Tatiana', 'Jones')
    assert 'Tatiana' == p.first_name
    assert 'Jones' == p.last_name


def test_add_guardians():
    g = Guardian('Mary', 'Jones')
    p = Player('Tatiana', 'Jones')
    p.add_guardian(g)
    assert [g] == p.guardians


@pytest.mark.skip(reason='have not yet implemented method')
def test_add_guardians():
    p = Player('Tatiana', 'Jones')

    # Add one guardian
    g1 = Guardian('Mary', 'Jones')
    p.add_guardian(g1)

    # layer, add one more
    g2 = Guardian('Joanie', 'Johnson')
    g3 = Guardian('Jerry', 'Johnson')
    p.add_guardians((g2, g3))

    assert g1 == p.primary_guardian
