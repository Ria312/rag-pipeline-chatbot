import urllib.request, json 
import requests
import io
import pandas as pd    

### 1. Country Travel Information dataset (HTML)
url_cti = "https://cadatacatalog.state.gov/dataset/4a387c35-29cb-4902-b91d-3da0dc02e4b2/resource/299b3b67-3c09-46a3-9eb7-9d0086581bcb/download/countrytravelinfo.json"

# with urllib.request.urlopen(url_cti) as url:
#     data = json.load(url)[0]# dict type
    # print(data)

### 2. 5000TravelQuestionsDataset (Hugging Face)
url_5k = "https://huggingface.co/datasets/NLPC-UOM/Travel-Dataset-5000/resolve/main/5000TravelQuestionsDataset.xlsx"

s=requests.get(url_5k).content
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
print(df_taxonomy.head())
