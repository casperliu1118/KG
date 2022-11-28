import spacy
nlp = spacy.load('en_core_web_sm')


doc = nlp("The 22-year-old recently won ATP Challenger tournament.")
doc2 = nlp("今天天氣真好。")

for tok in doc2:
  print(tok.text, "...", tok.dep_)
  