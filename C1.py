from whoosh import scoring

# Create a searcher with TF-IDF weighting
searcher = ix.searcher(weighting=scoring.TF_IDF())

# Define a query using a query parser
query_parser = QueryParser("content", schema=schema)
query = query_parser.parse("your_query_here")

# Search for documents and get the results sorted by relevance
results = searcher.search(query)

# Print the results and their relevance scores
for result in results:
    print(f"Document ID: {result['id']} - Relevance Score: {result.score:.4f}")

# Close the searcher when done
searcher.close()
