#!/usr/bin/env python
from itertools import islice
import optparse
import sys
from collections import defaultdict

optparser = optparse.OptionParser()
optparser.add_option("-d", "--data", dest="train", default="data/hansards", help="Data filename prefix (default=data)")
optparser.add_option("-e", "--english", dest="english", default="e", help="Suffix of English filename (default=e)")
optparser.add_option("-f", "--french", dest="french", default="f", help="Suffix of French filename (default=f)")
optparser.add_option("-t", "--threshold", dest="threshold", default=0.5, type="float", help="Threshold for aligning with Dice's coefficient (default=0.5)")
optparser.add_option("-n", "--num_sentences", dest="num_sents", default=100000000000, type="int", help="Number of sentences to use for training and alignment")
(opts, _) = optparser.parse_args()
f_data = "%s.%s" % (opts.train, opts.french)
e_data = "%s.%s" % (opts.train, opts.english)

sys.stderr.write("Training with IBM Model 1")

# Initialize translation probabilities uniformly
trans_prob = defaultdict(lambda: defaultdict(lambda: 1.0))

# Iteratively refine alignment probabilities using Expectation-Maximization
for iteration in range(5):  # Consider more iterations for better results
    count_fe = defaultdict(float)
    total_f = defaultdict(float)

    for (f, e) in islice(zip(open(f_data), open(e_data)), opts.num_sents):
        f_words = f.strip().split()
        e_words = e.strip().split() + ["NULL"]  # IBM Model 1 includes a NULL token

        # Compute normalization factor
        total_s = defaultdict(float)
        for f_word in f_words:
            total_s[f_word] = sum([trans_prob[f_word][e_word] for e_word in e_words])

        # Collect counts
        for f_word in f_words:
            for e_word in e_words:
                c = trans_prob[f_word][e_word] / total_s[f_word]
                count_fe[(f_word, e_word)] += c
                total_f[e_word] += c
    # Update probabilities
    for (f_word, e_word), count in count_fe.items():
        trans_prob[f_word][e_word] = count / total_f[e_word]

# Align based on the refined probabilities
for (f, e) in islice(zip(open(f_data), open(e_data)), opts.num_sents):
    f_words = f.strip().split()
    e_words = e.strip().split()

    for i, f_word in enumerate(f_words):
        max_prob = -1
        max_j = -1
        for j, e_word in enumerate(e_words):
            if trans_prob[f_word][e_word] > max_prob:
                max_prob = trans_prob[f_word][e_word]
                max_j = j

        sys.stdout.write(f"{i}-{max_j} ")

    sys.stdout.write("\n")