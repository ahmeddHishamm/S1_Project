# Importing string library to get list of punctuation
from string import punctuation
# Importing NLTK library for stemming and obtaining stop words
from nltk import PorterStemmer
from nltk.corpus import stopwords

ps = PorterStemmer()
# Downloading NLTK for first time use
# nltk.download("stopwords")
stopwords = stopwords.words("english")
stopwords.remove("where")


# Creating a class for text processing which will inculde all of its methods
class text_processing:
    def __init__(self, text):
        self._text = text

    # Making all text lowercase
    @property
    def normalize(self):
        self._text = self._text.lower()

    # Remove punctuation
    @property
    def remove_punctuation(self):
        filtered = []
        for letter in self._text:
            if letter not in punctuation:
                filtered.append(letter)
        self._text = "".join(filtered)

    # Tokenizing (splitting into a list)
    @property
    def tokenize(self):
        self._text = self._text.split()

    # Checking if user input has a proper name and changes it to
    # upper case so that it is not stemmed and removed as a stopping word
    @property
    def exceptions(self):
        proper_names = ["lido", "pickup", "elements", "tbs"]
        filtered = []
        for word in self._text:
            if word in proper_names:
                filtered.append(word.upper())
            else:
                filtered.append(word)
        # return filtered
        self._text = filtered

    # Stemming to remove unwanted suffix or prefix
    @property
    def text_stem(self):
        stemmed = []
        for word in self._text:
            if word == word.lower():
                stemmed.append(ps.stem(word))
            else:
                stemmed.append(word)
        # return stemmed
        self._text = stemmed

    # Removing stop words to take only key words from user input
    @property
    def remove_stop_words(self):
        filtered_text = []
        for word in self._text:
            if word == word.lower():
                if word not in stopwords:
                    filtered_text.append(word)
            else:
                filtered_text.append(word)
        self._text = filtered_text

    # Main function to call of the other functions
    @property
    def clean_text(self):
        self.normalize
        self.remove_punctuation
        self.tokenize
        self.exceptions
        self.text_stem
        self.remove_stop_words

    @property
    def get_text(self):
        return self._text


# ===================== driver code =================
# while True:
#     text1 = text_processing(input(">"))
#     text1.clean_text
#     print(text1.get_text)
