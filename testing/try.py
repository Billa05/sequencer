from bgp import Sequencer
from bgp.modules.terms import NGramProcessor, WordFreqModule
import json

s = Sequencer({
    '2gram': NGramProcessor(modules={
        '2grams': WordFreqModule()
    }, n=2, threshold=2, stop_words=None)})
genome = s.sequence('isbn_1842738577')

with open("testing/output.json","w") as f:
    f.write(json.dumps(genome.results))
