import csv

def save_csv(filename, csv_file='records.csv'):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([filename])  

def read_csv(csv_file='records.csv'):
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0]) 
    except FileNotFoundError:
        print(f"Файл {csv_file} не знайдено.")

if __name__ == '__main__':
    read_csv()