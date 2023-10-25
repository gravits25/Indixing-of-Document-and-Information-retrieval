from whoosh.fields import TEXT, KEYWORD, Schema
from whoosh.index import create_in, open_dir
from whoosh.writing import IndexWriter
from whoosh.qparser import QueryParser
from whoosh import index, qparser
from tabulate import tabulate
import os

# Define a schema
schema = Schema(title=TEXT(stored=True), content=TEXT)

index_dir = "my_index"

if not os.path.exists(index_dir):
    os.mkdir(index_dir)

ix = create_in(index_dir, schema)

ix = open_dir("my_index")

with ix.writer() as writer:
    for i in range(103):
        file_path = f'./Emails\\email_{i}.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        writer.add_document(title=f"email_{i}", content=file_content)

ix = open_dir("my_index")

# Create a QueryParser for the "content" field
parser = QueryParser("content", schema=ix.schema)


with ix.searcher() as searcher:
    query_parser = qparser.QueryParser("content", ix.schema)
    query = query_parser.parse("content:202111029 OR content:Gaurav")
    results = searcher.search(query)
    print("Query: " ,query)
    print("{:<30} {:<30} {:<30} {:<30}".format("Rank", "DocID", "Title", "Relevance Score"))

    for rank, result in enumerate(results):
    
        relevance_score = result.score
        title = result["title"]

        docID = result.docnum 
        rankk = rank+1
        
        print("{:<30} {:<30} {:<30} {:<30}".format(rankk, docID, title, f'{relevance_score:.4f}'))
 
    if(results):
        print()
    else:
        print("No related document found")
