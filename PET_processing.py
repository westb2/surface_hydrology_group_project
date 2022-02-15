#%%
#import needed packages
import pandas as pd
import math

# %%
#create a list of the basin ids
basin_ids = [
    "09480000",
    "11151300",
    "11098000",
    "10172700",
    "08194200",
    "08267500",
    "06154410",
    "02235200",
    "02177000",
    "07315200",
    "12041200",
    "10259000"
]

# %%
#define the file prefixes 
file_suffix = "_lump_cida_forcing_leap.csv"
file_prefix = "/Users/matthewford/Desktop/Python files/AZGW_research/Merge_files/gage_precip/"

# %%
#create the dataframe
basins_data = []
for basin_id in basin_ids:
    file_name = file_prefix + basin_id + file_suffix
    data = pd.read_csv(file_name)
    # Add a water year column by adding 1 to the year if the month is october or afterwards
    data["Water Year"] = data["Year"] + data["Mnth"].apply(lambda x: math.floor(int(x)/10))
    output_data = data[["Water Year", "tmax(C)", "tmin(C)"]]
    output_data = output_data.groupby(["Water Year"]).mean()
    output_data = output_data.rename(columns = {"tmax(C)": basin_id + "tmax(C)"})
    output_data = output_data.rename(columns = {"tmin(C)": basin_id + "tmin(C)"})
    basins_data.append(output_data)
# basins_data[0]

#%%
#do some finaL manipulation
final_output = pd.merge(basins_data[0], basins_data[1], on="Water Year")
for i in range(2, len(basins_data)):
    final_output = pd.merge(final_output, basins_data[i], on="Water Year")
final_output.transpose()
final_output.to_csv("/Users/matthewford/Desktop/Python files/AZGW_research/Merge_files/temp_mean.csv")
# %%
