from faker import Faker
import random
import csv

fake = Faker()
statuses = ["success", "failure"]

# Create CSV file
with open("login_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "username", "IP_address", "status"])  # header row
    
    for _ in range(100):  # generate 100 rows
        writer.writerow([
            fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            fake.user_name(),
            fake.ipv4(),
            random.choice(statuses)
        ])
