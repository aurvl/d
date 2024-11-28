from pycountry import countries
import pandas as pd
import re

def isoer():
    try:
        print('=======================================================')
        print("Welcome! I'm the 'isoer' function.")
        print("I return the ISO codes of any countries in an xlsx file.")
        print("⚠️ Please ensure this script is in the same directory as your dataset.")
        print('=======================================================')
        path = input("\nWhat is the path of your dataset (xlsx or csv) : ")
        country_columns = input("What is the name of the country column : ")
        
        found_csv = re.findall('.csv', path)
        found_xsx = re.findall('.xlsx', path)
        if found_csv:
            data = pd.read_csv(path)
        elif found_xsx:
            data = pd.read_excel(path)
        else:
            print("Sorry, I don't know how to read this file format")
        data = pd.read_excel(path)
        def get_iso_code(country_name):
            try:
                return countries.lookup(country_name).alpha_3
            except LookupError:
                return None

        # Ajouter une colonne avec les codes ISO
        data['ISO_Code'] = data[country_columns].apply(get_iso_code)
        data.to_excel('data.xlsx', index=False)
        return print("\nYour dataset have been created 😊 Enjoy !")
    except Exception:
        print("\n⚠️⚠️⚠️An error occurred 😣 Please retry !\n")
        return isoer()
isoer()