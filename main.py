import data_clean
import generate_summary
import json
import os
import time 
#import pickle

from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    
    start_time = time.time()
    data = []
    test = open("documentJSON.txt", "a")
  
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", padding_side="left")
    tokenizer.pad_token = tokenizer.eos_token  # Most LLMs don't have a pad token by default
    model.to("cuda")

    conclusion_directory = "/users/PAS2570/jindal73/Downloads/NLP_Dataset-main/sumpubmed-master/text"
    summary_directory = "/users/PAS2570/jindal73/Downloads/NLP_Dataset-main/sumpubmed-master/abstract"

    files = os.listdir(conclusion_directory)

    # get conclusions from articles
    conclusion_text = []
    # get summaries for each article
    summary_text = []
    
    j = 300
    while j < 500:
       
       # program will stop executing after 55 min
       if time.time() - start_time >= 3300:
           break

       file_conclusion = open(conclusion_directory + "/" + files[j], 'r')
       conclusion_text.append(data_clean.remove_tags(data_clean.extract_conclusion(file_conclusion)))
       file_conclusion.close()

       split_name = files[j].split("_", 1)

       summary_location = summary_directory + "/abstract_" + split_name[1]
       file_summary = open(summary_location, 'r')
       text = data_clean.remove_tags(data_clean.extract_conclusion(file_summary))
       summary_text.append("Summarize the following so that it is comprehensible to the average high schooler: " + text)
       file_summary.close() 

       j += 1


    
    model_inputs = tokenizer(input, return_tensors="pt", padding=True).to("cuda")
    
    '''
    pklfile = open('tokenized.pkl', 'ab')
    pickle.dump(model_inputs, pklfile)                    
    pklfile.close()
    '''
    for SOMETHING THROUGH TOKENIZED INPUT:
        json_obj = {
            "Document": {
                "Summary": generate_summary.query(model_inputs(FIX THIS), model, tokenizer),
                "Conclusion": conclusion_text[i]
            }
        }
        json.dump(json_obj, test)
        data.append(json.dumps(json_obj))

    test.close()

    dataset = {
        "Data": data
    }

    with open('data.json', 'w') as f:
        json.dump(dataset,f) 

    f.close()

if __name__ == "__main__":
    main()    
