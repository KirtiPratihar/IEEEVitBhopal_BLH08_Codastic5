import csv

def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    return [name, age, city]

def write_to_csv(data, filename='user_data.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    # If file does not exist, create it and write the header
    filename = 'data.csv'
    try:
        with open(filename, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "City"])
    except FileExistsError:
        pass

    while True:
        user_data = get_user_input()
        write_to_csv(user_data)

        another = input("Do you want to enter another record? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
