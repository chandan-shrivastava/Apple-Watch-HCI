import os
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import csv

def merge_files(path, out_file):
    with open(out_file, "w") as outfile:
        for file in os.listdir(path):
            if file.endswith(".txt"):
                with open(os.path.join(path, file), "r") as infile:
                    outfile.write(infile.read())

merge_files(".","merge.txt")

# wordcloud from csv file with word and frequency

df = pd.read_csv("merge.csv")
df = df[~df["word"].isin(stopwords.words("english"))]

wordcloud = WordCloud(
    width=2500, height=2500, background_color="white", min_font_size=5
).generate_from_frequencies(df.set_index("word").to_dict()["frequency"])
plt.figure(figsize=(200, 200), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

from collections import Counter

if len(sys.argv) != 3:
    print("Usage: python word_count.py path out_file")
    sys.exit(1)

path = sys.argv[1]
out_file = sys.argv[2]

words = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        with open(os.path.join(path, file), "r") as infile:
            words.extend(infile.read().split())

counter = Counter(words)
with open(out_file, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["word", "count"])
    writer.writerows(counter.most_common())

# python3 word_count.py . word_count.csv