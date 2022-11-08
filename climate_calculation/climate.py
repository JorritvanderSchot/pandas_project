"""Do something"""
#Jorrit van der Schot
#%%Importing modules
import pandas as pd

#%%Defaults
fn = 'TAG_Datensatz_19000101_20221031.csv'
#%%Loading in the data
df = pd.read_csv(fn, parse_dates=["time"], index_col="time")

#%%Investigate the number of hot days (tmax ≥ 30 K) and frost days (tmin < 0 K) at those stations. 
#How do they change over the years?
def hotfrostdays(station, hotorfrost = 'hot', plot = True, begin='1900-01-01', end='2022-10-31', 
threshold=30, data=df):
    """ Function to calculate the number of hot days (tmax ≥ threshold) or
    frost days (tmax < threshold) at a particular station for a given time 
    interval. If 'plot = True', a time series of the number of hot days per 
    year will be displayed. """
    subset = data[data["station"] == station][begin:end]
    hot_days = subset[subset["t"] >= threshold]
    frost_days = subset[subset["t"] < threshold]
    no_hot_days = len(hot_days)
    no_frost_days = len(frost_days)
    if hotorfrost == 'hot':
        if plot == True:
            hot_days['substation'].resample("Y").count().plot(
                title='Days with temperature ≥ ' + str(threshold), xlim=(begin, end))
        print("{} days with temperature ≥ {} in the period {} until {}".format(
        str(no_hot_days), str(threshold), str(begin), str(end)))
    elif hotorfrost == 'frost':
        if plot == True:
            frost_days['substation'].resample("Y").count().plot(
                title='Days with temperature < ' + str(threshold))
        print("{} days with temperature < {} in the period {} until {}".format(
        str(no_frost_days), str(threshold), str(begin), str(end)))
    else:
        print('Invalid input for "hotorfrost". Please enter "hot" or "frost"')

#%%Compute the trend of monthly temperature anomalies
def monthly_T_anomalies(variable='t'):
    """ Function to plot the trend of monthly temperature anomalies for either
    T, Tmin or Tmax. """
    df_clim = df["1991-01":"2020-12"]
    clim = df_clim.groupby(df_clim.index.month).mean()
    clim.index.name = "month"
    monthly_means = df.groupby([df.index.year, df.index.month]).mean()
    monthly_means.index.names = ["year", "month"]
    anom = monthly_means - clim
    years = anom.index.get_level_values(0).astype(str)
    months = anom.index.get_level_values(1).astype(str)
    dates = pd.to_datetime(years + "-" + months + "-01")
    anom = anom.set_index(dates)
    anom[[variable]].plot(title='Monthly anomalies of ' + str(variable) +
    '\n compared to the climate normal 1991-2020')
