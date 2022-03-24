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
file_suffix = "_streamflow_qc.csv"
file_prefix = "/Users/matthewford/Desktop/Python files/AZGW_research/Merge_files/gage_streamflow/"

# %%
#create the dataframe
basins_data1 = []
for basin_id in basin_ids:
    file_name = file_prefix + basin_id + file_suffix
    data = pd.read_csv(file_name)
    # Add a water year column by adding 1 to the year if the month is october or afterwards
    data["Water Year"] = data["YEAR"] + data["MONTH"].apply(lambda x: math.floor(int(x)/10))
    output_data = data[["Water Year", "STREAMFLOW"]]
    output_data1 = data[['YEAR', "MONTH",'DAY', 'STREAMFLOW']]
    output_data1[output_data1<0]= 0
    output_data = output_data.groupby(["Water Year"]).mean()
    output_data1 = output_data1.groupby(by=['YEAR','MONTH'])['STREAMFLOW'].mean()
    output_data1 = output_data1.to_frame().reset_index()
    output_data = output_data.rename(columns = {"STREAMFLOW": basin_id + "streamflow(cfs)"})
    output_data1 = output_data1.rename(columns = {"STREAMFLOW": basin_id + "streamflow(cfs)"})
    basins_data1.append(output_data1)
    basins_data1
# basins_data[0]

#%%
#do some finaL manipulation
final_output = pd.merge(basins_data1[0], basins_data1[1], on=["YEAR", "MONTH"])
for i in range(3, len(basins_data1)):
    final_output = pd.merge(final_output, basins_data1[i], on=["YEAR", "MONTH"])
final_output
#final_output.transpose()
final_output.to_csv("/Users/matthewford/Desktop/HWRS519 Surface/Group_Project(2)/python_outputs/streamflow_moyr.csv")
# %%
