# Finger exercise, p.216
# Implement a subclass of Person that meets the specification

from person import Person


class Politician(Person):
    """A politician is a person who can belong to a political party"""

    def __init__(self, name, party=None):
        """name and party are strings"""
        super().__init__(name)
        self._party = party

    def get_party(self):
        """Returns the party to which self belongs"""
        return self._party

    def might_agree(self, other):
        """Returns True if self and other belong to the same party or at least
           one of them does not belong to a party.
        """
        agree = False
        # IF both politician belong to the same party
        if ((self._party and other._party) and (self._party == other._party)):
            agree = True
        # OR at least one politician belongs to a party
        elif ((self._party is None and other._party)
              or (self._party and other._party is None)):
            agree = True
        return agree
