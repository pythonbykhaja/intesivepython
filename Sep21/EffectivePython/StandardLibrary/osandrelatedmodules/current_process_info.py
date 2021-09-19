import platform
import os
import sys

if __name__ == '__main__':
    # Current process information
    print("Process Id: ", os.getpid())
    print("Parent Process Id: ", os.getppid() )

    # Machine information using platform
    print("Machine Network Name: ",platform.node())
    print("Python version: ", platform.python_version())
    print("System: ", platform.system())

    # Get the Python Path and the arguments passed to interpreter
    print()
    print("Python module lookup path", sys.path)
    print("Command i.e. used to run Python ", sys.argv)

    # Read environment varaible
    print()
    print("Environmental variable path: ",os.environ['PATH'])
    
