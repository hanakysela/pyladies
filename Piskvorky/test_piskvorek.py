import pytest
import Oskar

def test_tah():
    pole=Oskar.tah("-------", 1, "x")
    assert len(pole) == 7
    assert pole[1] == "x"


def test_chybny_tah():
    with pytest.raises(ValueError):
        Oskar.tah("xxxxxxx", 2, "o")
