import tkinter as tk
from tkinter import ttk

import pickle
import pandas as pd


# Create the main window
root = tk.Tk()
root.title("User Information")

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
age_label.pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack()


# Gender input
gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
gender_combo = ttk.Combobox(root, textvariable=gender_var, width=30)
gender_combo['values'] = ("Male", "Female")
gender_combo.pack()

# Education input
educ = ["Less than 1st grade", "1st - 4th grade", "5th or 6th", \
        "7th or 8th", "9th", "10th", "11th", "12th grade NO DIPLOMA", \
        "High school graduate, diploma or GED", "Some college but no degree", \
        "Associate degree -- occupational/vocational", "Associate degree -- academic program", \
        "Bachelor's degree (e.g. BA,AB,BS)", "Master's degree (e.g. MA,MS,MEng,Med,MSW,MBA)", \
        "Professional school deg. (e.g. MD,DDS,DVM,LLB,JD)", \
        "Doctorate degree (e.g. PhD, EdD)"]
education_label = tk.Label(root, text="Education level:")
education_label.pack()
education_var = tk.StringVar()
education_combo = ttk.Combobox(root, textvariable=education_var, width=30)
education_combo['values'] = (tuple(educ))
education_combo.pack()

# Race input
race = ["White ","Black ","American Indian ","Asian only","Hawaiian/Pacific Islander only","White-Black","White-AI ","White-Asian ","White-Hawaiian ","Black-AI","Black-Asian","Black-HP","AI-Asian ","AI-HP","Asian-HP ","W-B-AI ","W-B-A ","W-B-HP ","W-AI-A ","W-AI-HP ","W-A-HP ","B-AI-A ","W-B-AI-A ","W-AI-A-HP ","Other 3 Race Combinations","Other 4 and 5 Race Combinations"]
race_label = tk.Label(root, text="Race:")
race_label.pack()
race_var = tk.StringVar()
race_combo = ttk.Combobox(root, textvariable=race_var, width=30)
race_combo['values'] = tuple(race)
race_combo.pack()


# Ethnicity input
ethnicity = ["Non-Hispanic", "Hispanic"]
ethnicity_label = tk.Label(root, text="Ethnicity:")
ethnicity_label.pack()
ethnicity_var = tk.StringVar()
ethnicity_combo = ttk.Combobox(root, textvariable=ethnicity_var, width=30)
ethnicity_combo['values'] = tuple(ethnicity)
ethnicity_combo.pack()

# Marital input
marital = ["Married civilian spouse present", "Married AF spouse present", "Married spouse absent or separated", "Widowed", "Divorced", "Separated", "Never Married"]
marital_label = tk.Label(root, text="Marital status:")
marital_label.pack()
marital_var = tk.StringVar()
marital_combo = ttk.Combobox(root, textvariable=marital_var, width=30)
marital_combo['values'] = tuple(marital)
marital_combo.pack()

# Citizenship input
citizenship = ["Native, born in US", "Native, born in Puerto Rico or US Outlying Area", "Native, born abroad of American Parent(s)", "Foreign born, US citizen by naturalization", "Foreign born, Not a citizen of the US"]
citizenship_label = tk.Label(root, text="Citizenship status:")
citizenship_label.pack()
citizenship_var = tk.StringVar()
citizenship_combo = ttk.Combobox(root, textvariable=citizenship_var, width=30)
citizenship_combo['values'] = tuple(citizenship)
citizenship_combo.pack()

# FT - PT status
ftpt = ['FT Hours (35+), Usually FT', 'Not At Work, Usually FT', 'PT hrs, Usually PT For Non-Economic', 'PT For Economic Reasons, Usually FT',  'PT For Non-Economic Reasons, Usually FT', 'PT Hours, Usually PT For Economic Reasons', 'Not at work, Usually Part-Time', 'FT hrs, Usually PT For Non-Economic','FT Hours, Usually PT For Economic Reas']
ftpt_label = tk.Label(root, text="Full-time/Part-time:")
ftpt_label.pack()
ftpt_var = tk.StringVar()
ftpt_combo = ttk.Combobox(root, textvariable=ftpt_var, width=30)
ftpt_combo['values'] = tuple(ftpt)
ftpt_combo.pack()

