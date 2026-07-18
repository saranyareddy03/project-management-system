import csv
def read_csv(filename):

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []

    except Exception as e:
        print("Error reading file:", e)
        return []


def write_csv(filename, data, fieldnames):
   
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(data)

    except Exception as e:
        print("Error writing file:", e)