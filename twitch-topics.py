#!/usr/bin/env python2

import itertools
import time
import yaml


topics_file = "topics.yaml"
delay = 10


def read_topics():
    topics = []
    for key, value in yaml.load(open(topics_file))['topics'].iteritems():
        topics.append(value)

    return topics


def main():
    topics = read_topics()
    iterator = itertools.cycle(topics)
    for i in range(len(topics)):
        topic = next(iterator)
        print topic["short"] + " " + topic["full"]
        time.sleep(delay)

main()
