from nose.tools import assert_equal
from sys import argv
from app.engine import *

liceo = Classe()
compare = Classe()

compare.surnames.extend(["Arcangeli\n",
                        "Di Corcia\n",
                        "Di Rocco\n",
                        "Rossi\n",
                        "Massicci\n",
                        "Carrara\n",
                        "Di Vizia\n",
                        "Codogni\n",
                        "Morri\n",
                        "Meneghelli\n"])

def test_getdata():
    liceo.getdata("test")
    compare.surnames.sort()
    assert_equal(compare.surnames, liceo.surnames)
    for p in liceo.surnames:
        assert_equal(p, liceo.members[p].surname)

def test_randomsort():
    assert_equal(liceo.randomsort(), liceo.sortedsurnames)

#from random import sample

#name = "test"

#filetxt = open(name + ".txt")

#l = []
#l.extend(filetxt.readlines())

#print(sample(l, len(l)))
