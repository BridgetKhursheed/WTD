import json
import gzip
import urllib
import warc
from contextlib import closing
from urlparse import urljoin
from multiprocessing.pool import Pool
import multiprocessing
from collections import defaultdict
import urlparse
import os
import sys
import logging
import datetime
import matplotlib.pyplot as plt
import tldextract
import math
from collections import Counter
import pandas as pd
import seaborn as sns
import statistics
import numpy as np

def _main():
    
    trademarks_list = set()
    all_values = []
    max_numbers = []
    min_numbers = []
    median_numbers = []
    counter= 0
    #open provenance file
    with open("provenance.txt", 'r') as input_file:
        for item in input_file:
            item = item.strip()
            provenance_list.add(item)
    #open squatted
    with gzip.open("ip_counts_probe.gz", 'r') as input_file:
        for item in input_file:
            if "WARN" not in item:
                item = item.strip()
                item2 = item.split("\t")
                #print item2[1]
                if item2[1] in provenance_list:
                #               if (counter >2):
                #if int(item2[2])>1:
                    all_values.append(int(item2[2]))

#counter = counter +1
    
    print "No longer counting"
    
    #sns.set_context("paper")
    sns.set_style('darkgrid', {'axes.linewidth': 1, 'axes.edgecolor':'black'})
    plt.figure(figsize=(8, 6))
    plt.gca().set_color_cycle(['dodgerblue', 'darkorange', 'blue'])
    plt.plot(np.sort(all_values), np.linspace(0, 1, len(all_values), endpoint=False))
    plt.gca().set_xscale("log")
    plt.xlabel('Ips', size=15)
    plt.ylabel('CDF', size=15)
    plt.ylim(0.96, 1)
    #plt.legend(['Number of nameservers of PROBE domain names', 'Median of length ', 'Average of length'], loc='lower right')

    a = plt.axes([0.5,0.2,0.35,0.2])
    n, bins, patches = plt.hist(all_values,normed=True,facecolor='darkorange', alpha=0.75)
    plt.gca().set_yscale("log")
    plt.title('Ips Frequency')
    plt.xlabel('Ips')
    plt.tick_params(axis='x', colors='black')
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['right'].set_color('black')
    plt.gca().spines['bottom'].set_color('black')

    plt.savefig("ProbeLIst_cdf.pdf",bbox_inches='tight')
    plt.show()




if __name__ == '__main__':
    _main()
