import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pickle
import pandas as pd
import numpy as np
import json

# Create the main window
from joblib import dump, load
rf5 = load('random_forest4.joblib') 

stfips_json = json.load(open('stfips.json'))
prcitshp_json = json.load(open('prcitshp.json'))
class94_json = json.load(open('class94.json'))
dind02_json = json.load(open('dind02.json'))
docc00_json = json.load(open('docc00.json'))
ftpt94_json = json.load(open('ftpt94.json'))
occ_json = json.load(open('occ.json'))


root = tk.Tk()
root.title("Salary & COL Estimator 1.0")


##############################################
# CBSA data pre-processing
##############################################
cbsa_df = pd.read_csv('cost of living with cbsa with manual completed data2.csv', header=None, names=["City", "State", "CBSA"])
col_df = pd.read_csv('Cost of living data.csv', header=None, names=["City", "State", "col_index"])

##############################################
# Input fields
##############################################

# Age Input
age_label = tk.Label(root, text="Age:")
age_label.grid(row = 0, column = 0, pady = 2)
age_entry = tk.Entry(root, width=30)
age_entry.grid(row = 0, column = 1, pady = 2)


# Gender input
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row = 1, column = 0, pady = 2)
gender_var = tk.StringVar()
gender_combo = ttk.Combobox(root, textvariable=gender_var, width=30)
gender_combo['values'] = ("Male", "Female")
gender_combo.grid(row = 1, column = 1, pady = 2)

# Education input
educ = ["Less than 1st grade", "1st - 4th grade", "5th or 6th", \
        "7th or 8th", "9th", "10th", "11th", "12th grade NO DIPLOMA", \
        "High school graduate, diploma or GED", "Some college but no degree", \
        "Associate degree -- occupational/vocational", "Associate degree -- academic program", \
        "Bachelor's degree (e.g. BA,AB,BS)", "Master's degree (e.g. MA,MS,MEng,Med,MSW,MBA)", \
        "Professional school deg. (e.g. MD,DDS,DVM,LLB,JD)", \
        "Doctorate degree (e.g. PhD, EdD)"]
education_label = tk.Label(root, text="Education level:")
education_label.grid(row = 2, column = 0, pady = 2)
education_var = tk.StringVar()
education_combo = ttk.Combobox(root, textvariable=education_var, width=30)
education_combo['values'] = (tuple(reversed(educ)))
education_combo.grid(row = 2, column = 1, pady = 2)

# Race input
race = ["White ","Black ","American Indian ","Asian only","Hawaiian/Pacific Islander only","White-Black","White-AI ","White-Asian ","White-Hawaiian ","Black-AI","Black-Asian","Black-HP","AI-Asian ","AI-HP","Asian-HP ","W-B-AI ","W-B-A ","W-B-HP ","W-AI-A ","W-AI-HP ","W-A-HP ","B-AI-A ","W-B-AI-A ","W-AI-A-HP ","Other 3 Race Combinations","Other 4 and 5 Race Combinations"]
race_label = tk.Label(root, text="Race:")
race_label.grid(row = 3, column = 0, pady = 2)
race_var = tk.StringVar()
race_combo = ttk.Combobox(root, textvariable=race_var, width=30)
race_combo['values'] = tuple(race)
race_combo.grid(row = 3, column = 1, pady = 2)


# Ethnicity input
ethnicity = ["Non-Hispanic", "Hispanic"]
ethnicity_label = tk.Label(root, text="Ethnicity:")
ethnicity_label.grid(row = 4, column = 0, pady = 2)
ethnicity_var = tk.StringVar()
ethnicity_combo = ttk.Combobox(root, textvariable=ethnicity_var, width=30)
ethnicity_combo['values'] = tuple(ethnicity)
ethnicity_combo.grid(row = 4, column = 1, pady = 2)

# Marital input
marital = ["Married civilian spouse present", "Married AF spouse present", "Married spouse absent or separated", "Widowed", "Divorced", "Separated", "Never Married"]
marital_label = tk.Label(root, text="Marital status:")
marital_label.grid(row = 5, column = 0, pady = 2)
marital_var = tk.StringVar()
marital_combo = ttk.Combobox(root, textvariable=marital_var, width=30)
marital_combo['values'] = tuple(marital)
marital_combo.grid(row = 5, column = 1, pady = 2)

# Citizenship input
citizenship = ['Native, Born In US', 'Foreign Born, US Cit By Naturalization',\
       'Foreign Born, Not a US Citizen', \
       'Native, Born Abroad Of US Parent(s)',\
       'Native, Born in PR or US Outlying Area']
