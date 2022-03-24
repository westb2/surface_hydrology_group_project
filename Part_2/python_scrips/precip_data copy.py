#%%
import pandas as pd
import math

#%%
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

#%%
file_suffix = "_lump_cida_forcing_leap.csv"
file_prefix = "/Users/matthewford/Desktop/Python files/AZGW_research/Merge_files/gage_precip/"

#%%
basins_data1 = []
for basin_id in basin_ids:
    file_name = file_prefix + basin_id + file_suffix
    data = pd.read_csv(file_name)
    # Add a water year column by adding 1 to the year if the month is october or afterwards
    data["Water Year"] = data["Year"] + data["Mnth"].apply(lambda x: math.floor(int(x)/10))
    output_data1 = data[['Year','Mnth',"prcp(mm/day)"]]
    output_data = data[["Water Year", "prcp(mm/day)"]]
    output_data = output_data.groupby(["Water Year"]).mean()
    output_data1 = output_data1.groupby(by=['Year','Mnth']).mean()
    output_data1 = output_data1.reset_index()
    output_data = output_data.rename(columns = {"prcp(mm/day)": basin_id + " prcp(mm/day)"})
    output_data1 = output_data1.rename(columns = {"prcp(mm/day)": basin_id + " prcp(mm/day)"})
    basins_data1.append(output_data1)
# basins_data[0]

#%%
final_output = pd.merge(basins_data1[0], basins_data1[1], on=["Year",'Mnth'])
for i in range(3, len(basins_data1)):
    final_output = pd.merge(final_output, basins_data1[i], on=["Year",'Mnth'])
#final_output.transpose()
final_output.to_csv("/Users/matthewford/Desktop/HWRS519 Surface/Group_Project(2)/python_outputs/precip_moyr.csv")
 
#%%
