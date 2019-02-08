import parmed as pmd

from topology.external.convert_parmed import from_parmed

def test_from_parmed():
    struc = pmd.load_file('ethane.mol2').to_structure()
    top = from_parmed(struc)

    assert top.n_sites == 8
    assert top.n_connections == 7