citizenship_label = tk.Label(root, text="Citizenship status:")
citizenship_label.grid(row = 6, column = 0, pady = 2)
citizenship_var = tk.StringVar()
citizenship_combo = ttk.Combobox(root, textvariable=citizenship_var, width=30)
citizenship_combo['values'] = tuple(citizenship)
citizenship_combo.grid(row = 6, column = 1, pady = 2)

# FT - PT status
ftpt = ['FT Hours (35+), Usually FT', 'Not At Work, Usually FT', 'PT hrs, Usually PT For Non-Economic', 'PT For Economic Reasons, Usually FT',  'PT For Non-Economic Reasons, Usually FT', 'PT Hours, Usually PT For Economic Reasons', 'Not at work, Usually Part-Time', 'FT hrs, Usually PT For Non-Economic','FT Hours, Usually PT For Economic Reas']
ftpt_label = tk.Label(root, text="Full-time/Part-time:")
ftpt_label.grid(row = 7, column = 0, pady = 2)
ftpt_var = tk.StringVar()
ftpt_combo = ttk.Combobox(root, textvariable=ftpt_var, width=30)
ftpt_combo['values'] = tuple(ftpt)
ftpt_combo.grid(row = 7, column = 1, pady = 2)



# Sector Input
sector = ['Private, For Profit', 'Government - State', 'Government - Local', \
            'Government - Federal', 'Private, Nonprofit']
sector_label = tk.Label(root, text="Sector:")
sector_label.grid(row = 8, column = 0, pady = 2)
sector_var = tk.StringVar()
sector_combo = ttk.Combobox(root, textvariable=sector_var, width=30)
sector_combo['values'] = tuple(sector)
sector_combo.grid(row = 8, column = 1, pady = 2)

# Industry input:
industry = ['Hospitals', 'Educational services', 'Construction',
       'Administrative and support services', 'Public Administration',
       'Retail trade', 'Social assistance', 'Finance',
       'Health care services , except hospitals', 'Mining',
       'Accomodation', 'Food services and drinking places', 'Real Estate',
       'Wholesale trade', 'Transportation equipment manufacturing',
       'Professional and Technical services', 'Telecommunications',
       'Primary metals and fabricated metal products',
       'Personal and laundry services', 'Utilities',
       'Computer and electronic products', 'Insurance',
       'Furniture and fixtures manufacturing', 'Machinery manufacturing',
       'Beverage and tobacco products', 'Transportation and warehousing',
       'Paper and printing',
       'Forestry, logging, fishing, hunting, and trapping',
       'Food manufacturing', 'Chemical manufacturing',
       'Broadcasting (except internet)', 'Private households',
       'Repair and maintenance',
       'Membership associations and organizations',
       'Arts, entertainment, and recreation',
       'Electrical equipment, appliance manufacturing',
       'Textile, apparel, and leather manufacturing',
       'Waste management and remediation services',
       'Other information services',
       'Miscellaneous and not specified manufacturing',
       'Publishing industries (except internet)', 'Agriculture',
       'Rental and leasing services', 'Nonmetallic mineral products',
       'Plastics and rubber products', 'Wood products',
       'Management of companies and enterprises',
       'Motion picture and sound recording industries',
       'Internet publishing and broadcasting',
       'Petroleum and coal products',
       'Internet service providers and data processing services']
industry_label = tk.Label(root, text="Industry:")
industry_label.grid(row = 9, column = 0, pady = 2)
industry_var = tk.StringVar()
industry_combo = ttk.Combobox(root, textvariable=industry_var, width=30)
industry_combo['values'] = tuple(sorted(industry))
industry_combo.grid(row = 9, column = 1, pady = 2)

# High level occupation input
docc = ['Office and administrative support occupations',
       'Education, training, and library occupations',
       'Construction and extraction occupations',
       'Business and financial operations occupations',
       'Production occupations',
       'Food preparation and serving related occupations',
       'Management occupations', 'Healthcare support occupations',
       'Legal occupations', 'Sales and related occupations',
       'Architecture and engineering occupations',
       'Community and social service occupations',
       'Healthcare practitioner and technical occupations',
       'Transportation and material moving occupations',
       'Computer and mathematical science occupations',
       'Installation, maintenance, and repair occupations',
       'Protective service occupations',
       'Arts, design, entertainment, sports, and media occupations',
       'Personal care and service occupations',
       'Farming, fishing, and forestry occupations',
       'Building and grounds cleaning and maintenance occupations',
       'Life, physical, and social science occupations']
