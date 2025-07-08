import time

def read_file(filename):
    print(f"Reading file {filename}...")
    start_time = time.perf_counter()
    with open(filename, "r") as f:
        bytes = f.read()
        print(f"Read file with length {len(bytes)} in {time.perf_counter() - start_time:0.2f} seconds.")

def process_data(list_of_files):
    start_time = time.perf_counter()
    for file in list_of_files:
        read_file(file)
    total_time = time.perf_counter() - start_time
    print(f"Processed {len(list_of_files)} files in {total_time:0.2f} seconds.")

if __name__ == '__main__':
    list_of_files = ['news.csv','news.csv','news.csv']
    process_data(list_of_files)
