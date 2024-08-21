import json

def load_chunks(file_path):
    """
    Load chunks from a JSON file.
    
    Args:
    - file_path (str): Path to the JSON file containing chunks.
    
    Returns:
    - List of chunks (dicts) from the JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def evaluate_relevancy(chunks, queries):
    """
    Evaluate the relevancy of chunks based on sample queries.
    
    Args:
    - chunks (list of dicts): List of chunks where each chunk contains 'text'.
    - queries (list of str): Sample queries to test relevancy.
    
    Returns:
    - List of dicts with queries and corresponding relevant chunks.
    """
    relevancy_results = []
    for query in queries:
        relevant_chunks = [chunk for chunk in chunks if query.lower() in chunk['text'].lower()]
        relevancy_results.append({
            "query": query,
            "relevant_chunks": relevant_chunks
        })
    return relevancy_results

def evaluate_correctness(chunks, original_transcript):
    """
    Evaluate the correctness of chunks by comparing with the original transcript.
    
    Args:
    - chunks (list of dicts): List of chunks where each chunk contains 'text'.
    - original_transcript (str): Full transcript text to compare chunks with.
    
    Returns:
    - List of dicts with chunk IDs and correctness status.
    """
    correctness_results = []
    for chunk in chunks:
        if chunk['text'] in original_transcript:
            correctness_results.append({"chunk_id": chunk['chunk_id'], "status": "correct"})
        else:
            correctness_results.append({"chunk_id": chunk['chunk_id'], "status": "incorrect"})
    return correctness_results

def evaluate_token_efficiency(chunks):
    """
    Evaluate the efficiency of chunk sizes in terms of token count.
    
    Args:
    - chunks (list of dicts): List of chunks where each chunk contains 'text'.
    
    Returns:
    - Dictionary with average chunk length and total chunk count.
    """
    lengths = [len(chunk['text'].split()) for chunk in chunks]
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    return {"average_length": avg_length, "chunk_count": len(chunks)}

def evaluate_cost(chunks, cost_per_token):
    """
    Estimate the cost based on the total token count.
    
    Args:
    - chunks (list of dicts): List of chunks where each chunk contains 'text'.
    - cost_per_token (float): Cost per token.
    
    Returns:
    - Dictionary with total tokens and estimated cost.
    """
    total_tokens = sum(len(chunk['text'].split()) for chunk in chunks)
    estimated_cost = total_tokens * cost_per_token
    return {"total_tokens": total_tokens, "estimated_cost": estimated_cost}

# Example usage
chunks = load_chunks('chunks.json')
queries = ["How can I group DataFrames in Pandas?"]
original_transcript = "Full transcript text here"
cost_per_token = 0.01  # Example cost per token

print(evaluate_relevancy(chunks, queries))
print(evaluate_correctness(chunks, original_transcript))
print(evaluate_token_efficiency(chunks))
print(evaluate_cost(chunks, cost_per_token))