docc_label = tk.Label(root, text="Occupation group:")
docc_label.grid(row = 10, column = 0, pady = 2)
docc_var = tk.StringVar()
docc_combo = ttk.Combobox(root, textvariable=docc_var, width=30)
docc_combo['values'] = tuple(sorted(docc))
docc_combo.grid(row = 10, column = 1, pady = 2)

# Occupation input
with open('occ.pkl', 'rb') as file:
    occ = pickle.load(file)
occupation_label = tk.Label(root, text="Occupation:")
occupation_label.grid(row = 11, column = 0, pady = 2)
occupation_var = tk.StringVar()
occupation_combo = ttk.Combobox(root, textvariable=occupation_var, width=30)
occupation_combo['values'] = tuple(sorted(occ))
occupation_combo.grid(row = 11, column = 1, pady = 2)

# State and city input
def on_state_selected(event):
    selected_state = states_combobox.get()
    
    # Update the second Combobox based on the selected category
    update_city_combobox(selected_state)

def update_city_combobox(selected_state):
    # Clear the current values in the subcategory Combobox
    city_combobox.set('')

    city_list = sorted(cbsa_df.loc[cbsa_df['State'] == selected_state, 'City'].tolist())

    city_combobox['values'] = city_list

# Create the first Combobox for categories (states)
state_label = tk.Label(root, text="Primary State:")
state_label.grid(row = 12, column = 0, pady = 2)
state_var = tk.StringVar()
states = sorted(cbsa_df['State'].unique().tolist())
states_combobox = ttk.Combobox(root, textvariable=state_var, values=states, width=30)
states_combobox.grid(row = 12, column = 1, pady = 2)


# Create the second Combobox for subcategories (cities)
city_label = tk.Label(root, text="Primary City:")
city_label.grid(row = 13, column = 0, pady = 2)
city_var = tk.StringVar()
city_combobox = ttk.Combobox(root, textvariable=city_var, width=30)
city_combobox.grid(row = 13, column = 1, pady = 2)

# Set event handler for category selection
states_combobox.bind("<<ComboboxSelected>>", on_state_selected)


def on_sec_state_selected(event):
    sec_selected_state = sec_states_combobox.get()
    
    # Update the second Combobox based on the selected category
    update_sec_city_combobox(sec_selected_state)

def update_sec_city_combobox(sec_selected_state):
    # Clear the current values in the subcategory Combobox
    sec_city_combobox.set('')

    sec_city_list = sorted(cbsa_df.loc[cbsa_df['State'] == sec_selected_state, 'City'].tolist())

    sec_city_combobox['values'] = sec_city_list

# Create the secondary state combobox
sec_state_label = tk.Label(root, text="Secondary State:")
sec_state_label.grid(row = 14, column = 0, pady = 2)
sec_state_var = tk.StringVar()
sec_states = sorted(cbsa_df['State'].unique().tolist())
sec_states_combobox = ttk.Combobox(root, textvariable=sec_state_var, values=sec_states, width=30)
sec_states_combobox.grid(row = 14, column = 1, pady = 2)


# Create the second Combobox for subcategories (cities)
sec_city_label = tk.Label(root, text="Secondary City:")
sec_city_label.grid(row = 15, column = 0, pady = 2)
sec_city_var = tk.StringVar()
sec_city_combobox = ttk.Combobox(root, textvariable=sec_city_var, width=30)
sec_city_combobox.grid(row = 15, column = 1, pady = 2)

sec_states_combobox.bind("<<ComboboxSelected>>", on_sec_state_selected)

##############################################
# Mappings
##############################################
gender_map = {"Male" : 1, "Female" : 2}
educ_map = {val : idx + 31 for idx, val in enumerate(educ)}
race_map = {val : idx + 1 for idx, val in enumerate(race)}
ethnic_map = {val : idx for idx, val in enumerate(ethnicity)}
marital_map = {val : idx + 1 for idx, val in enumerate(marital)}


