from .nodeSeed import seedNodes
from .treeSeed import seedTrees
from .connectionSeed import seedConnections

def seedTables():
    seedNodes() 
    seedTrees()
    seedConnections()
    print("Seeds successfully run")