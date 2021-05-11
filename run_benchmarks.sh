#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Illegal number of parameters"
  exit 2
fi

n=1;
max=$1;

while [ "$n" -le "$max" ]; do
  mkdir "run_$n"
  echo "Run #$n"

  mkdir "run_$n"/host

  echo "Running cpu benchmark on host..."
  sysbench cpu run > "run_$n"/host/cpu.txt

  echo "Running memory benchmark on host..."
  sysbench memory run > "run_$n"/host/memory.txt

  echo "Running threads benchmark on host..."
  sysbench threads run > "run_$n"/host/threads.txt

  echo "Running mutex benchmark on host..."
  sysbench mutex run > "run_$n"/host/mutex.txt

  echo "Running fileio-seqwr on host..."
  sysbench fileio --file-test-mode=seqwr run > "run_$n"/host/seqwr.txt

  echo "Running fileio-seqrewr on host..."
  sysbench fileio --file-test-mode=seqrewr run > "run_$n"/host/seqrewr.txt

  echo "Running fileio-seqrd on host..."
  sysbench fileio --file-test-mode=seqrd run > "run_$n"/host/seqrd.txt

  echo "Running fileio-rndrd on host..."
  sysbench fileio --file-test-mode=rndrd run > "run_$n"/host/rndrd.txt

  echo "Running fileio-rndwr on host..."
  sysbench fileio --file-test-mode=rndwr run > "run_$n"/host/rndwr.txt

  echo "Running fileio-rndrw on host..."
  sysbench fileio --file-test-mode=rndrw run > "run_$n"/host/rndrw.txt

  rm -rf test_file*

  mkdir "run_$n"/docker

  echo "Running cpu benchmark on docker..."
  docker run giordan12/sysbench_cont:0.4 cpu run > "run_$n"/docker/cpu.txt

  echo "Running memory benchmark on docker..."
  docker run giordan12/sysbench_cont:0.4 memory run > "run_$n"/docker/memory.txt

  echo "Running threads benchmark on docker..."
  docker run giordan12/sysbench_cont:0.4 threads run > "run_$n"/docker/threads.txt

  echo "Running mutex benchmark on docker..."
  docker run giordan12/sysbench_cont:0.4 mutex run > "run_$n"/docker/mutex.txt

  echo "Running fileio-seqwr on docker..."
  docker run giordan12/sysbench_cont:0.4 fileio --file-test-mode=seqwr run > "run_$n"/docker/seqwr.txt

  echo "Running fileio-seqrewr on docker..."
  docker run giordan12/sysbench_cont:0.4 fileio --file-test-mode=seqrewr run > "run_$n"/docker/seqrewr.txt

  echo "Running fileio-seqrd on docker..."
  docker run giordan12/sysbench_cont:0.4 fileio --file-test-mode=seqrd run > "run_$n"/docker/seqrd.txt

  echo "Running fileio-rndrd on docker..."
  docker run giordan12/sysbench_cont:0.4 fileio --file-test-mode=rndrd run > "run_$n"/docker/rndrd.txt

  echo "Running fileio-rndwr on docker..."
  docker run giordan12/sysbench_cont:0.4 fileio --file-test-mode=rndwr run > "run_$n"/docker/rndwr.txt

  echo "Running fileio-rndrw on docker..."
  docker run giordan12/sysbench_cont:0.4 fileio --file-test-mode=rndrw run > "run_$n"/docker/rndrw.txt

  rm -rf test_file*

  n=`expr "$n" + 1`;
done

python parse_results.py $2
