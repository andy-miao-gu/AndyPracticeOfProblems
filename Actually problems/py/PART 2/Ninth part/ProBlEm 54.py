"""#Problem: Population Growth and Resource Consumption

You are tasked with analyzing the population growth and its impact on resource 
consumption in a city over a certain period of time. Here are the details of the 
problem:

Initial Population: The city's population at the beginning of the analysis period is 
500,000 people.

Annual Growth Rate: The city experiences an annual population growth rate of 2.5%.

Resource Consumption per Capita: On average, each person in the city consumes 500 
liters of water and 1 megawatt-hour (MWh) of electricity per year.

Resource Availability: The city has a limited supply of resources. At the start of 
the analysis, it has 100 million liters of water and 200,000 MWh of electricity 
available.

Resource Renewal: The city can renew 10 million liters of water and 5,000 MWh of 
electricity per year through sustainable sources.

You need to answer the following questions:

a. Calculate the city's population after 10 years.

b. Determine the total water and electricity consumption in the city after 10 years.

c. Assess whether the city's resource availability will be sufficient to support 
the population after 10 years based on the calculated consumption."""
population=721858
growth_rate=1.7
years=10
population_years=population+(1+growth_rate)**years
print(population_years)
water=500
water_spent=water*population_years
population_years
electric=1
electric_spent=electric*population_years
Water_wehave=100000000
Electric_wehave=50000
if water_spent > Water_wehave:
    print("sorry water not avaliable")
if electric_spent>Electric_wehave:
    print("sorry electric not avaliable")