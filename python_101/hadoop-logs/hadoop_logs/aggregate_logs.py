import pandas as pd
import sys
import ipdb

def read_csv(filepath):
        df = pd.read_csv(filepath)
        return df


def aggregate(df):
    #breakpoint()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace = True)
    resampled_df = df.groupby([pd.Grouper(freq='30s'), 'level']).size().unstack(fill_value=0)
    return resampled_df

def main():
    resampled_df = aggregate(read_csv(sys.argv[1]))
    resampled_df.to_csv(sys.argv[2])

if __name__ == "__main__":
    import cProfile; cProfile.run("main()")
