# Implement the UndergroundSystem class:

# void checkIn(int id, string stationName, int t)
# A customer with a card id equal to id, gets in the station stationName at time t.
# A customer can only be checked into one place at a time.
# void checkOut(int id, string stationName, int t)
# A customer with a card id equal to id, gets out from the station stationName at time t.
# double getAverageTime(string startStation, string endStation)
# Returns the average time to travel between the startStation and the endStation.
# The average time is computed from all the previous traveling from startStation to endStation that happened directly.
# Call to getAverageTime is always valid.
# You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.


# HINT: Use two hash tables. The first to save the check-in time for a customer and the second to update the total time between two stations.

# DESIGN UNDERGROUND SYSTEM

from collections import defaultdict


class UndergroundSystem:
    
    def __init__(self):
        self.ins = {}                                              # customer_id: (start_station, start_time)
        self.outs = defaultdict(list)                              # (start_station, end_station)

    def checkIn(self, id, stationName, t):
        self.ins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start_station, start_time = self.ins[id]
        total = t - start_time
        self.outs[(start_station, stationName)].append(total)

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)
        difference = self.outs[key]
        return sum(difference) / len(difference)

# TIME COMPLEXITY: 

class UndergroundSystem:
    
    def __init__(self):
        self.checkIns = {}
        self.times = {}

    def checkIn(self, id, stationName, t):
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        try:
            self.times[self.checkIns[id][0] + "-" + stationName].append(t-self.checkIns[id][1])
        except KeyError:
            self.times[self.checkIns[id][0] + "-" + stationName] = [t-self.checkIns[id][1]]
            
    def getAverageTime(self, startStation, endStation):
        return sum(self.times[startStation + "-" + endStation])/len(self.times[startStation + "-" + endStation])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

a = UndergroundSystem()

# Test 1

a.checkIn(10,"Leyton",3)

a.checkOut(10,"Paradise", 8)

print(a.getAverageTime("Leyton", "Paradise"))

