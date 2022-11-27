emb = fastTextWordEmbedding
words =  ["menstruation","athletics","skin","contact","measurements","respiratory", "countdown","sleep","mode","snooze","stopwatch","compass","playlist","music","weight","audio","library","stocks","iPhone","pace","GPS","BPM","indoor","disease","Bluetooth","Wifi","Alarm","treatment","workout","entertain","fat","gym","sport","sports","games","nervous","relaxation","detection","checkups","checkup","disability","track","medications","power","swimming","fitbit","breathe","ovulation", "diagnosis", "clinical", "record", "blood", "vessels", "wrist", "pressure", "ehealth", "athletes","activity", "therapy", "calories", "steps", "patient", "exercise", "jog", "pump", "privacy", "data", "allergy","pulse",  "Apple",    "screen",    "watch",    "sensor",    "product",    "battery",    "band",    "phone",    "charge",    "display","heart","life", "worth", "cardiology", "oxygen", "cardio", "healthcare",   "rate",    "very",    "series",    "use",    "more",    "easy",    "upgrade",    "really",    "first",    "time",    "recommend",    "wife",    "gift", "buy",    "color",    "looks",    "size",    "track",    "bigger",    "larger",    "mobility",    "emergency",  "monitoring","happy", "great", "good", "best", "new", "love", "better", "nice"]
V = word2vec(emb,words);
size(V)
XY = tsne(V);
figure 
textscatter(XY,words)
title("Word Embedding t-SNE Plot")