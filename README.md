## Description
Run all sysbench benchmarks with their default parameters one or more times, both locally and in a docker container. Also outputs relevant results to terminal and to CSV files.


## Instructions
To run all benchmarks n times and (optionally) save summary of results to CSV(s):
```
./run_benchmarks.sh [number of runs (n)] [save to CSV (1 = True, 0 = False)] [average results (1 = True, 0 = False)]
```

To view results summary of each run in terminal:
```
python parse_results.py 0 0
```

To save results summary of each run to CSV(s):
```
python parse_results.py 1 0
```

To view average and standard deviation of results summary in terminal:
```
python parse_results.py 0 1
```

To save average and standard deviation of results summary to (separate) CSVs:
```
python parse_results.py 0 1
```
