#!/usr/bin/env python
# coding: utf-8

# In[10]:


import stanza
from stanza.utils.conll import CoNLL


# In[2]:


#stanza.download('en') # download English model
nlp_en = stanza.Pipeline('en', processors='tokenize,pos') # initialize English neural pipeline


# In[3]:


#stanza.download('es')
nlp_es = stanza.Pipeline('es')


# In[4]:


file_path = "gum_en_extract_test.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text_en = f.read()


# In[6]:


doc_en = nlp_en(text_en)


# In[14]:


file_path = "es_ancora_extract_test.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text_es = f.read()


# In[15]:


doc_es = nlp_es(text_es)


# In[16]:


CoNLL.write_doc2conll(doc_es, "es_ancora_extract_test_stanza.conllu")


# In[13]:


CoNLL.write_doc2conll(doc_en, "gum_en_extract_test_stanza.conllu")


# In[ ]:




