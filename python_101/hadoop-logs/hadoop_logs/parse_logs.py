import sys
import re
import pandas as pd


def parse_log_data(file_path):
    parsed_log_data = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w*) \[(.*?)\] (.*?): (.*)', line)
            if match:
                parsed_log_data.append({
                    "timestamp": match.group(1),
                    "level": match.group(2),
                    "thread": match.group(3),
                    "source": match.group(4),
                    "message": match.group(5),
                })
    return parsed_log_data

def write_to_csv(parsed_log_data,file_path):
    df = pd.DataFrame(parsed_log_data)
    df.to_csv(file_path,index=False)

if __name__ == "__main__":
    write_to_csv(parse_log_data(sys.argv[1]),sys.argv[2])
