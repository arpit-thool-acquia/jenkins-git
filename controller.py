from road import Urban, Rural
from map import Car
class Controller:
    #Check road type validity
    def validate_road_type(self,road_type):
        if not(road_type == "urban" or road_type=="rural"):
            return 1
        else:
            return 0

    #Check if road_length is not empty
    def validate_road_length(self,road_length):
        if (road_length == "" or road_length == " "):
            return 0.0
        else:
            return float(road_length)

    #Check mapping length is within valid range
    def check_road_length(self,road_length):
        if (road_length == 0.0):
            return 1
        if not(road_length > 0.0 and road_length < 100000000.0):
            return 1
        else:
            return 0

    def process(self,road_type,road_length):
        vrt = self.validate_road_type(road_type)
        if(vrt == 1):
            return "Invalid Road Type"
        road_length = self.validate_road_length(road_length)
        crl = self.check_road_length(road_length)
        if(crl == 1):
            return "Invalid Road length"
        #Initiate objects
        if(road_type == "urban"):
            road = Urban(road_type,road_length)
        elif(road_type == "rural"):
            road = Rural(road_type,road_length)

        #Perform Mapping Task
        carObject = Car()
        output = carObject.mapping(road)
        return output
