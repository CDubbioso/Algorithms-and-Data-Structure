import numpy as np

RNG = np.random.default_rng()

class Ring():
    """
    One ring of the lock.
    """
    def __init__(self, current=0, size=3):
        """
        Attributes:
            :param current: Current value that is on top of the ring.
            :type current: int
            :param size: The number of options that this ring has.
            :type size: int
            :param answer: the correct position of this ring.
            :type answer: int
        """
        self.__current = current
        self.__size = size
        self.__answer = RNG.integers(size)

    def turn(self):
        """
        This method turns the ring clockwise and
        returns if the ring is in the original order.
        :return: if the ring is in the original order.
        :rtype: boolean
        """
        self.__current = (self.__current + 1) % self.__size
        return not self.__current

    def correct(self):
        """
        This method check if the ring is currently in the right position.
        """
        return self.__current == self.__answer

    def __repr__(self):
        return f"Ring({chr(self.__current + 65)})"

class LockCombinationPuzzle():
    """
    This class represents a lock with a certain amount of rings
    that need to be positioned in the correct order to open the lock.
    """
    def __init__(self, n_rings=None, size=3):
        """
        This initialized the lock.
        Attributes:
            :param rings: The rings of the lock.
            :type rings: list[Ring}
        :param n_rings: The number of rings this lock has, defaults to 3
        :type n_rings: int, optional
        :param size: The size of each ring (number of options), defaults to 3
                     This can also be a list with the size of each individual ring.
                     This list should have the same length as n_rings.
        :type size: list[int] or int, optional
        """
        if not isinstance(size, int):
            if n_rings != len(size) and not n_rings is None:
                raise ValueError("The number of rings should be equal to the number of sizes that are given for each individual ring!")
            self.__rings = [Ring(0, s) for s in size]
        else:
            if n_rings is None:
                n_rings = 3
            self.__rings = [Ring(0, size) for _ in range(n_rings)]

    def turn_ring(self, ring):
        """
        This method can rotate one ring clockwise.
        It also tells the user if the ring is back in its original position.
        Thus with the "A" on top.
        :param ring: The ring that is rotated.
        :type ring: int
        :return: If the ring is in its original position.
        :rtype: boolean
        """
        return self.__rings[ring].turn()

    def check_open(self):
        """
        This method checks if you can open the lock.
        :return: If opening the lock succeeded.
        :rtype: boolean
        """
        for ring in self.__rings:
            if not ring.correct():
                return False
        return True

    def __len__(self):
        """
        This gives the length of the lock which
        is defined as the number of rings.
        """
        return len(self.__rings)

    def __repr__(self):
        return str(self.__rings)
    

    
"""
In this assignment, you will interacted with a lock object as defined in the lock_helper.py file. 
Define a functionL: solve_lock_combination, which exhaustively generates the solution to unlock a sequence of combination locks.

You will need to read through the auxiliary file to understand how to interact with the lock-object.
"""

def solve_lock_combination(lock):
    """
    This function solves the lock with "n" rings problem.

    :param lock: The lock that needs to be opened.
    :type lock: lockRingPuzzle
    :return: This function does not have a return, as the lock object is changed.
    :rtype: None
    """
    solve_lock_combination_recursive(lock, 0)

def solve_lock_combination_recursive(lock, ring):
    """
    This is an optional helper-function, which you may implement to 
    compute "one step" e.g. in a DFS. This is one step in the exhaustive search algorithm which uses depth-first search.

    :param lock: The lock that needs to be opened.
    :type lock: lockRingPuzzle
    :param ring: The ring that is currently turned.
    :type ring: int
    :return: If the lock is opened in the current configuration.
    :rtype: boolean 
    """
    # Base case: all rings are set, check if it opens
    if ring == len(lock):
        return lock.check_open()

    # Try the current position of this ring
    if solve_lock_combination_recursive(lock, ring + 1):
        return True

    # Turn and try each remaining position
    while not lock.turn_ring(ring):
        if solve_lock_combination_recursive(lock, ring + 1):
            return True

    # Ring is back to start, nothing worked
    return False

# The code below randomly generates a lock and 
if __name__ == "__main__":
    lock = LockCombinationPuzzle()
    solve_lock_combination(lock)
    print(lock.check_open(), lock)