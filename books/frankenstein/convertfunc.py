from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import re

analyzer = SentimentIntensityAnalyzer()

def convertfunc(filename):
    outputfile = filename+".html"
    with open(filename)as f, open(outputfile, "w") as html:
        paragraphtext = f.read()
        print("<p class='{}'>".format(colorscheme(scoresent(paragraphtext))), file=html)
        sentences = listconvert(paragraphtext)
        for sentence in sentences:
            print(marksent(sentence),file=html)
        print("</p>", file=html)


def scoresent(string):
    vs = analyzer.polarity_scores(string)
    return vs["compound"]

def listconvert(string):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', str(string))
    return sentences

def marksent(sentence):
    return "<span class = '{}'>{}</span>".format(colorscheme(scoresent(sentence)), sentence)



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
