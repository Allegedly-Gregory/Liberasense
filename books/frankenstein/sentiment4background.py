import os
import glob
from nltk.corpus import PlaintextCorpusReader
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sent_tokenize
import nltk
import json
import re
# nlt=.download("vader_lexicon")


analyzer = SentimentIntensityAnalyzer()
cwd = os.getcwd()

# par_dict = {}
results = []
# i = 0
# j = 1
paragraph_list = []
sentence_list = []
htnml = []
for filename in sorted(
        glob.glob(os.path.join("./", "*.txt"))
):
    # if str(filename[5:-7]) == str(filename[5:-7]):
        with open(filename) as f, open(filename+".html", "w") as html:
            paragraphs = f.read().split("\n\n")
            sentences = re.split(r' *[\.\?!][\'"\)\]]* *', str(paragraphs))
            vsp = analyzer.polarity_scores(str(paragraphs))
            vsnt = analyzer.polarity_scores(str(sentences))
            for paragraph in paragraphs:
                paragraph_list.append(paragraph)
                paragraph_list.append(vsp)
                # print("PARAGRAPH SCORING\n{}\n{}\n{}\n\n".format(filename, vsp, paragraph))
            for sentence in sentences:
                sentence_list.append(sentence)
                sentence_list.append(vsnt)
                # htmlspan =  """<span class={}>{}</span>""".format(sentence)
                # print("SENTENCE SCORING\n{}\n{}\n{}\n\n".format(filename, vsnt, sentence))
print(paragraph_list)
# print(paragraph_list[2])
# # print("")
# # print("")
# # print(sentence_list[2])
# # for x in paragraph_list, sentence_list:
# #     print(x)
#             # print(vsnt)
# #             print("<p class={}".format())
# #             sentences = f.read().split(".")
# #             strpar = str(paragraph)
# #             for sentence in paragraph:
# #                 ## chapter_text.append(str(filename + "-" + line + str(vs)))
# #                 sentence = sent_tokenize(sentence)
# #                 vs = analyzer.polarity_scores(str(sentence))
# #                 vs["paragraph"] = paragraph
def colorscheme(score):

    if score <= -0.9:
        sc01 = "#e44138"
        return "sc01"
    elif score <= -0.6:
        sco2 = "#da6258"
        return "sc02"
    elif score <= -0.3:
        sco3 = "#cb928f"
        return "sc03"
    elif score <= -0.01:
        sco4 = "#c2b4b4"
        return "sc04"
    elif score <= 0.01:
        sc05 = "#b3babd"
        return "sc05"
    elif score <= 0.3:
        sco6 = "#8fa8b8"
        return "sc06"
    elif score <= 0.6:
        sc07 = "#568db0"
        return "sc07"
    elif score <= 0.9:
        sc08 = "#316bab"
        return "sc08"


print(colorscheme(


frank_html = open("sentiment_frankenstein.html", "w")
paragraph_txt = """<html><p class={} style="background-color:{}""</p></html>""".format(sentence, style)
frank_html.write(paragraph_txt)








#                 results.append(vs)
#                 par_dict[i] = {
#                     "paragraph_num": filename,
#                     "line_num": i,
#                     "line_text": sentence,
#                     "score": vs["compound"],
#                     "style": style,
#                 }
#                 i += 1
# # print(paragraph)
#                 # print(par_dict)
frank_html.close()
