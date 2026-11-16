import pandas as pd

devices = {}
while True:
    name = input("Enter device name (or 'done'): ")
    if name.lower() == "done":
        break
    watt = float(input("Enter wattage: "))
    hours = float(input("Enter usage hours: "))
    devices[name] = [watt, hours]

def calc_kwh(watt, hours):
    return (watt * hours) / 1000

data = []
for name, (watt, hours) in devices.items():
    kwh = calc_kwh(watt, hours)
    data.append([name, watt, hours, kwh])

df = pd.DataFrame(data, columns=["Device", "Watt", "Hours", "kWh"])
df.to_csv("energy.csv", index=False)

df = pd.read_csv("energy.csv").dropna()
print("Mean:", df["kWh"].mean())
print("Median:", df["kWh"].median())
print("Highest usage device:", df.loc[df["kWh"].idxmax(), "Device"])