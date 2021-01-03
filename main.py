import Constants
import functions

if __name__ == "__main__":

    rounded_vals = {}
    global country_data
    global state_data
    global India
    global States
    Constants.initialize()

    functions.clean_round_coords(r"C:\Users\vtham\Downloads\SRP_Light+Pop\clipped_ispop.xyz", "pop", "light",
                                 rounded_vals)
    functions.clean_round_coords(r"C:\Users\vtham\Downloads\SRP_Light+Pop\India_2012_VIIRS.xyz", "light", "pop",
                                 rounded_vals)

    State_vals = {}  # Format: {"State": {"pop": __, "light" __}...}
    for i in rounded_vals.keys():
        coords = i.split("_")
        coords[0] = float(coords[0])
        coords[1] = float(coords[1])
        print(coords)
        if functions.Check_State(coords) in State_vals.keys():
            State_vals[functions.Check_State(coords)]['pop'] += rounded_vals[i]['pop']
            State_vals[functions.Check_State(coords)]['light'] += rounded_vals[i]['light']
        else:
            State_vals[functions.Check_State(coords)] = {'pop': rounded_vals[i]['pop'],
                                                         'light': rounded_vals[i]['light']}

    print(State_vals)

    # functions.output_csv(rounded_vals)
#######################################################################################################################
# 2.5 Check whether the coordinate is in India, if not skip
#######################################################################################################################

#######################################################################################################################
# 3. Round the latitude and longitude for each "point"/element to the 4th decimal point.
#######################################################################################################################

#######################################################################################################################
# 4. Create a key in the dict "rounded_vals" for that rounded latitude and longitude and add the band number to that
#     part of the dictionary.  If we end up with multiple co-ordinates rounding to the same value, then add the
#     band numbers for both. Final dictionary would have the following format:
#     {"Values": {"Lat_long": {'pop': dd, 'light': dd}... }
#######################################################################################################################

#######################################################################################################################
# 5. Create a new key in the pop, light dictionary within "rounded_vals" by dividing light by pop. The new key will be
#    "l/p"
#######################################################################################################################

#######################################################################################################################
# 6. Create a new text file called "poverty.xyz" and for each line the format will be...
#    "Latitude Longitude l/p"
#######################################################################################################################


#######################################################################################################################
# 2. Open the relevant file (whether that be light intensity or population density)
# The format of the file is ascii with "latitude longitude band_value"
# In each file, it provides the map co-ordinates, and the relevant light intensity or population density for that point.
#######################################################################################################################

#######################################################################################################################
# 3. Round the latitude and longitude for each "point"/element to the 4th decimal point.
#######################################################################################################################

#######################################################################################################################
# 4. Create a key in the dict "rounded_vals" for that rounded latitude and longitude and add the band number to that
#     part of the dictionary.  If we end up with multiple co-ordinates rounding to the same value, then add the
#     band numbers for both. Final dictionary would have the following format:
#     {"Values": {"Lat_long": {'pop': dd, 'light': dd}... }
#######################################################################################################################

#######################################################################################################################
# 5. Create a new key in the pop, light dictionary within "rounded_vals" by dividing light by pop. The new key will be
#    "l/p"
#######################################################################################################################

#######################################################################################################################
# 6. Create a new text file called "poverty.xyz" and for each line the format will be...
#    "Latitude Longitude l/p"
#######################################################################################################################

# {None: {'pop': 3620163.0, 'light': 32638.35999527946}, 'Jammu and Kashmir': {'pop': 12456568.0,
# 'light': 147629.84996567108}, 'Himachal Pradesh': {'pop': 6864665.0, 'light': 56917.9899612125}, 'Punjab': {'pop':
# 27267522.0, 'light': 364095.34998935834}, 'Uttaranchal': {'pop': 9872953.0, 'light': 134844.7099224124},
# 'Haryana': {'pop': 25225485.0, 'light': 360913.2000644095}, 'Chandigarh': {'pop': 1330088.0,
# 'light': 12539.67999947071}, 'Uttar Pradesh': {'pop': 198102282.0, 'light': 1196895.949492529}, 'Rajasthan': {
# 'pop': 68235095.0, 'light': 785136.639719151}, 'Arunachal Pradesh': {'pop': 1466136.0, 'light': 11915.43997811526},
# 'Delhi': {'pop': 16456108.0, 'light': 247774.05008530617}, 'Sikkim': {'pop': 607281.0, 'light': 5003.439996473491},
# 'Assam': {'pop': 31233808.0, 'light': 146972.26012585498}, 'Bihar': {'pop': 103497721.0,
# 'light': 159933.91990682483}, 'West Bengal': {'pop': 90196877.0, 'light': 408875.0398449544}, 'Nagaland': {'pop':
# 1820201.0, 'light': 14790.849993985146}, 'Madhya Pradesh': {'pop': 72093158.0, 'light': 489552.20986174047},
# 'Meghalaya': {'pop': 2722337.0, 'light': 16667.019984206185}, 'Manipur': {'pop': 2533969.0,
# 'light': 6332.139990957454}, 'Jharkhand': {'pop': 32657707.0, 'light': 211346.79987068474}, 'Gujarat': {'pop':
# 59820627.0, 'light': 569686.2200032007}, 'Tripura': {'pop': 3478575.0, 'light': 27513.539950465783}, 'Mizoram': {
# 'pop': 1063227.0, 'light': 3200.4599995575845}, 'Chhattisgarh': {'pop': 25449675.0, 'light': 311824.6398261562},
# 'Orissa': {'pop': 41745978.0, 'light': 306901.9799316991}, 'Maharashtra': {'pop': 111298452.0,
# 'light': 770980.779693136}, 'Daman and Diu': {'pop': 170913.0, 'light': 4552.639999072999}, 'Dadra and Nagar
# Haveli': {'pop': 291010.0, 'light': 8813.419993488118}, 'Andhra Pradesh': {'pop': 84004300.0,
# 'light': 717866.3697655536}, 'Karnataka': {'pop': 60564172.0, 'light': 558140.6199203413}, 'Puducherry': {'pop':
# 1236383.0, 'light': 7587.960002955049}, 'Goa': {'pop': 1408972.0, 'light': 21433.470001850277}, 'Andaman and
# Nicobar': {'pop': 282382.0, 'light': 1662.6099991612136}, 'Tamil Nadu': {'pop': 71812450.0,
# 'light': 430761.2697998937}, 'Kerala': {'pop': 31528582.0, 'light': 66003.26995996758}, 'Lakshadweep': {'pop':
# 7584.0, 'light': 11.699999894946814}}
