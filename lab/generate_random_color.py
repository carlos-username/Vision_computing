#!/usr/bin/python2
#from grayscale import *
import matplotlib.pyplot as plt

import random
from sys import argv
def random_color(pastel_factor = 0.5):
    values=[]
    for x in [random.uniform(0,1.0) for n in xrange(3)]:
        values.append((x+pastel_factor)/(1.0+pastel_factor))
    return values # get three values within range of 1 because there are three channels

def color_distance_value(c1,c2):
    return sum([abs(x[0]-x[1]) for x in zip(c1,c2)]) # substracting color value to get distance 

def generate_new_color(existing_colors,pastel_factor = 0.5):
    max_distance = 0
    best_color = 0
    for i in xrange(150):
        color = random_color(pastel_factor = pastel_factor)
        #print "color: ",color
        if not existing_colors:
            return color
        best_dis = min([color_distance_value(color,c) for c in existing_colors])
        if not max_distance or best_dis > max_distance:
            max_distance = best_dis
            best_color = color
    return best_color

if __name__ == '__main__': #based on https://gist.github.com/adewes/5884820
    colors_list = []
    number=int(argv[1])
    for i in xrange(number):
        colors_list.append(generate_new_color(colors_list,pastel_factor = 0.5))
    
    print "Your colors:",colors_list
    N = len(colors_list)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    plt.axis('scaled')
    ax.set_xlim([ 0, N])
    ax.set_ylim([-0.5, 0.5])
    #cmap = colors
    for i in range(N): #Draw colors
        col = colors_list[i]
        rect = plt.Rectangle((i, -0.5), 1, 1, facecolor=col)
        ax.add_artist(rect)
    ax.set_yticks([])
    plt.show()
