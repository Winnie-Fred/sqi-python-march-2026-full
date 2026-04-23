from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data

print(read_data("data.txt"))
print(fetch_user_data())