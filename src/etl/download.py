import urllib.request, json 
import requests
import pandas as pd
from bs4 import BeautifulSoup
import unicodedata    

def extract_json_data(dataset_url):
    """Extract json data from URL and return a dictionary"""
    with urllib.request.urlopen(dataset_url) as url:
        data = json.load(url)
        return data

def extract_csv_data(dataset_url):
    """Extract csv data from URL and return dfs"""
    s = requests.get(dataset_url).content
    df_questions = pd.read_excel(
        s,
        header = None, 
        sheet_name="Questions", 
        engine="openpyxl")
    
    df_taxonomy = pd.read_excel(
        s,
        header = None, 
        sheet_name="Taxonomy", 
        engine="openpyxl")
    
    return df_questions, df_taxonomy

def html_cleaning(json_file):
    """ Remove html tags from text
            input: json data
        - These fileds will be cleaned:
            * travel_transportation
            * health
            * local_laws_and_special_circumstances
            * safety_and_security
            * entry_exit_requirements
            * destination_description
            * travel_embassyAndConsulate
            """
    feature_list = [ 'travel_transportation',
                     'health',
                     'local_laws_and_special_circumstances',
                     'safety_and_security',
                     'entry_exit_requirements',
                     'destination_description',
                     'travel_embassyAndConsulate']
    
    for idx, entry in enumerate(json_file):
        for feat in feature_list:
            raw_text = entry[feat]
            cleaned = BeautifulSoup(raw_text, "html.parser" )
            cleaned_text = cleaned.get_text(separator = ' ', strip = True)
            final_text = unicodedata.normalize("NFKD",cleaned_text)
            json_file[idx][feat] = final_text
            
    return json_file
    

if __name__ == "__main__":

    # Extract data from URL
    ### 1. Country Travel Information dataset (HTML)
    url_cti = "https://cadatacatalog.state.gov/dataset/4a387c35-29cb-4902-b91d-3da0dc02e4b2/resource/299b3b67-3c09-46a3-9eb7-9d0086581bcb/download/countrytravelinfo.json"

    ### 2. 5000TravelQuestionsDataset (Hugging Face)
    url_5k = "https://huggingface.co/datasets/NLPC-UOM/Travel-Dataset-5000/resolve/main/5000TravelQuestionsDataset.xlsx"
    
    json_data = extract_json_data(url_cti)
    df_questions, df_taxonomy = extract_csv_data(url_5k)
    
    # Clean json data
    clean_json = html_cleaning(json_data)