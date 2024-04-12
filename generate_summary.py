from transformers import AutoTokenizer, AutoModelForCausalLM
import data_clean

def query(model_inputs, model, tokenizer):
    generated_ids = model.generate(**model_inputs, do_sample=True, max_length = 8000)
    summaries = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    result = []
    for j in range(1):
        result.append(data_clean.clean_result(data_clean.remove_tags(summaries[j]),input[j]))
    
    return result
    