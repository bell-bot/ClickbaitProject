from itertools import takewhile
from more_itertools import split_before
import re

class Query_Parser():

    def __init__(self, inverted_index, documents):
        self.inverted_index = inverted_index
        self.documents = documents

    # Boolean query implementation ------------------------------------------------------------------------------------

    def single_term_query(self, term):
        if term in self.inverted_index:
            return self.inverted_index[term]
        else:
            return []

    def and_query(self, term1, term2):
        docs1 = self.single_term_query(term1)
        docs2 = self.single_term_query(term2)
        
        common_docs = []
        for doc in docs1:
            if doc in docs2:
                common_docs.append(doc)
        
        return common_docs
    
    def or_query(self, term1, term2):
        docs1 = self.single_term_query(term1)
        docs2 = self.single_term_query(term2)
        
        common_docs = docs1 + docs2
        return set(common_docs)
    
    def not_query(self, term):
        docs = self.single_term_query(term)
        
        docs_without_term = []
        
        for doc in self.documents:
            if doc not in docs:
                docs_without_term.append(doc)
        
        return docs_without_term
    
    # Parsing utilities ------------------------------------------------------------------------------------

    def is_whitespace(self, c):
        whitespace = re.compile("[\s]+")
        return whitespace.match(c)
    
    def is_alphanum(self, c):
        alphanum = re.compile("[a-zA-Z0-9]+")
        return alphanum.match(c)
    
    def is_not(self,c):
        not_term = re.compile("not")
        return not_term.match(c.lower())
    
    # Parsing queries ------------------------------------------------------------------------------------

    def parse_query(self, query):
        # Get the first term in the query
        q1, q2 = list(split_before(query, self.is_whitespace))

        # Convert q1 to a string
        q1 = ''.join(q1)

        #
        print(q1, q2)

if __name__ == "__main__":
    inverted_index = {
        "dog": [1,2,3],
        "cat": [2,3,4],
        "hamster": [9,1,4]
    }
    documents = [1,2,3,4,9]
    qp = Query_Parser(inverted_index,documents)
    query = "Howdy cowboy"
    qp.parse_query(query)