from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def process_paragraph(paragraph):
    # sentces = paragraph.split(".")
    sentces = tokenize.sent_tokenize(paragraph)
    list_each_sentence = []
    lemmatizer = WordNetLemmatizer()

    for p in range(len(sentces)):
        list_each_sentence.append(word_tokenize(sentces[p]))

    for j in range(len(list_each_sentence)):
        for h in range(len(list_each_sentence[j])):
            list_each_sentence[j][h] = lemmatizer.lemmatize(list_each_sentence[j][h])

    result_senteces = []

    for j in range(len(list_each_sentence)):
        mkk = []
        for h in range(len(list_each_sentence[j])):
            if list_each_sentence[j][h].lower() not in stopwords.words("english"):
                mkk.append(list_each_sentence[j][h])
        result_senteces.append(mkk)

    return result_senteces


paragraph_input = "Here we will implement the Polynomial Regression using Python. We will understand it by comparing " \
            "Polynomial Regression model with the Simple Linear Regression model. So first, let's understand the " \
            "problem for which we are going to build the model. "

process_paragraph(paragraph_input)
result = process_paragraph(paragraph_input)

for i in range(len(result)):
    print(result[i])
