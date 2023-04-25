from spacy_conll import init_parser
import spacy
from spacy import displacy
import spacy_udpipe

spacy_udpipe.download("en") # download English model
spacy_udpipe.download("es")

path_es = "data/es_ancora_extract_test.txt"
path_en = "data/gum_en_extract_test.txt"
output_path_en_ud = ("sortie/sorti_udpipe_en.html")
output_path_es_ud = ("sortie/sorti_udpipe_es.html")
output_path_en_st = ("sortie/sorti_stanza_en.html")
output_path_es_st = ("sortie/sorti_stanza_es.html")

nlp_en_st = init_parser("en",
                  "stanza",
                  parser_opts={"use_gpu": True, "verbose": False},
                  include_headers=True)
nlp_es_st = init_parser("es",
                  "stanza",
                  parser_opts={"use_gpu": True, "verbose": False},
                  include_headers=True)
nlp_en_ud = spacy_udpipe.load("en")
nlp_es_ud = spacy_udpipe.load("es")

# Parse a given string
def lect_pars(path,nlp_choisi):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        doc = nlp_choisi(text)
        sentence_spans = list(doc.sents)
        return sentence_spans
    
sentence_spans_en_st = lect_pars(path_en,nlp_en_st)
sentence_spans_es_st = lect_pars(path_es,nlp_es_st)
    
sentence_spans_en_ud = lect_pars(path_en,nlp_en_ud)
sentence_spans_es_ud = lect_pars(path_es,nlp_es_ud)

def graph(output,sentence_spans):
    html = displacy.render(sentence_spans, style='dep',page="true")
    with open(output, "w", encoding="utf-8") as fo:
        fo.write(html)

graph(output_path_en_st,sentence_spans_en_st)
graph(output_path_es_st,sentence_spans_es_st)
graph(output_path_en_ud,sentence_spans_en_ud)
graph(output_path_es_ud,sentence_spans_es_ud)