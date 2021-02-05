import Constants
import functions
import xlwt
from xlwt import Workbook

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

    functions.output_csv(rounded_vals)

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


    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    states = list(State_vals.keys())
    for i in range(len(states)):
        sheet1.write(i, 0, states[i])
        sheet1.write(i, 1, str(State_vals[states[i]]['pop']/State_vals[states[i]]['light']))
    wb.save("data.xls")
