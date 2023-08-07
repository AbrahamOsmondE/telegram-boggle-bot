import boto3
import os
import sys

s3 = boto3.client('s3')
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

def generate_trie():
    response = s3.get_object(Bucket="bogglebot", Key="csw19.txt")['Body']
    WORD_KEY = '$'
    trie = {}
    for word in response.iter_lines():
        word = word.decode('UTF-8')
        word = word.replace('\n', '')
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word
    return trie

sys.modules[__name__] = generate_trie