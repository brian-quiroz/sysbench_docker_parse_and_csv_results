## Description
Run all sysbench benchmarks with their default parameters one or more times, both locally and in a docker container. Also outputs relevant results to terminal and as CSV files.


## Instructions
To run all benchmarks n times and (optionally) save summary of results as CSV(s):
```
./run_benchmarks.sh [number of runs (n)] [save as CSV] [average results]
```

Once you have run the above script once, you can view/save your results at any time using:
```
python parse_results.py [save as CSV] [average results]
```

Note that "save as CSV" and "average results" are flags (1 = activate, 0 = deactivate). If "save as CSV" is activated, the results will be saved as CSV file(s). Otherwise, the output will be printed to the command line. If "average results" is activated, the program will output the average and standard deviation of each value across all runs. Otherwise, the program will output the results of each run individually.
