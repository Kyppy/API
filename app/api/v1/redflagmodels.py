"""Module provides methods to manipulate a simulated database variable"""
redflag_incidents = []
"""Database substitute variable"""


class RedFlagModel():
    """This class contains methods to manipulate the redflag_incident
    variable used to simulate a database"""
    def __init__(self):
        self.db = redflag_incidents

    def store(self, redflag_incidents):
        """Appends values to the redflag_incident variable"""
        self.db.append(redflag_incidents)
        
    def get_flags(self):
        """Returns a list of all values in redflag_incident"""
        return self.db
