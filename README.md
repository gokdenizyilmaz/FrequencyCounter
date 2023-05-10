# FrequencyCounter
This code count the frequiencies of the words. But here is the difference, this code counts the roots of the words. Let me give you an example:
lets say our text is , text= "I swam in the lake last week with John at the London." , 
output will be "{'i': 1, 'in': 1, 'the': 2, 'lake': 1, 'last': 1, 'week': 1, 'with': 1, 'at': 1, 'london': 1, 'swam': 1}"
What happened in here ?
This code seperates the text three parts;
first one is normal words,nouns, but it doesnt count the private names like John,Emma etc only if it is a city name then it counts.
second one is verbs but this part doesnt count the irregular verbs like "went,swam" etc.. It only counts the regular verbs roots
and the last part is irregular verbs, this part detects the irregular verbs using a compare algorithm
