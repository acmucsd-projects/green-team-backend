from .nodeSeed import seedNodes
from .treeSeed import seedTrees
from .userSeed import seedUsers
from .connectionSeed import seedConnections

def seedTables():
    seedNodes()
    seedTrees()
    seedConnections()
    seedUsers()
    print("Seeds successfully run")
