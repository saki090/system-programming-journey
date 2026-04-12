import csv
import os

# hint: define your CSV filename as a variable
filename = "f1_database.csv"
# hint: these are my column headers
fields = ["Race", "Driver", "Team", "Position", "FastestLap"]
# hint: list of dictionaries, one per race result
rows = [
    {"Race": "Australian GP", "Driver": "George Russell", "Team": "Mercedes", "Position": 1, "FastestLap": "1:32.156"},
    {"Race": "Chinese GP", "Driver": "Kimi Antonelli", "Team": "Mercedes", "Position": 2, "FastestLap": "1:32.456"},
    {"Race": "Japanese GP", "Driver": "Kimi Antonelli", "Team": "Mercedes", "Position": 1, "FastestLap": "1:32.789"},
]
def save_to_csv():
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
def read_from_csv():
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
def find_winner():
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
        winners = [row for row in all_rows if int(row["Position"]) == 1]
        for winner in winners:
            print(f"Winner of {winner['Race']}: {winner['Driver']} ({winner['Team']})")
if __name__ == "__main__":
    save_to_csv()
    read_from_csv()
    find_winner()  