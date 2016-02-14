# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#Add-ons for later functions
def removePunctuation(word):
    """Input: string, Output: string without punctuation"""
    for i in list(word):
        if i == "'":
            word = word.replace(word[word.index(i):],"")
        elif i in string.punctuation:
            word = word.replace(i,'')
    return word

def remove_punctuation_list(List):
    for i in range(len(List)):
        List[i] = removePunctuation(List[i])
    return List

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

#Whole-word Triggers
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
    def is_word_in(self, text):
        text = text.lower()
        for punc in string.punctuation:
            text = text.replace(punc," ")
        self.text = text.split(" ")
        #self.text type list, is uncapitalized, separated in to words ignoring punctuation
        for eachWord in self.text:
            if eachWord == self.word:
                boolean = True
                return boolean
                break
            else:
                boolean = False
        return boolean

class TitleTrigger(WordTrigger):
    def __init__(self, word):
        self.titleTrigger = WordTrigger(word)
    def evaluate(self, story):
        return self.titleTrigger.is_word_in(story.get_title())

class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        self.subjectTrigger = WordTrigger(word)
    def evaluate(self, story):
        return self.subjectTrigger.is_word_in(story.get_subject())

class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        self.summaryTrigger = WordTrigger(word)
    def evaluate(self, story):
        return self.summaryTrigger.is_word_in(story.get_summary())

                   
# Composite Triggers
class NotTrigger(Trigger):
    def __init__(self, triggerFunction):
        self.triggerFunction = triggerFunction
    def evaluate(self, story):
        return not self.triggerFunction.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, triggerFunction1, triggerFunction2):
        self.triggerFunction1 = triggerFunction1
        self.triggerFunction2 = triggerFunction2
    def evaluate(self, story):
        return self.triggerFunction1.evaluate(story) and self.triggerFunction2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, triggerFunction1, triggerFunction2):
        self.triggerFunction1 = triggerFunction1
        self.triggerFunction2 = triggerFunction2
    def evaluate(self, story):
        return self.triggerFunction1.evaluate(story) or self.triggerFunction2.evaluate(story)

# Phrase Trigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        return self.phrase in story.get_subject() or self.phrase in story.get_title() or self.phrase in story.get_summary()

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    triggeredStories = []
    for story in list(stories):
        for trigger in list(triggerlist):
            if story not in triggeredStories:
                if trigger.evaluate(story):
                    triggeredStories.append(story)
    return triggeredStories

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    #Eliminates blank lines and comments  
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)
        
    triggerDict = {}
    triggerList = []
    configList = []
    for line in lines:
        configList.append(line.split(' '))
        """Creates list of key words for configuration within the list of lines"""
    for config in configList:
        if config[0] == 'ADD':
            for trigger in config[1:]:
                triggerList.append(triggerDict[trigger])
        else:
            if config[1] == 'TITLE':
                triggerDict[config[0]] = TitleTrigger(config[2])
            elif config[1] == 'SUMMARY':
                triggerDict[config[0]] = SummaryTrigger(config[2])
            elif config[1] == 'SUBJECT':
                triggerDict[config[0]] = SubjectTrigger(config[2])
            elif config[1] == 'PHRASE':
                for word in config[2:]:
                    phrase = ''
                    phrase += word + ' '
                    phrase.replace(phrase[-1],'')
                triggerDict[config[0]] = PhraseTrigger(phrase)
            elif config[1] == 'NOT':
                triggerDict[config[0]] = NotTrigger(triggerDict[config[2]])
            elif config[1] == 'AND':
                triggerDict[config[0]] = AndTrigger(triggerDict[config[2]],triggerDict[config[3]])
            elif config[1] == 'OR':
                triggerDict[config[0]] = OrTrigger(triggerDict[config[2]],triggerDict[config[3]])
    return triggerList


    
import thread

def main_thread(p):
    """Sample Trigger List
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    """
    
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often to poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()
