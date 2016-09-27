from csvreader import CSVReader
import sys

if __name__ == "__main__":
    try:
        csv_path = sys.argv[1]
    except:
        raise ValueError('csv file path not given')

    CSVReader(csv_path)
