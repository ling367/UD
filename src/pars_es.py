import re
import stanza



def extract_corpus (path:str)-> list:
    data = open(path,mode="r",encoding='utf-8')
    annotations = data.read()
# type(annotations) = str
    phrases = re.findall(r'# text = (.+?\n)',annotations)
#select = np.random.choice(phrases, 100, False)
    phrases = sorted(phrases,key=len)
    phrases = [i for i in phrases if len(i) > 20]
    # print (len(phrases))
    selection = phrases[::16]
    selection_100 = selection[6:]
    return selection_100

# # for i in selection_100:
# #     print(len(i))
    # list_len = []
    # for i in phrases:
    #     list_len.append(len(i))
    # print(list_len)
# print(len(selection))
# #méthode 1
path = 'data/es_ancora-ud-test.conllu'
selection_100 = extract_corpus (path)
print (selection_100)
doc = open('data/es_ancora_extract_test.txt','w')
for phrase in selection_100:
    doc.write(phrase)
doc = open('data/es_ancora_extract.txt')
doc = doc.read()
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma,depparse')

doc = nlp(doc)
pars_phrases = [f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words] 

# print (pars_phrases[1])
depl_pars = open('sortie/es_ancora_pars_test.conllu','w',encoding='utf-8')
start = 'id: 1	word:'
i = 0
for phrase in pars_phrases:
    if start in phrase:
        i += 1
        depl_pars.write('\n'+'id_sent'+str(i)+'\n'+phrase+'\n')
    else:
        depl_pars.write(phrase+'\n')
depl_pars.close()
# # #méthode 2 
# # deppars_in = [stanza.Document([],text = doc)for doc in selection_100]
# # deppars = nlp(deppars_in)
# # print(deppars)
