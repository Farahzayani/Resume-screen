import pandas as pd 
import os 
import fitz 


root_path = r'C:\Users\ASUS\Desktop\resume screening\Data\original_data'
categories = [name for name in os.listdir(root_path) ]
all_ids = []
all_cats = []

T=[]
for i in range(len(categories)):
    root = fr'C:\Users\ASUS\Desktop\resume screening\Data\original_data\{categories[i]}' 
    pdfs=[name for name in os.listdir(root) ] 
     
    for j in range(len(pdfs)):
        path=os.path.join(fr'C:\Users\ASUS\Desktop\resume screening\Data\original_data\{categories[i]}',pdfs[j])
        doc=fitz.open(path)
        text = "" 
        for page in doc: 
            text += page.get_text()
        T.append(text) 
    
    IDS=[name.replace('.pdf', '') for name in os.listdir(root) ]  
    cat=[categories[i] for j in range(len(IDS))] 
    all_ids.extend(IDS)            
    all_cats.extend(cat )
    #text.extend(T)    

df = pd.DataFrame({
    "IDS": all_ids,
    "Category": all_cats,
    'text':T
})
#32df['text']=T
#print(df)

pdfs=[name for name in os.listdir(root) ] 

#print(df)
print(df['text'][0])
