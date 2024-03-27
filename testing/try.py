from bgp import Sequencer
from bgp.modules.terms import NGramProcessor, WordFreqModule
from internetarchive import get_item
import json

# # Initialize the sequencer
# s = Sequencer({
#     '2gram': NGramProcessor(modules={
#         '2grams': WordFreqModule()
#     }, n=2, threshold=2, stop_words=None)})

# # Sequence the book
# genome = s.sequence('isbn_1842738577')

# # Write the results to a JSON file
# with open("testing/output.json","w") as f:
#     f.write(json.dumps(genome.results))

# Get the book item from the Internet Archive
item = get_item('isbn_1842738577')
print(item.metadata)
# Download the plaintext of the book
# plaintext = item.plaintext

# # Write the plaintext to a file
# with open("testing/fulltext.txt", "w") as f:
#     f.write(plaintext)