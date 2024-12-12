import csv
import copy

# Define the vehicle template
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Print the default template
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Initialize the inventory list
myInventoryList = []

# Open and process the CSV file
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            # Print column headers
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Print vehicle details
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')

            # Create a new vehicle instance and populate its data
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = int(row[3])  # Convert to integer
            currentVehicle["range"] = int(row[4])  # Convert to integer
            currentVehicle["topSpeed"] = int(row[5])  # Convert to integer
            currentVehicle["zeroSixty"] = float(row[6])  # Convert to float
            currentVehicle["mileage"] = int(row[7])  # Convert to integer

            # Add to inventory list
            myInventoryList.append(currentVehicle)
            lineCount += 1

    print(f'Processed {lineCount - 1} lines.')  # Exclude header line

# Print inventory list details
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
