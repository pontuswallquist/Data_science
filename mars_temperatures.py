import json
import urllib.request
import numpy as np
import matplotlib.pyplot as plt

with urllib.request.urlopen("https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0") as response:
    source = response.read()

data = json.loads(source)

with open("mars_weather.json", "w") as f:
    json.dump(data, f, indent=2)

with open('mars_weather.json','r') as f:
    data = json.load(f)


#Convert F to C
for sol in data['sol_keys']:
    tempf = data[sol]['AT']['av']
    data[sol]['AT']['av'] = ((tempf-32) * 5/9)

    tempf = data[sol]['AT']['mn']
    data[sol]['AT']['mn'] = ((tempf-32) * 5/9)

    tempf = data[sol]['AT']['mx']
    data[sol]['AT']['mx'] = ((tempf-32) * 5/9)

#Print temperature information in Celsius
print('SOL:\tAvg-T:\tMin-T:\tMax-T:\tFrom:\t\tTo:')
for sol in data['sol_keys']:
    print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(sol, round(data[sol]['AT']['av'], 2), round(data[sol]['AT']['mn'], 2), round(data[sol]['AT']['mx'], 2), data[sol]['First_UTC'][0:10], data[sol]['Last_UTC'][0:10]))

date = []
avgtemp = []

for sol in data['sol_keys']:
    date.append(data[sol]['First_UTC'][5:10])
    avgtemp.append(data[sol]['AT']['av'])

plt.plot(date, avgtemp, 'ro-')
plt.title("Recent Average Temperature on Mars")
plt.xlabel('Date (month-day)')
plt.ylabel('Avg-Temp')

plt.show()