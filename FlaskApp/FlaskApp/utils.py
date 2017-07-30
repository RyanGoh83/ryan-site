import random

quote_dict =[["a1", "q1"],
         ["a2", "q2"],
         ["a3", "q3"]
        ]

def quote_generator():
    qotd_pair = random.choice(quote_dict)
    quote = qotd_pair[1]
    who_said = qotd_pair[0]
    return quote, who_said
