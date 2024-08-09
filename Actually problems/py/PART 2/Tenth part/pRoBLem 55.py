"""


**Real-World Scenario:** You are planning a road trip from New York City to
 Los Angeles, which is approximately 2,800 miles (4,506 kilometers) away.
   You want to calculate the total cost of fuel for the trip, 
   given the average fuel efficiency of your vehicle and the current 
   price of gasoline.

**Data:**
- Distance from New York City to Los Angeles: 2,800 miles (4,506 kilometers).
- Average fuel efficiency of your vehicle: 25 miles per gallon (MPG).
- Current price of gasoline: $3.50 per gallon.

"""
##GOOD

distance=2800
MPG=25
PPG=3.50
GFD=distance/MPG
TM=GFD*PPG
print(TM)
