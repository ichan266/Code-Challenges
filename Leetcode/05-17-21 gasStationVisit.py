# Leetcode # 134
# https://leetcode.com/problems/gas-station/

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

#* This solution works but it is very slow!
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    
    startStationIndex = []
    
    # This for loop is to find out which stations I can start with, then put it in a list
    for (index, gasReceived) , gasNeeded in zip((enumerate(gas)), cost):
        if gasReceived >= gasNeeded:
            startStationIndex.append(index)
    
    # Using the index gathered from above, now I start testing with each startStation with slicing
    # Note that the else clause executes at the end of the for loop. So if the for loop is completed and current_tank >= 0, then we find the station!
    for startStation in startStationIndex:
        current_tank = 0
        newGas = gas[startStation:] + gas[:startStation]
        newCost = cost[startStation:] + cost[:startStation]
        for gas1, cost1 in zip(newGas, newCost):
            current_tank = current_tank + gas1 - cost1
            if current_tank < 0:
                break
        else:
            if current_tank >= 0:
                return startStation
                
    return -1
                   