import os
import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.mode.chained_assignment = None


def get_apcte_v1_classification(fnm="clasified_assets_v1.csv"):
    fldr = os.path.join(os.getcwd(), "_input_data", "apcte_solution")
    csv_filnme = os.path.join(fldr, fnm)

    df_res = pd.read_csv(csv_filnme)

    return df_res


if __name__ == '__main__':
    df_res = get_apcte_v1_classification()
