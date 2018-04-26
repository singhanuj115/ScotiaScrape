import glob, os
import pandas as pd

from pandas import DataFrame, ExcelWriter

writer = ExcelWriter("/Users/weirdguy/PycharmProjects/CrawlEnviron/__crawler/__crawler/spiders/data/compiled.xlsx")

for filename in glob.glob("/Users/weirdguy/PycharmProjects/CrawlEnviron/__crawler/__crawler/spiders/data/*cleaned.csv"):
    df_csv = pd.read_csv(filename)

    (_, f_name) = os.path.split(filename)
    (f_short_name, _) = os.path.splitext(f_name)
    f_short_name = f_short_name.split("_")[0]
    df_csv.to_excel(writer, f_short_name, index=False)

writer.save()