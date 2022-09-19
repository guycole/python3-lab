import pandas as pd 

if __name__ == '__main__':
    print("main")

    manifest = {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }

    df = pd.DataFrame(manifest)

    print(df)