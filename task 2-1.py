def handle_query(query, index, all_chunks):
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = embedding_model.encode(query).reshape(1, -1)

    # Perform similarity search
    D, I = index.search(query_embedding, k=5)  # k is the number of nearest neighbors
    return [(I[0][i], D[0][i]) for i in range(len(I[0]))]

# Example Query
user_query = "What uw medicine are available?"
results = handle_query(user_query, index, chunks)

# Display results
for idx, distance in results:
    print(f"Result Chunk: {chunks[idx]}\nDistance: {distance}\n")