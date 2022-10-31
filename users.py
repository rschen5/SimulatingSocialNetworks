import itertools
import copy


class User:
    """A class to model users of social network.

    Attributes:
        id (int): Auto incremented unique identifier.
        agreeableness (float): real number from 0-1.
        emotions (dict): real numbers for anxious, bored, happy, confused, scared, angry
        beliefs (float): real number from 0-1
        activity_level (dict): frequency of posts and interactions per unit time(int) and frequency of visits per unit time(int)
        groups (list): list of groups (subnetworks)
        num_connections (list): list of other users
        false_exposure (float): exposure to false news which decays over time, real number 0-1 
        exploration (float):  tendency to join new networks, real number 0-1 
        stability (float): tendency to leave a network, real number 0-1 
    """
    id_iter = itertools.count()

    def __init__(self, agreeableness, emotions, beliefs, activity_level, groups, num_connections, false_exposure, exploration, stability):
        self.__id = next(self.id_iter)
        self.agreeableness = agreeableness
        self.emotions = copy.deepcopy(emotions)
        self.beliefs = beliefs
        self.activity_level = copy.deepcopy(activity_level)
        self.groups = copy.deepcopy(groups)
        self.num_connections = copy.deepcopy(num_connections)
        self.false_exposure = false_exposure
        self.exploration = exploration
        self.stability = stability

    # getters and setters
    @property
    def id(self):
        return self.__id

    @property
    def agreeableness(self):
        return self._agreeableness

    @agreeableness.setter
    def agreeableness(self, value):
        if value < 0 or value > 1:
            raise ValueError("Agreeableness should be between 0 and 1")
        self._agreeableness = float(value)

    @property
    def emotions(self):
        return self._emotions

    @emotions.setter
    def emotions(self, value):
        if not isinstance(value, dict):
            raise ValueError("emotions should be a dict")
        for key in value:
            if value[key] < 0 or value[key] > 1:
                raise ValueError("emotions items should be between 0 and 1")
        self._emotions = copy.deepcopy(value)

    @property
    def beliefs(self):
        return self._beliefs

    @beliefs.setter
    def beliefs(self, value):
        if value < 0 or value > 1:
            raise ValueError("Beliefs should be between 0 and 1")
        self._beliefs = float(value)

    @property
    def activity_level(self):
        return self._activity_level

    @activity_level.setter
    def activity_level(self, value):
        if not isinstance(value, dict):
            raise ValueError("activity_level should be a dict")
        for key in value:
            if isinstance(value[key], (int, long)):
                raise ValueError("activity_level items should be integer")
        self._activity_level = copy.deepcopy(value)

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, value):
        if not isinstance(value, list):
            raise ValueError("groups should be a list")
        for item in value:
            pass
            # check if item is network
            # if not isinstance(value, list):
            #     raise ValueError("groups should be a list")
        self._groups = copy.deepcopy(value)

    @property
    def num_connections(self):
        return self._num_connections

    @groups.setter
    def num_connections(self, value):
        if not isinstance(value, list):
            raise ValueError("groups should be a list")
        for item in value:
            if not isinstance(item, (int, long)):
                raise ValueError(
                    "items in num_connection should be a int or ids")
        self._num_connections = copy.deepcopy(value)

    @property
    def false_exposure(self):
        return self._false_exposure

    @false_exposure.setter
    def false_exposure(self, value):
        if value < 0 or value > 1:
            raise ValueError("false_exposure should be between 0 and 1")
        self._false_exposure = float(value)

    @property
    def exploration(self):
        return self._exploration

    @exploration.setter
    def exploration(self, value):
        if value < 0 or value > 1:
            raise ValueError("exploration should be between 0 and 1")
        self._exploration = float(value)

    @property
    def stability(self):
        return self._stability

    @stability.setter
    def stability(self, value):
        if value < 0 or value > 1:
            raise ValueError("stability should be between 0 and 1")
        self._stability = float(value)

    # update methods
    def update_beliefs(self, factors):
        # do something with factors
        self.beliefs = self.beliefs

    def update_groups(self, factors):
        # do something with factors
        self.groups = self.groups

    def update_num_connections(self, factors):
        # do something with factors
        self.num_connections = self.num_connections

    def update_activity_level(self, factors):
        # do something with factors
        self.activity_level = self.activity_level

    def update_emotions(self, factors):
        # do something with factors
        self.emotions = self.emotions

    def update_false_exposure(self, posts):
        # do something with factors
        # if posts are empty, just reduce the value
        # otherwise change based on calculate_false_exposure function
        self.false_exposure = self.false_exposure
    
    
    def calculate_false_exposure(posts):
        # do something with factors
        # calculate mean veracity, remove extreme outliers and calculate the weight
        pass

    def __str__(self):
        return "id: " + str(self.__id) + ", agreeableness: " + str(self.agreeableness)


u = User(0.8, {}, 0.9, {}, [], [], 0, 0.5, 0.5)

print(u)

u.agreeableness = 0.3
