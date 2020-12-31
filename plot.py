import numpy as np
import pylab as plt
import seaborn as sns
import regex as re


def get_scores(fname):
    f = open(fname, 'r')
    scores = []
    while True:
        line = f.readline()
        if not line:
            break
        scores.append(int(re.match('\d+',line)[0]))
    f.close()
    return scores


def plot_game_data(ax,fname,label):
    scores = get_scores(fname)
    ax.hist(scores,label=label)
    return


def plot_multiple_game_data(ax, labels):
    score_sets = []
    for lab in labels:
        fname = lab+'_game_data.txt'
        scores = get_scores(fname)
        score_sets.append(scores)
    ax.hist(score_sets,label=labels)
    return


if __name__=='__main__':
    labels = ['random','always_down','max_add_score']

    fig, ax = plt.subplots()
    plot_multiple_game_data(ax,labels)
    plt.ylabel('final score')
    plt.legend()
    plt.show()
