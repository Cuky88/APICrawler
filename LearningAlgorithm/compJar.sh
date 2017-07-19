#!/usr/bin/env bash

for file in results/kmeansresults/*
do
    java -jar Comparator.jar file 'results/manualClusters.json'
done