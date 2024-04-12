import re 

#this function extracts the conclusion section from a given article
def extract_conclusion(file_conclusion):
    lines = file_conclusion.readlines()
    for j in range(len(lines)):
        if lines[j] == "CONCLUSIONS\n":
            return lines[j+1]

# this function removes <dig> tags from text
def remove_tags(text):
    return re.sub(r'<.*?>', "", text)

# this function takes result from AI model and cleans it 
def clean_result(text, input):
    text = re.sub(r'\\\\n', "", text)
    return text.replace(input, "")