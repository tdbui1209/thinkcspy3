import string

paragraph = '''For instance, the government may want to analyze population
census figures to decide which regions require further spending and investment
on infrastructure and services. In this case, it will be important to have
access to reliable data to avoid erroneous fiscal decisions.
In the business world, incorrect data can be costly. Many companies use
customer information databases that record data like contact information,
addresses, and preferences. For instance, if the addresses are inconsistent,
the company will suffer the cost of resending mail or even losing customers.
'''

# Function to remove punctuation and return clean paragraph
def remove_punctuation(s):
    s_without_punct = ''
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

# Function to count if word contain letter 'e'.
def count_e_word(words):
    count = 0
    for word in words:
        for letter in word:
            # if letter contain letter 'e', count plus 1 and break loop.
            if letter == 'e':
                count += 1
                break
    return count

def process(s):
    s = remove_punctuation(s)
    words = s.split()
    count = count_e_word(words)
    layout = 'Your text contains {0} words, ' \
             'of which {1} ({2:.1f}%) contain an "e"'
    return layout.format(len(words), count, count/len(words)*100)

print(process(paragraph))
    
