import pandas as pd
import matplotlib .pyplot as plt
#print("A")
df = pd.read_csv('/Users/jason/Downloads/p_week02_source/data/samples.csv')

# plot_default = df.plot(x="Rank", y=["P25th", "Median", "P75th"])
# plt.show()
# median_column = df["Median"]
# plot_median_hist = median_column.plot(kind="hist") 
# plt.show()
# top_5 = df.sort_values(by="Median", ascending=False).head()
# plot_median_top5 = top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
# plt.show()
# top_medians = df[df["Median"] > 60000].sort_values("Median")
# plot_three_bars = top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
# plt.show()
# plot_scatter = df.plot(x="Median", y="Unemployment_rate", kind="scatter")
# plt.show()
# cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()
# plot_grouping = cat_totals.plot(kind="barh", fontsize=4)
# plt.show()
# small_cat_totals = cat_totals[cat_totals < 100_000]
# big_cat_totals = cat_totals[cat_totals > 100_000]
# small_sums = pd.Series([small_cat_totals.sum()], index=["Other"])
# big_cat_totals = big_cat_totals.append(small_sums)
# plot_pie = big_cat_totals.plot(kind="pie", label="")
# plt.show()
df = pd.read_csv('/Users/jason/Downloads/p_week02_source/data/covid-19-cases.csv')
# group by country column and sum over the different states/regions of each country
grouped = df.groupby('Country/Region')
df_countries = grouped.sum()
def make_plot(country):
#"""make the bar plot of case numbers and change in numbers line plot.""" # extract the series corresponding to the case numbers for country
    c_df = df_countries.loc[country, df_countries.columns[3:]]
    # convert index to a proper datetime object
    c_df.index = pd.to_datetime(c_df.index)
    # get the number of column
    n = len(c_df)
    # setting bar with corresponding values
    plt.bar(range(n), c_df.values)
        # setting x and y label
    plt.xlabel('Days') 
    plt.ylabel('Confirmed cases, $N$')
    # add a title reporting the latest number of cases available
    title = '{}\n{} cases on {}'.format(country, c_df[-1], c_df.index[-1].strftime('%d %B %Y'))
    plt.suptitle(title)
# make plot for a corresponding country
make_plot('Vietnam')
plt.show()