def read_data(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    parsed_data = []

    for line in lines:
        name, age = line.split(",")
        parsed_data.append((name, int(age)))

    return parsed_data
