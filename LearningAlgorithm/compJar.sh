#!/usr/bin/env bash

FILES=results/kmeansresults/*
#printf '%s\n' "${PWD##*/}"

for f in $FILES
do
    bash -c "java -jar Comparator.jar '$f' 'results/manualClusters.json'"
done