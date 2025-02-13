import matplotlib.pyplot as plt
import pandas as pd
import sys

def read_resampled_logs(filepath):
    resampled_df = pd.read_csv(filepath,parse_dates=["timestamp"])
    resampled_df.set_index("timestamp",inplace=True)
    return resampled_df

def plot_logs(resampled_df):
    color_dict = {'FATAL': '#000000', 'ERROR': '#E69F00', 'WARN': '#56B4E9'}

    for column in resampled_df.columns:
        if column != "INFO":
            resampled_df[column].plot(label=column,color=color_dict[column])
    plt.savefig("logs.png")

if __name__ == "__main__":
    plot_logs(read_resampled_logs(sys.argv[1]))
    #print(read_resampled_logs(sys.argv[1]))
