def generate_response(retrieved_chunks):
    # Here you would implement the call to an actual LLM API
    for chunk in retrieved_chunks:
        print("Generated response based on chunk: ", chunk)

# Example of generating a response from the retrieved chunks
most_relevant_chunks = [chunks[i] for i, _ in results]
generate_response(most_relevant_chunks)