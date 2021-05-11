## Description
Run all sysbench benchmarks with their default parameters one or more times, both locally and in a docker container. Also outputs relevant results to terminal and to CSV files.


## Instructions
To run all benchmarks n times and (optionally) save summary of results to CSV(s):
```
./run_benchmarks.sh [number of runs (n)] [save to csv (1) or don't save to csv(0)]
```
 
To view results summary in terminal (you must have run ./run_benchmarks.sh previously to create the results files used by this script):
```
python parse_results.py 0
```

To view results summary in terminal and save to CSV(s) (you must have run ./run_benchmarks.sh previously to create the results files used by this script):
```
python parse_results.py 1
```
