## Description
Run all sysbench benchmarks with their default parameters one or more times, both natively and in a docker container. Also outputs relevant results to terminal and as CSV files.


## Instructions
To run all benchmarks n times and (optionally) save summary of results as CSV(s):
```
./run_benchmarks.sh [number of runs (n)] [average results] [save as CSV]
```

Once you have run the above script once, you can view/save your results at any time using:
```
python parse_results.py [average results] [save as CSV]
```

Note that "average results"  and "save as CSV" are flags (1 = activate, 0 = deactivate). If "average results" is activated, the program will output the average and standard deviation of each value across all runs. Otherwise, the program will output the results of each run individually. If "save as CSV" is activated, the results will be saved as CSV file(s). Otherwise, the output will be printed to the command line.

If you run the shell script more than once, the files from the previous runs will be preserved. For example, if you use the shell script to run all benchmarks 10 times, and then use it again to run it 5 more times, all 15 results will be avaialable for the parser to display/save at any time.

If you want to remove all files from previous runs, run:

```
./clear.sh
```

This will remove all "run_n" folders and everything inside them, but will not remove any CSV files.
