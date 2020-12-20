import math
file = ['t1.txt', 't2.txt', 't3.txt']
d = 3
tf = dict()
idf = dict()
doc_freq = dict()
docx = dict()
def termFrequency(doc, t):
    res = float(0.0)
    for s in t:
        if s.lower() in doc:
            res = float(doc[s.lower()] / float(len(doc)))
            doc_freq[s.lower()] = doc_freq[s.lower()] + 1
            tf[s.lower()].append(res) 
        else:
            tf[s.lower()].append(0)  

c = int(input("Enter the number of terms to be searched: "))
term = list(input("Enter the terms to be searched: ").split()[:c])

for t in term:
    doc_freq[t.lower()] = 0
    idf[t.lower()] = 0
    tf[t.lower()] = []

for i in range(d):
    docx[i + 1] = 0

for f in file:
    counts = dict()
    handle = open(f)
    for line in handle:
        words = line.split()
        for w in words:
            counts[w.lower()] = counts.get(w.lower(), 0) + 1
    print(counts)
    print(len(counts))
    termFrequency(counts, term)

for i in term:
    a = float(d/(doc_freq[i] + 1))
    idf[i] = math.log(a)

print("Term Frequency:{}".format(tf))
print("IDF:{}".format(idf))

for j in range(d):
    for s in term:
        docx[j + 1] = docx[j + 1] + tf[s.lower()][j] * idf[s.lower()]

print("TF * IDF score: {}".format(docx))

doc_final = sorted(docx.items(), key = lambda x: (x[1], x[0]), reverse = True)
print("The search results in the order of relevance are as follows:")
print(doc_final)