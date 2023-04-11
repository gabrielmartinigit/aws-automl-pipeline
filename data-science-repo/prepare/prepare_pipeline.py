import pandas as pd
from sklearn.model_selection import train_test_split


def transform_sex(value):
    if value == "female":
        return 1
    else:
        return 0


if __name__ == "__main__":
    base_dir = "/opt/ml/processing"

    df = pd.read_parquet(f"{base_dir}/input/dataset.parquet")

    df["sex"] = df["sex"].map(transform_sex)

    train, test = train_test_split(
        df, test_size=0.2, random_state=22, shuffle=True
    )
    test, validation = train_test_split(
        test, test_size=0.2, random_state=22, shuffle=True
    )

    train.to_csv(f"{base_dir}/train/train.csv")
    validation.to_csv(f"{base_dir}/validation/validation.csv")