# Sector Input
sector = ['Private, For Profit', 'Government - State', 'Government - Local', \
            'Government - Federal', 'Private, Nonprofit']
sector_label = tk.Label(root, text="Sector:")
sector_label.pack()
sector_var = tk.StringVar()
sector_combo = ttk.Combobox(root, textvariable=sector_var, width=30)
sector_combo['values'] = tuple(sector)
sector_combo.pack()

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
industry_label.pack()
industry_var = tk.StringVar()
industry_combo = ttk.Combobox(root, textvariable=industry_var, width=30)
industry_combo['values'] = tuple(sorted(industry))
industry_combo.pack()

# Occupation input
with open('occ.pkl', 'rb') as file:
    occ = pickle.load(file)
occupation_label = tk.Label(root, text="Occupation:")
occupation_label.pack()
occupation_var = tk.StringVar()
occupation_combo = ttk.Combobox(root, textvariable=occupation_var, width=30)
occupation_combo['values'] = tuple(sorted(occ))
occupation_combo.pack()

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

# Create the first Combobox for categories
state_label = tk.Label(root, text="State:")
state_label.pack()
state_var = tk.StringVar()
states = sorted(cbsa_df['State'].unique().tolist())
states_combobox = ttk.Combobox(root, textvariable=state_var, values=states, width=30)
states_combobox.pack()
# states_combobox.grid(row=0, column=0, padx=10, pady=10)

# Create the second Combobox for subcategories
city_label = tk.Label(root, text="City:")
city_label.pack()
city_var = tk.StringVar()
city_combobox = ttk.Combobox(root, textvariable=city_var, width=30)
city_combobox.pack()
# city_combobox.grid(row=0, column=1, padx=10, pady=10)

# Set event handler for category selection
states_combobox.bind("<<ComboboxSelected>>", on_state_selected)

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

    gender = gender_map[gender_var.get()]
    education = educ_map[education_var.get()]
    race = race_map[race_var.get()]
    ethnicity = ethnic_map[ethnicity_var.get()]
    citizenship = citizenship_var.get()
    marital = marital_map[marital_var.get()]
    ftpt = ftpt_var.get()

    sector = sector_var.get()
    industry = industry_var.get()
    occ = occupation_var.get()
    info_label.config(text = \
                      f"Age: {age}, type: {type(age)} \n \
                        CBSA: {cbsa}, type: {type(cbsa)} \n \
                        Gender: {gender}, type: {type(gender)} \n \
                        Education: {education}, type: {type(education)} \n \
                        Race: {race}, type: {type(race)} \n \
                        Ethnicity: {ethnicity}, type: {type(ethnicity)} \n \
                        Citizenship: {citizenship}, type: {type(citizenship)} \n \
                        Marital Status: {marital}, type: {type(marital)} \n \
                        FT-PT: {ftpt}, type: {type(ftpt)} \n \
                        Sector: {sector}, type: {type(sector)} \n \
                        Industry: {industry}, type: {type(industry)} \n \
                        Occupation: {occ}, type: {type(occ)} \n ")


# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Display collected information
info_label = tk.Label(root, text="")
info_label.pack()

    
# def selection_changed(event):
#     selected_item = combo_var.get()
#     result_label.config(text=f"Selected Item: {selected_item}")


# Create a button to display the selected item
# button = tk.Button(root, text="Show Selection", command=selection_changed)
# button.pack()

# # Create a label to display the selected item
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Bind the event to the function
# combo.bind("<<ComboboxSelected>>", selection_changed)

# # Hobbies Input
# hobbies_label = tk.Label(root, text="Hobbies:")
# hobbies_label.pack()
# hobby_vars = [tk.StringVar() for _ in range(3)]
# hobby_checkboxes = [
#     tk.Checkbutton(root, text="Reading", variable=hobby_vars[0]),
#     tk.Checkbutton(root, text="Gaming", variable=hobby_vars[1]),
#     tk.Checkbutton(root, text="Cooking", variable=hobby_vars[2])
# ]
# for checkbox in hobby_checkboxes:
#     checkbox.pack()


# Start the main loop
if __name__ == "__main__":
    root.mainloop()