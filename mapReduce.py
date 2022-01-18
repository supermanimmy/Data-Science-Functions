"""
MapReduce application
@date 07/01/22
@author Imran and Joel Grus
"""


from typing import List, Tuple, Iterator, Iterable
from collections import  Counter, defaultdict

def tokenise(document: str) -> List[str]:
    """Split on whitespace"""
    return document.split()

"""
Return most frequent words in documnts
"""
def word_count_old(documents: List[str]):
    """Word count not using MapReduce"""
    return Counter(word 
        for document in documents
        for word in tokenise(document))


def wc_mapper(document: str) -> Iterator[Tuple[str, int]]:
    """For each word in the document, emit (word, 1"""
    for word in tokenise(document):
        yield (word, 1)

def wc_reducer(word: str, counts: Iterable[int])-> Iterator[Tuple[str, int]]:
    """Sum up the counts for a word"""
    yield (word, sum(counts))

"""Collect results from wc_mapper and feed them to wc_reducer"""

def word_count(documents: List[str]) -> List[Tuple[str, int]]:
    """Count the words in the input documents using MapReduce"""
    collector  = defaultdict(list) # to store groupled values

    for document in documents:
        for word,  count in wc_mapper(document):
            collector[word].append(count)
    
    return [output
            for word, counts in collector.items()
            for output in wc_reducer(word, counts)]

assert  word_count(["data science", "data", "big data"]) == [('data', 3), ('science', 1), ('big', 1)]

