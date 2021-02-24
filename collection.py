import os
import requests
from secret_key import API_KEY


# Put instructions in the README to rebuild this project like:
# Ensure that you create a secret_key.py file
# Mention site to get the key

def print_progress(command):
    print()
    print("==============================")
    print(f"{command}")
    print("==============================")
    print()


def create_api_string(company, month):
    return f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={company}&interval=1min&slice=year1month{month}&adjusted=false&apikey={API_KEY}"


def create_directory():
    if "TDL_Project_Data" not in os.listdir():
        os.mkdir("./TDL_Project_Data")
        print_progress("1. Created TDL_Project_Data directory.")

    else:
        print_progress("1. TDL_Project_Data Directory exists. Ignoring create directory.")


def check_dataset():
    print_progress("Checking dataset.\nComputing all missing files.")

    # Decide all companies to be present in the dataset
    companies_list = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]

    # List of files in dataset
    dataset_files = os.listdir("./TDL_Project_Data")

    missing_files = []

    for company in companies_list:
        for month in range(1, 4):
            csv_file_name = f"{company}_year1_month{month}.csv"

            if csv_file_name not in dataset_files:
                print(f"{csv_file_name} missing from dataset.")
                missing_files.append(csv_file_name)

            else:
                print(f"{csv_file_name} present in dataset.")

    return missing_files


def download_missing_files(missing_files):
    missing_files_string = '\n'.join(missing_files)
    print_progress(f"Files to download:\n{missing_files_string}")

    no_of_files = len(missing_files)
    current_file = 0

    for csv in missing_files:
        current_file += 1
        print(f"Downloading file {current_file} of {no_of_files}")

        month = csv[-5]
        company = csv[:-17]
        print(f"Downloading {csv}, please wait as this may take time.")

        req = requests.get(create_api_string(company, month), stream=True)
        if req.status_code == 200:
            content = req.content
            with open(f"./TDL_Project_Data/{csv}", 'wb') as csv_file:
                csv_file.write(content)
                csv_file.close()

        print(f"Successfully downloaded {csv}.")
        print()


def run():
    print_progress("Running script to create/fix dataset.")
    create_directory()
    missing_files = check_dataset()
    download_missing_files(missing_files)


if __name__ == "__main__":
    run()
