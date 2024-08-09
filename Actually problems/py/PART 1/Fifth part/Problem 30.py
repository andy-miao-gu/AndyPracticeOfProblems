bruh=earthquake_data = [
{
"date": "2023-05-26",
"magnitude": 6.5,
"location": "Tokyo"
},
{
"date": "2023-04-10",
"magnitude": 5.8,
"location": "Osaka"
},
{
"date": "2023-02-18",
"magnitude": 7.2,
"location": "Sapporo"
},
{
"date": "2023-01-07",
"magnitude": 6.2,
"location": "Kobe"
},
{
"date": "2022-11-19",
"magnitude": 5.4,
"location": "Nagoya"
},
{
"date": "2022-09-30",
"magnitude": 6.9,
"location": "Fukuoka"
},
{
"date": "2022-08-14",
"magnitude": 5.7,
"location": "Yokohama"
},
{
"date": "2022-06-25",
"magnitude": 6.1,
"location": "Sendai"
},
{
"date": "2022-05-09",
"magnitude": 5.9,
"location": "Hiroshima"
},
{
"date": "2022-03-22",
"magnitude": 6.4,
"location": "Nagasaki"
},
{
"date": "2022-02-03",
"magnitude": 5.5,
"location": "Kyoto"
},
{
"date": "2022-01-14",
"magnitude": 6.8,
"location": "Tokyo"
},
{
"date": "2021-12-05",
"magnitude": 5.6,
"location": "Osaka"
},
{
"date": "2021-10-18",
"magnitude": 6.3,
"location": "Sapporo"
},
{
"date": "2021-09-01",
"magnitude": 5.9,
"location": "Kobe"
},
{
"date": "2021-07-14",
"magnitude": 5.3,
"location": "Nagoya"
},
{
"date": "2021-06-26",
"magnitude": 6.0,
"location": "Fukuoka"
},
{
"date": "2021-05-09",
"magnitude": 5.7,
"location": "Yokohama"
},
{
"date": "2021-03-22",
"magnitude": 6.4,
"location": "Sendai"
},
{
"date": "2021-02-03",
"magnitude": 5.5,
"location": "Hiroshima"
},
{
"date": "2021-01-14",
"magnitude": 6.9,
"location": "Tokyo"
}
]
all_mag = []
for each in bruh:
    if each['location'] == "Tokyo":
        print(each)
    all_mag.append(each['magnitude'])
print("the sorted of the list =",sorted(all_mag))
print("the top 5 earthquakes =",sorted(all_mag)[-5:])
print("the max of the list =",max(all_mag))
print("the min of the list =",min(all_mag))
print("the sum of the list =",sum(all_mag))
print("the average of the list =",sum(all_mag)/len(all_mag))