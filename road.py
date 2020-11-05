#Parent class
class Road(object):

    #Constructor for Road object
    def __init__(self):
        self._road_type = "normal"
        self._road_length = 0.0 #Length of Mapping task
        self._maxRangeModifier = 0.0
        self._speedModifier = 0.0
        self._garageDistance = 0.0

    #Getter methods for Road attributes
    def getRoadType(self):
        return self.road_type

    def getRoadLength(self):
        return self.road_length

    def getGarageDistance(self):
        return self.garageDistance

    def getMaxRangeModifier(self):
        return self.maxRangeModifier

    def getSpeedModifier(self):
        return self.speedModifier

#Child class of Road
class Urban(Road):

    #Constructor for Urban
    def __init__(self, road_type, road_length):
        self.road_type = road_type
        self.road_length = road_length
        self.maxRangeModifier = -0.25
        self.speedModifier = -0.25
        self.garageDistance = 20.0
        super(Road,self).__init__()

#Child class of Road
class Rural(Road):

    #Constructor for rural
    def __init__(self, road_type, road_length):
        self.road_type = road_type
        self.road_length = road_length
        self.speedModifier = 0.15
        self.maxRangeModifier = 0.0
        self.garageDistance = 50.0
        super(Road,self).__init__()
