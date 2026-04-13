import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\DA Projects\AB Testing project\ab_data.csv\ab_data.csv")
#print(df.head(100))
#print(df.shape)
#print(df.info())
df_clean = df[
    ((df["group"] == "control") & (df["landing_page"] == "old_page")) |
    ((df["group"] == "treatment") & (df["landing_page"] == "new_page"))
]
#print(df_clean.head())
#print(df_clean.info())
#print(df_clean['user_id'].duplicated().sum())
df_clean = df_clean.drop_duplicates(subset="user_id")
#print(df_clean['user_id'].duplicated().sum())
#print(df_clean.info())
#print(df_clean.shape)

df_countries = pd.read_csv(r"D:\DA Projects\AB Testing project\ab_data.csv\countries.csv")
#print(df_countries.head())
#print(df_countries.info())
#print(df_countries['user_id'].duplicated().sum())
df_countries = df_countries.drop_duplicates(subset="user_id")
#print(df_countries.info())
#print(df_countries['user_id'].duplicated().sum())

df_merged = df_clean.merge(
    df_countries,
    on = "user_id",
    how = "left"
)
print(df_merged)
print(df_merged.groupby("group")["converted"].agg(["sum","count","mean"]))

from statsmodels.stats.proportion import proportions_ztest
conversions = df_clean.groupby('group')['converted'].sum()
users = df_clean.groupby('group')['converted'].count()
z_stat, p_value = proportions_ztest(conversions, users)

print("z-test statistic: ", z_stat)
print("p-value: ", p_value)

p_control = df_merged[df_merged["group"] == "control"]["converted"].sum() / df_merged[df_merged["group"] == "control"]["converted"].count()
#print(r"p_control :",p_control)
p_treatment = df_merged[df_merged["group"] == "treatment"]["converted"].sum() / df_merged[df_merged["group"] == "treatment"]["converted"].count()
#print(r"p_treatment :",p_treatment)
#p_control = 17489 / 145274
#p_treatment = 17264 / 145311

# Difference
diff = p_treatment - p_control
# Standard error
se = np.sqrt(
    (p_control * (1 - p_control) / df_merged[df_merged["group"] == "control"]["converted"].count()) +
    (p_treatment * (1 - p_treatment) / df_merged[df_merged["group"] == "treatment"]["converted"].count())
)
# Z for 95% confidence
z = 1.96

# Confidence Interval
lower = diff - z * se
upper = diff + z * se
print(r"The confidence interval for our data is :","(",lower,",",upper,")")
