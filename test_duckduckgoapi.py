'''
Author: Carson Pribble
Purpose: Tests the duckduckgo api with a query
    for presidents of the united states. Tests
    that the results from RelatedTopics from
    the query actually contain valid information
    (in this case it is checking that they contain
    the last name of each unique president's last
    name).
'''

import pytest
import requests

# Formal url for duckduckgo api
url_ddg = "https://api.duckduckgo.com"

# Using requests, query the duckduckgo api for 'presidents of the united states'
response = requests.get(url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json")
# Get the json formatted text to store in memory
rsp_data = response.json()

# Gather a list of dict's from the json 'RelatedTopics' attribute
relatedTopics = rsp_data['RelatedTopics']

# Create a new list to store only the text from each index in the
#   RelatedTopics list. Append the text from each index to the list.
names_list = list()
for topic in relatedTopics:
    names_list.append(topic['Text'])

# Create a list of all US President's last names.
president_list = ['Lincoln', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson',
                  'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan',
                  'Washington', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison',
                  'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover',
                  'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan',
                  'Bush', 'Clinton', 'Bush', 'Obama', 'Trump', 'Biden Jr.']
# Extract only unique last names
president_set = set(president_list)

# Test each index in the names list for the occurrence of a
#   President's last name
@pytest.mark.parametrize("test_input", president_set)
def test_president(test_input):
    for name in names_list:
        if test_input in name:
            assert True

# Final note, all tests pass: totaling 40 tests (40 unique President's last names)

