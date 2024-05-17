import pandas as pd
import json
import base64
import requests
from openai import OpenAI
pkey = 'YOUR_API_KEY'
client = OpenAI(api_key=pkey)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def gpt4v_inference(text_prompt, image_path):
    
    # Getting the base64 string
    # Path to your image e.g. image_path = "./img/B00DJIWQVG.jpg"
    base64_image = encode_image(image_path)
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {pkey}"
    }

    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt_temp
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 100
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":

    fp_data = 'Food_annotated_final.tsv'
    fp_attr = 'options_Food.json'

    with open(fp_attr) as f:
        dic = json.load(f)
    print(dic.keys())

    df = pd.read_csv(fp_data, sep='\t', header=0)
    df['gpt4v_pred'] = 'todo'
    df.head()
    print(len(df))

    for ind, row in df.iterrows():
    
        if row['gpt4v_pred'] == 'todo':
            
            print(ind)
            image_names = row['images']
            image_path = f"./img/{image_names}"
            attribute = row['attribute_names']
            category = row['category']
            title = row['texts']
            Options = '[' + ', '.join(dic[attribute]) + ']'
            prompt_temp = f'''What is the {attribute} of this product?
        Context: [Category] {category} {title}.
        Choose the most appropriate one from the options: {Options}.
        '''
            print(prompt_temp)
            print(image_path)
            print('=*='*20)


            row['gpt4v_pred'] = gpt4v_inference(prompt_temp, image_path)


    # e.g. 'Clothing_annotated_final.tsv'
    fp_out = fp_data.replace('.tsv', '_gpt4.tsv')
    df.to_csv(fp_out, sep = '\t')
    print('Done...')
                