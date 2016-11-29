---
title: Answering multiple choice questions
date: 2015-12-02
---

Back in middle school and high school, my teachers told me that if you run out of time on a test and need to guess the remaining answers, it is better to guess only one answer for each remaining question rather than a different answer for each remaining question. I wasn't sure that this was correct, so I wrote a simulation.

{% highlight python %}
from random import randint
from itertools import zip_longest



a = 4     # Number of answers per question
q = 25    # Number of questions
n = 10000 # Number of tests to simulate



def simulate_test():
    answers        = [randint(1, a) for i in range(q)]
    random_guesses = [randint(1, a) for i in range(q)]
    single_guess   = [randint(1, a)] * q

    random_correct       = sum([1 if guess == solution else 0 for guess, solution in zip_longest(answers, random_guesses)])
    single_guess_correct = sum([1 if guess == solution else 0 for guess, solution in zip_longest(answers, single_guess)])

    return (random_correct, single_guess_correct)



total_random_correct = 0
total_single_guess_correct = 0

for i in range(n):
    if i % 1000 == 0: print(i)

    random_correct, single_guess_correct = simulate_test()

    total_random_correct += random_correct
    total_single_guess_correct += single_guess_correct

total_random_score = total_random_correct / (q * n)
total_single_guess_score = total_single_guess_correct / (q * n)



print(total_random_score)
print(total_single_guess_score)
{% endhighlight %}

The results showed that it doesn't matter if you guess one answer or guess random answers. Interesting stuff!
