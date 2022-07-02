class Cast:
    """A collection of players.

    The responsibility of a cast is to keep track of a collection of players. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _players (dict): A dictionary of players { key: group_name, value: a list of players }
    """

    def __init__(self):
        """Constructs a new Player."""
        self._players = {}
        
    def add_player(self, group, player):
        """Adds an player to the given group.
        
        Args:
            group (string): The name of the group.
            player (Player): The player to add.
        """
        if not group in self._players.keys():
            self._players[group] = []
            
        if not player in self._players[group]:
            self._players[group].append(player)

    def get_players(self, group):
        """Gets the players in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The players in the group.
        """
        results = []
        if group in self._players.keys():
            results = self._players[group].copy()
        return results
    
    def get_all_players(self):
        """Gets all of the players in the cast.
        
        Returns:
            List: All of the players in the cast.
        """
        results = []
        for group in self._players:
            results.extend(self._players[group])
        return results

    def get_first_player(self, group):
        """Gets the first player in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first player in the group.
        """
        result = None
        if group in self._players.keys():
            result = self._players[group][0]
        return result

    def remove_player(self, group, player):
        """Removes an player from the given group.
        
        Args:
            group (string): The name of the group.
            player (Player): The player to remove.
        """
        if group in self._players:
            self._players[group].remove(player)