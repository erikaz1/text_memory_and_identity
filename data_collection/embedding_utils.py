import json
from tqdm import tqdm
import openai
from concurrent.futures import ThreadPoolExecutor, as_completed # Parallelize


## Functions for embedding ##
"""
These are ready to be used (functionable when called in-notebook), but I 
couldn't get it to work by importing embedding_utils.py. There are some 
weird error messages that arise when called upon this way.
"""


def get_embedding(text, model="text-embedding-3-small"):
    # Maximum number of tokens allowed by the GPT model
    max_tokens = 8192
    
    # If the text is shorter than the maximum tokens, use it directly
    if len(text.split()) <= max_tokens:
        return client.embeddings.create(input = [text], model=model).data[0].embedding
    
    # Calculate the start and end indices for the middle chunk
    start_index = (len(text.split()) - max_tokens) // 2
    end_index = start_index + max_tokens
    
    # Extract the middle chunk of text
    middle_chunk = ' '.join(text.split()[start_index:end_index])
    
    # Generate the embedding for the middle chunk
    return client.embeddings.create(input=[middle_chunk], model=model).data[0].embedding


# https://platform.openai.com/docs/guides/embeddings/use-cases

# Function to be executed in parallel
def get_embedding_for_text(row, col_to_embed, index_name):
    text_index = row[index_name]
    text = row[col_to_embed]
    embedding = get_embedding(text)  # Make the API call to get the embedding
    return text_index, embedding


def create_text_embedding_json_parallel(df, col_to_embed, index_name, output_file_name="text_embeddings_parallel.json", workers=8):
    with open(output_file_name, 'w') as outfile, ThreadPoolExecutor(max_workers=workers) as executor:
        # Use a dictionary to keep track of futures, with the song title as the key
        future_to_text = {executor.submit(get_embedding_for_text, row, col_to_embed, index_name): row[col_to_embed] for _, row in df.iterrows()}
        
        # Process completed futures as they complete
        for future in tqdm(as_completed(future_to_text), total=len(df), desc="Processing text"):
            text_title = future_to_text[future]
            try:
                # Get the result from the future
                text_index, embedding = future.result()
                # Create a JSON object for the current song and its embedding
                text_embedding_json = json.dumps({text_index: embedding})
                # Write the JSON object to the file on a new line
                outfile.write(text_embedding_json + '\n')
            except Exception as exc:
                print(f'{text_title} generated an exception: {exc}')

    print(f"Embeddings saved to {output_file_name}")