##############################################
# Submission and output
##############################################
def submit():
    # Get values from input fields
    age = float(age_entry.get())
    
    state = state_var.get()
    city = city_var.get()
    cbsa = int(cbsa_df.loc[(cbsa_df['State'] == state) & (cbsa_df['City'] == city), 'CBSA'].values[0])
    col = col_df.loc[(col_df['State'].str.upper() == state) & (col_df['City'].str.upper() == city), 'col_index'].values[0]

    gender = gender_map[gender_var.get()]
    education = educ_map[education_var.get()]
    race = race_map[race_var.get()]
    ethnicity = ethnic_map[ethnicity_var.get()]
    citizenship = citizenship_var.get()
    marital = marital_map[marital_var.get()]
    ftpt = ftpt_var.get()

    sector = sector_var.get()
    industry = industry_var.get()
    docc = docc_var.get()
    occ = occupation_var.get()


    in_list = [cbsa, age,gender, education, race,ethnicity,marital]
    stfips_class = list(stfips_json.keys())[list(stfips_json.values()).index(state)]
    prcitshp_class =   list(prcitshp_json.keys())[list(prcitshp_json.values()).index(citizenship)]
    ftpt94_class = list(ftpt94_json.keys())[list(ftpt94_json.values()).index(ftpt)]
    class94_class =   list(class94_json.keys())[list(class94_json.values()).index(sector)]
    docc00_class = list(docc00_json.keys())[list(docc00_json.values()).index(docc)]
    dind02_class =   list(dind02_json.keys())[list(dind02_json.values()).index(industry)]
    occ_class =   list(occ_json.keys())[list(occ_json.values()).index(occ)]
    in_list += [stfips_class,  prcitshp_class, ftpt94_class,class94_class,docc00_class,dind02_class ,occ_class]

    sec_state = sec_state_var.get()
    sec_city = sec_city_var.get()

    sec_in_list = []
    if sec_state and sec_city:
        sec_cbsa = int(cbsa_df.loc[(cbsa_df['State'] == sec_state) & (cbsa_df['City'] == sec_city), 'CBSA'].values[0])
        sec_in_list = [sec_cbsa, age,gender, education, race,ethnicity,marital]
        sec_stfips_class = list(stfips_json.keys())[list(stfips_json.values()).index(sec_state)]
        sec_in_list += [sec_stfips_class,  prcitshp_class, ftpt94_class,class94_class,docc00_class,dind02_class ,occ_class]


    pred = rf5.predict(np.array(in_list).reshape(1, -1))
    if sec_in_list:
        sec_pred = rf5.predict(np.array(sec_in_list).reshape(1, -1))

    # print(pred)
    

    #AL,33860,49.0,1,41,2,0.0,1,"Native, Born In US","FT Hours (35+), Usually FT","Private, For Profit",865.0,Construction and extraction occupations,Construction,Electricians,44980.0,63421.799999999996
    # messagebox.showinfo("Message Box", f"Your salary in {city}, {state} is predicted to be: \033{salary_formatter(pred[0])}\033")
    if sec_state and sec_city:
        sec_col = col_df.loc[(col_df['State'].str.upper() == sec_state) & (col_df['City'].str.upper() == sec_city), 'col_index'].values[0]
        info_label.config(text = \
                    f"Your salary in {city}, {state} is predicted to be: {salary_formatter(pred[0])}\nCost of living index of {city}, {state} is: {col}\nAffordability Index: {pred[0]/1000/col:.3f}\n\nYour salary in {sec_city}, {sec_state} is predicted to be: {salary_formatter(sec_pred[0])}\nCost of living index of {sec_city}, {sec_state} is: {sec_col}\nAffordability Index: {sec_pred[0]/1000/sec_col:.3f}\n")
    else:
        info_label.config(text = \
                      f"Your salary in {city}, {state} is predicted to be: {salary_formatter(pred[0])}\nCost of living index of {city}, {state} is: {col}\nAffordability Index: {pred[0]/1000/col:.3f}")
    
    sec_states_combobox.set('')
    sec_city_combobox.set('')
    


# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(pady=20)

# Display collected information
info_label = tk.Label(root, text="", anchor="w", justify="left")
info_label.grid(row = 16, column = 1, pady=10)


##############################################
# Helper functions
##############################################

def salary_formatter(sal):
    return f'${sal / 1000:.1f}K'



# def selection_changed(event):
#     selected_item = combo_var.get()
#     result_label.config(text=f"Selected Item: {selected_item}")


# Create a button to display the selected item
# button = tk.Button(root, text="Show Selection", command=selection_changed)
# button.grid()

# # Create a label to display the selected item
# result_label = tk.Label(root, text="")
# result_label.grid()

# # Bind the event to the function
# combo.bind("<<ComboboxSelected>>", selection_changed)

# # Hobbies Input
# hobbies_label = tk.Label(root, text="Hobbies:")
# hobbies_label.grid()
# hobby_vars = [tk.StringVar() for _ in range(3)]
# hobby_checkboxes = [
#     tk.Checkbutton(root, text="Reading", variable=hobby_vars[0]),
#     tk.Checkbutton(root, text="Gaming", variable=hobby_vars[1]),
#     tk.Checkbutton(root, text="Cooking", variable=hobby_vars[2])
# ]
# for checkbox in hobby_checkboxes:
#     checkbox.grid()


# Start the main loop
if __name__ == "__main__":
    root.mainloop()