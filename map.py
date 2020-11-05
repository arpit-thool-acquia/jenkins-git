import sys
from datetime import datetime
class Car:

    def __init__(self):
        self.__refuelDetourDistance = 10.0 #Round trip distance for refueling
        self.__refuelDetourTime = 0.5 # Time taken at fuel pump for refueling
        self.__totalDistanceTravelled = 0
        self.__totalTimeTaken = 0.0
        self.__totalRefuels = 0
        self.__maxRange = 200.0 #Maximum limit the car can travel in one refuel
        self.__speed = 70.0 #Speed limit imposed
        self.__remainingLimit = self.__maxRange

    #Getters for the defined attributes
    def getTotalDistanceTravelled(self):
        return self.__totalDistanceTravelled

    def getTotalTimeTaken(self):
        return self.__totalTimeTaken

    def getTotalRefuels(self):
        return self.__totalRefuels

    def getMaxRange(self):
        return self.__maxRange

    def getSpeed(self):
        return self.__speed

    def getRemainingLimit(self):
        return self.__remainingLimit

    def resetSpeed(self):
        self.__speed = 70.0


    def mapping(self,road):
        output = {}
        self.map(road.getRoadType(),road.getRoadLength(),road.getGarageDistance(),road.getSpeedModifier(),road.getMaxRangeModifier())
        dt_string = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        output = {
        "road_type":road.getRoadType(),
        "road_length":road.getRoadLength(),
        "totalDistanceTravelled":self.__totalDistanceTravelled,
        "totalTimeTaken":"{:.2f}".format(self.__totalTimeTaken),
        "totalRefuels":self.__totalRefuels,
        "datetime":dt_string
        }
        return output

    #Calculate the required result
    def map(self, road_type, road_length, garageDistance, speedModifier, maxRangeModifier):

        # Car travels from Garage to Mapping Area and back
        self.__totalTimeTaken += (2*garageDistance)/self.__speed

        self.__remainingLimit -= garageDistance

        #Car enters mapping area
        #Set constraints according to Road type
        self.__maxRange *= 1 + maxRangeModifier
        self.__speed *= 1 + speedModifier

        mappingDistance = road_length

        #For the first round
        # if(road_type == "urban"):
        self.__remainingLimit *= (1 + maxRangeModifier)

        oneRoundDistance = self.__remainingLimit - self.__refuelDetourDistance
        mappingDistance -= oneRoundDistance

        #First Refuel
        self.__totalRefuels += 1
        self.__remainingLimit = self.__maxRange
        self.__totalTimeTaken

        #Next Rounds
        self.__totalRefuels += round(mappingDistance/self.__remainingLimit)
        self.__totalDistanceTravelled += 2*garageDistance + road_length + self.__totalRefuels*self.__refuelDetourDistance
        self.__totalTimeTaken += (road_length + self.__totalRefuels*self.__refuelDetourDistance)/self.__speed + (self.__totalRefuels*self.__refuelDetourTime)
