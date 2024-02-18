# Function to input and store radiation data from a single location
def input_data(location):
  """
  This function takes a location as input and prompts the user to enter radiation readings.
  It stores the readings in a list and returns the list.
  """
  data = []
  while True:
    reading = float(input(f"Enter radiation reading for {location} (-1 to stop): "))
    if reading == -1:
      break
    data.append(reading)
  return data

# Function to calculate average and standard deviation
def calculate_statistics(data):
  """
  This function takes a list of radiation readings as input and calculates the average and standard deviation.
  It returns a tuple containing the average and standard deviation.
  """
  if not data:
    return None, None  # Handle empty data case
  total = sum(data)
  average = total / len(data)
  variance = sum((x - average) ** 2 for x in data) / len(data)
  standard_deviation = variance ** 0.5
  return average, standard_deviation

# Main program
locations = ["Location 1", "Location 2", "Location 3"]  # Modify as needed
all_data = {}

# Input data for each location
for location in locations:
  data = input_data(location)
  all_data[location] = data

# Analyze data for each location
for location, data in all_data.items():
  average, std_dev = calculate_statistics(data)
  print(f"\nResults for {location}:")
  print(f"Average radiation: {average:.2f}")
  print(f"Standard deviation: {std_dev:.2f}")

# Identify patterns and anomalies (further analysis based on your needs)
# Example: Compare averages and standard deviations across locations
# for location1, data1 in all_data.items():
#   for location2, data2 in all_data.items():
#     if location1 != location2:
#       average1, std_dev1 = calculate_statistics(data1)
#       average2, std_dev2 = calculate_statistics(data2)
#       # Compare average1, std_dev1 with average2, std_dev2
#       # Identify significant differences or patterns
'''
Explanation:

input_data function:

Takes a location as input.
Prompts the user to enter radiation readings in a loop until -1 is entered.
Stores the readings in a list and returns the list.
calculate_statistics function:

Takes a list of radiation readings as input.
Handles empty data case by returning None for both average and standard deviation.
Calculates the total sum of readings.
Calculates the average and variance.
Calculates the standard deviation as the square root of variance.
Returns a tuple containing the average and standard deviation.
Main program:

Defines a list of locations (modify as needed).
Creates an empty dictionary all_data to store data for each location.
Loops through each location:
Calls input_data to get readings for the current location.
Stores the readings in the all_data dictionary with the location as the key.
Loops through each location and its corresponding data in the dictionary:
Calls calculate_statistics to get average and standard deviation.
Prints the results for each location.
Pattern and anomaly identification:

This section provides an example of comparing averages and standard deviations across locations.
You can further analyze the data based on your specific needs, such as identifying significant differences, outliers, or correlations between locations.'''