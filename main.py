import pandas as pd


def main():
    data = {"a": 10, "b": 20}
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = main()
    print("I'm here!............")
    print(df)