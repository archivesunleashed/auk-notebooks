"""
This module is intended for use with Archives Unleashed Cloud
derivative data and the Archives Unleashed Cloud notebooks.
For more information, please visit https://archivesunleashed.org/.
"""

from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.draw.dispersion import dispersion_plot as dp
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords


class AuNotebook():
    """
    Auk notebook helper functions.
    """

    # Maximum number of words to show in output.
    # Jupyter will create an output error if the number is too high.
    top_count = 30

    # Domain suffixes to check non-U.S. domains so that (e.g.)
    # www.google.co.uk will become "google".
    stop_domains = ["co", "org", "net", "edu"]  # Domain suffixes to remove.

    # Minimum number of characters for a word to be included in a corpus.
    minimum_word_length = 3  # Eliminates "it", "I", "be" etc.

    # List of substrings to filter a text line, if desired.
    line_filter = ['404 Not Found']

    # How many lines of text to use.
    results_limit = 1000

    # If you want to start at a different line, you can increase this.
    # If results_start is great than results_limit you will get no results.
    results_start = 0

    # If you have a large file but want to sample the file more broadly.
    # You can increase this value skip to every Nth line.
    results_step = 1

    #  Change if you want a different filename.
    output_filename = "./filtered_text.txt"  # filename to output.

    # Characters to show per text file in output.
    # Larger numbers will result in more text showing in output.
    max_characters = 75

    # The years to include in the analysis.
    # If empty, you will get all available years.
    filtered_years = []  # E.g. ['2015', '2016', '2019'].

    # The domains to include in the analysis.
    # If empty, you will get all available domains.
    filtered_domains = []  # E.g ["google", "apple", "facebook"].

    # Use nltk stopwords?
    use_nltk = True

    # List of words not to include in a corpus for text analysis. Added to
    # nltk stop words if use_nltk is True.
    stop_words_user = ('north', 'south')

    # Will include nltk stop words if use_nltk is True, otherwise just user
    # selected stop words.
    stop_words = ""

    # Collection ID.
    collection = "4867"  # Default collection for auk-notebooks.
    auk_fp = './data/'
    auk_full_text = ""
    auk_gephi = ""
    auk_graphml = ""
    auk_domains = ""
    auk_filtered_text = ""

    def __init__(self, collection, folder, **kwargs):
        self.collection = collection
        if folder is not None:
            self.auk_fp = folder
        for key, value in kwargs.items():
            setattr(self, key.lower(), value)
        self.auk_full_text = self.auk_fp + self.collection + "-fulltext.txt"
        self.auk_gephi = self.auk_fp + self.collection + "-gephi.gexf"
        self.auk_graphml = self.auk_fp + self.collection + "-gephi.graphml"
        self.auk_domains = self.auk_fp + self.collection + "-fullurls.txt"
        self.auk_filtered_text = self.auk_fp \
            + self.collection + "-filtered_text.zip"
        self.stop_words = set(stopwords.words('english')).union(
            self.stop_words_user) if self.use_nltk else self.stop_words_user

    def clean_domain(self, s):
        """Extracts the name from the domain (e.g. 'www.google.com' becomes
        'google').

        :param: s: The domain name to clean.
        :return: The relevant name.
        """
        ret = ""
        dom = s.split(".")
        if len(dom) < 3:  # x.com is always x.
            ret = dom[0]
        elif dom[-2] in self.stop_words:  # www.x.co.uk should be x.
            ret = dom[-3]
        else:
            ret = dom[1]
        return ret

    def get_domains(self, split_method="full"):
        """Extracts the domains from a file by method.

        :param split_method: Either "full" "name" or "sub". "name" provides
            just the domain name, "sub" produces the name with subdomains.
            "full" provides the entire name.
        :return: A list of tuples containing (urlname, count).
        """
        ret = []
        clean = self.clean_domain
        scores = Counter()
        with open(self.auk_domains) as fin:
            for line in fin:
                ret.append(line.strip('()\n').split(","))
        if split_method == 'name':
            for url, count in ret:
                scores.update({clean(url): int(count)})
            ret = scores
        elif split_method == 'sub':
            splits = [(x[0].split('.'), int(x[1])) for x in ret]
            for url, count in splits:
                if len(url) < 3:
                    scores.update({'.'.join(['www', url[0]]): count})
                else:
                    scores.update({'.'.join([url[0], url[1]]): count})
            ret = scores
        else:
            for url, count in ret:
                scores.update({url: int(count)})
            ret = scores
        return ret

    def get_text(self, by="all"):
        """Get the text from the files (by domain or year if desired).

        :param by: "all", "domain" or "year" the output to return.
        :param minline: The minimum size of a line to be included.
        :return: [({year or domain}, textString)] if by is 'domain' or 'year',
            otherwise [textString].
        """
        text = []
        form = range(self.results_start, self.results_limit, self.results_step)
        with open(self.auk_full_text) as fin:
            for num in range(self.results_limit):
                if num in form:
                    line = next(fin)
                    split_line = str(line).split(",", 3)
                    line_filter = set(
                        [split_line[3].find(x) for x in self.line_filter])
                    if (len(split_line[3]) >= self.minimum_word_length and
                            line_filter == {-1}):
                        # Too short and filtered strings removed.
                        if by == "domain":
                            text.append((
                                self.clean_domain(split_line[1]),
                                split_line[3]))
                        elif by == "year":
                            text.append((split_line[0][1:5], split_line[3]))
                        else:
                            text.append(split_line[3])
                else:
                    next(fin)
        return text

    def get_text_tokens(self):
        """Get the data and tokenize the text.

        :param minlen: The minimum word size to be included in the
            list of words.
        :return: A list of words included in the text file.
        """
        return [x.lower() for x in word_tokenize(' '.join(self.get_text()))
                if len(x) > self.minimum_word_length]

    def get_tokens_domains(self):
        """Get tokens by domain.

        :param minlen: The minimum word size to be included in the
            list of words.
        :return: A list of tuples with (domain, Counter).
        """
        return [(x[0], Counter([y for y in word_tokenize(x[1])
                if len(y) > self.minimum_word_length]))
                for x in self.get_text("domain")]

    def get_tokens_years(self):
        """Get tokens by year.

        :para minlen: The minimum word size to be included in the
            list of words.
        :return: A list of tuples with (year, Counter).
        """
        return [(x[0], Counter([y for y in word_tokenize(x[1])
                if len(y) > self.minimum_word_length]))
                for x in self.get_text("year")]

    def year(self):
        """Used by get_top_tokens_by to get the tokens by year."""
        return self.get_tokens_years()

    def domain(self):
        """Used by get_top_tokens_by to get tokens by domain."""
        return self.get_tokens_domains()

    def get_top_tokens(self):
        """Return the top tokens for the text."""
        return [(key, value) for key, value in Counter(
                     self.get_text_tokens()).most_common(self.top_count)]

    def get_top_tokens_by(self, fun):
        """ Get the top tokens by a function.

        :para fun: A function that returns a list of (key,
            Counter([tokenized_list])).
        :para total: The number of top tokens to return for each key.
        :para minlen: The minimum word length.
        :return: List of minlen tokens by fun.
        """
        sep = dict()
        tokens = fun()
        sep = {k[0]: Counter() for k in tokens}
        for key, value in tokens:
            sep[key] += value
        ret = [(key, val.most_common(self.top_count))
               for key, val in sep.items()]
        return (ret)

    def international(self, text):
        """Applies UTF-16 if possible.

        :param text: The text to decode (assumes UTF-8).
        :return: UTF-32 or UTF-16 decoded string or else original string.
        """
        unicode = text.encode("utf-8")
        try:
            ret = unicode.decode("UTF-32-LE")
        except UnicodeDecodeError:
            try:
                ret = unicode.decode("UTF-32-BE")
            except UnicodeDecodeError:
                try:
                    ret = unicode.decode("UTF-16-LE")
                except UnicodeDecodeError:
                    try:
                        ret = unicode.decode("UTF-16-BE")
                    except UnicodeDecodeError:
                        ret = unicode.decode("UTF-8")
        return ret

    def write_output(self, stdout, results):
        """ Writes results to file.

        :param stdout: Filepath for file.
        :param results: A list of results.
        :return: None.
        """
        try:
            with open(filename, "w") as output:
                for value in results:
                    output_file_write(str(value))
        except:
            print("Error writing the file.")

    def sentiment_scores(self, by="domain"):
        """ Calculates sentiment scores for a body of text.

        :param by: Either "year" or "domain".
        :return: A list of tuples with (year/domain, ("neg", score),
            ("neu", score) etc.).
        """
        sep = dict()
        corpus = self.get_text(by)
        sep = {k[0]: [] for k in corpus}
        for key, value in corpus:
            sep[key] += sent_tokenize(value)
        sid = SentimentIntensityAnalyzer()
        result = []
        for a, b in sep.items():
            scores = Counter({"neg": 0, "pos": 0, "neu": 0, "compound": 0})
            for c in b:
                scores.update(sid.polarity_scores(c))
            result += [(a,
                       ("neg", scores['neg']/len(b)),
                       ("pos", scores['neg']/len(b)),
                       ("neu", scores['neu']/len(b)),
                       ("compound", scores['compound']/len(b)))]
        return(result)

if __name__ == "__main__":
    pass
