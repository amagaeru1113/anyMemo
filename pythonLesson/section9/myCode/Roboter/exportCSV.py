import os
import csv

import pandas as pd


def input_restaurant_count(restaurant_name, csv_name):
    fieldC_name, fieldC_count = "Name", "Count"
    fieldnames = [fieldC_name, fieldC_count]

    if not os.path.exists(csv_name):  # ファイルが存在しなかったら最初のcsvを作る
        with open(csv_name, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({fieldC_name: restaurant_name, fieldC_count: 1})
    else:
        df = pd.read_csv(csv_name)
        if not df.query("Name == @restaurant_name").empty:  # 既存の店名 -> add count 1
            add_count = df.loc[df[fieldC_name] == restaurant_name, fieldC_count] + 1
            df.loc[df.Name == restaurant_name, fieldC_count] = add_count
            df.to_csv(csv_name, columns=fieldnames, index=False)
            # index=Falseにしないと余計なindexが増えていく

        else:  # 新規の店名 -> add df row
            add_restaurant = pd.DataFrame([[restaurant_name, 1]], columns=fieldnames)
            df = df.append(add_restaurant)
            df.to_csv(csv_name, columns=fieldnames, index=False)
