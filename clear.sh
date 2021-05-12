#!/bin/bash

i=1
while [ -d "run_$i" ]; do
  rm -rf "run_$i"
  i=`expr "$i" + 1`;
done

