import csv
import json

data = [
    {"Name": "Pip", "Age": 26, "Hair": "None", "Python-Score": 0.69, "Active": True},
    {"Name": "Leia", "Age": 25, "Hair": "Purple", "Python-Score": 0.78, "Active": True},
    {"Name": "Prof. Turtle", "Age": 134, "Hair": "Gray", "Python-Score": 0.99, "Active": False}
]

# Save to txt file
with open("data.txt", "w") as txt_file:
    for entry in data:
        txt_file.write(str(entry) + "\n")

# Save to csv file
with open("data.csv", "w", newline="") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(data)

# Save to json file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Read from txt file
with open("data.txt", "r") as txt_file:
    # Create a new list by evaluating each line as a Python expression
    new_data_txt = [eval(line.strip()) for line in txt_file]

# Read from csv file
with open("data.csv", "r") as csv_file:
    # Create a new list by reading rows from the csv file as dictionaries
    csv_reader = csv.DictReader(csv_file)
    new_data_csv = [dict(row) for row in csv_reader]

# Read from json file
with open("data.json", "r") as json_file:
    # Load data from the json file into a new list
    new_data_json = json.load(json_file)

# Compare txt
print("Comparison for txt:", str(new_data_txt) == str(data))

# Compare csv
converted_new_data_csv = [{key: (int(value) if key == 'Age' else float(value) if key == 'Python-Score' else eval(value) if key == 'Active' else value) for key, value in row.items()} for row in new_data_csv]
print("Comparison for csv:", converted_new_data_csv == data)

# Compare json
print("Comparison for json:", str(new_data_json) == str(data))
