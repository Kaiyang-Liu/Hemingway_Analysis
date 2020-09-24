from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
d = path.dirname(__file__)
text = open(path.join(d, 'Hemingway on Writing.txt'), encoding='UTF-8').read()
Hemingway = np.array(Image.open(path.join(d, "Hemingway.jpg")))
stopwords = set(STOPWORDS)
stopwords.add("Author")
wc = WordCloud(background_color="white", max_words=2000, mask=Hemingway,
               stopwords=stopwords, max_font_size=30, random_state=42)
wc.generate(text)
image_colors = ImageColorGenerator(Hemingway)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(Hemingway, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()