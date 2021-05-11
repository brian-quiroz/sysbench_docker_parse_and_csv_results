import os.path
from os import path
import numpy as np
import pandas as pd
import sys

def get_speed(lines):
    ret_str = '-1'
    for line in lines:
        if line.strip().startswith("events per second:"):
            ret_str = line.split(':',1)[1].strip()
    return ret_str

def get_latency(lines):
    ret_str = '-1'
    for line in lines:
        if line.strip().startswith("avg:"):
            ret_str = line.split(':',1)[1].strip()
    return ret_str

def get_mib(lines):
    ret_str = '-1'
    for line in lines:
        if line.strip().endswith("MiB/sec)"):
            ret_str = line.split(' ',1)[0].strip()
    return ret_str

def get_num_events(lines):
    ret_str = '-1'
    for line in lines:
        if line.strip().startswith("total number of events:"):
            ret_str = line.split(':',1)[1].strip()
    return ret_str

def get_write_throughput(lines):
    ret_str = '-1'
    for line in lines:
        if line.strip().startswith("written, MiB/s:"):
            ret_str = line.split(':',1)[1].strip()
    return ret_str

def get_read_throughput(lines):
    ret_str = '-1'
    for line in lines:
        if line.strip().startswith("read, MiB/s:"):
            ret_str = line.split(':',1)[1].strip()
    return ret_str

def get_specific_value(folder, benchmark, parameter):
    file_path = folder + benchmark + '.txt'
    with open(file_path,'r') as reader:
        ret_str = ''
        lines = reader.readlines()

        if (benchmark == 'cpu'):
            if (parameter == 'speed'):
                ret_str = get_speed(lines)
            elif (parameter == 'latency'):
                ret_str = get_latency(lines)
            else:
                ret_str = ''

        elif (benchmark == 'memory'):
            if (parameter == 'mib'):
                ret_str = get_mib(lines)
            elif (parameter == 'latency'):
                ret_str = get_latency(lines)
            else:
                ret_str = ''

        elif (benchmark == 'threads'):
            if (parameter == 'num_events'):
                ret_str = get_num_events(lines)
            elif (parameter == 'latency'):
                ret_str = get_latency(lines)
            else:
                ret_str = ''

        elif (benchmark == 'mutex'):
            if (parameter == 'latency'):
                ret_str = get_latency(lines)
            else:
                ret_str = ''

        else:
            if (parameter == 'write_throughput'):
                ret_str = get_write_throughput(lines)
            elif (parameter == 'read_throughput'):
                ret_str = get_read_throughput(lines)
            elif (parameter == 'latency'):
                ret_str = get_latency(lines)
            else:
                ret_str = ''
        try:
            ret_float = float(ret_str)
            return ret_float
        except ValueError:
            print('Can\'t convert to float!')

def get_values(platform_path):
    new_dict = {}

    # CPU
    cpu_speed = get_specific_value(platform_path, 'cpu', 'speed')
    new_dict['cpu_speed'] = cpu_speed

    cpu_latency = get_specific_value(platform_path, 'cpu', 'latency')
    new_dict['cpu_latency'] = cpu_latency

    # Memory
    memory_mib = get_specific_value(platform_path, 'memory', 'mib')
    new_dict['memory_mib'] = memory_mib

    memory_latency = get_specific_value(platform_path, 'memory', 'latency')
    new_dict['memory_latency'] = memory_latency

    # Threads
    threads_num_events = get_specific_value(platform_path, 'threads', 'num_events')
    new_dict['threads_num_events'] = threads_num_events

    threads_latency = get_specific_value(platform_path, 'threads', 'latency')
    new_dict['threads_latency'] = threads_latency

    # Mutex
    mutex_latency = get_specific_value(platform_path, 'mutex', 'latency')
    new_dict['mutex_latency'] = mutex_latency

    # Fileio Seqwr
    seqwr_write_throughput = get_specific_value(platform_path, 'seqwr', 'write_throughput')
    new_dict['seqwr_write_throughput'] = seqwr_write_throughput

    seqwr_latency = get_specific_value(platform_path, 'seqwr', 'latency')
    new_dict['seqwr_latency'] = seqwr_latency

    #Fileio Seqrewr
    seqrewr_write_throughput = get_specific_value(platform_path, 'seqrewr', 'write_throughput')
    new_dict['seqrewr_write_throughput'] = seqrewr_write_throughput

    seqrewr_latency = get_specific_value(platform_path, 'seqrewr', 'latency')
    new_dict['seqrewr_latency'] = seqrewr_latency

    # Fileio Seqrd
    seqrd_read_throughput = get_specific_value(platform_path, 'seqrd', 'read_throughput')
    new_dict['seqrd_read_throughput'] = seqrd_read_throughput

    seqrd_latency = get_specific_value(platform_path, 'seqrd', 'latency')
    new_dict['seqrd_latency'] = seqrd_latency

    # Fileio Rndrd
    rndrd_read_throughput = get_specific_value(platform_path, 'rndrd', 'read_throughput')
    new_dict['rndrd_read_throughput'] = rndrd_read_throughput

    rndrd_latency = get_specific_value(platform_path, 'rndrd', 'latency')
    new_dict['rndrd_latency'] = rndrd_latency

    # Fileio Rndwr
    rndwr_write_throughput = get_specific_value(platform_path, 'rndwr', 'write_throughput')
    new_dict['rndwr_write_throughput'] = rndwr_write_throughput

    rndwr_latency = get_specific_value(platform_path, 'rndwr', 'latency')
    new_dict['rndwr_latency'] = rndwr_latency

    # Fileio Rndrw
    rndrw_read_throughput = get_specific_value(platform_path, 'rndrw', 'read_throughput')
    new_dict['rndrw_read_throughput'] = rndrw_read_throughput

    rndrw_write_throughput = get_specific_value(platform_path, 'rndrw', 'write_throughput')
    new_dict['rndrw_write_throughput'] = rndrw_write_throughput

    rndrw_latency = get_specific_value(platform_path, 'rndrw', 'latency')
    new_dict['rndrw_latency'] = rndrw_latency

    return new_dict

def print_data(data):
    for run, run_dict in data.items():
        print('\n')
        print(run)
        df = pd.DataFrame(run_dict)
        print(df)

def save_data(data):
    i = 1
    for run, run_dict in data.items():
        df = pd.DataFrame(run_dict)
        df.to_csv('run_' + str(i) + '.csv')
        i += 1

def compute_averages(data):
    avg_data = {}
    std_data = {}
    host_dicts = []
    docker_dicts = []

    for run, run_dict in data.items():
        host_dicts.append(run_dict['host'])
        docker_dicts.append(run_dict['docker'])

    host_df = pd.DataFrame(host_dicts)
    host_avg = dict(host_df.mean())
    host_std = dict(host_df.std())
    avg_data['host'] = host_avg
    std_data['host'] = host_std

    docker_df = pd.DataFrame(docker_dicts)
    docker_avg = dict(docker_df.mean())
    docker_std = dict(docker_df.std())
    avg_data['docker'] = docker_avg
    std_data['docker'] = docker_std

    return avg_data, std_data

def print_data_average(data):
    avg_data, std_data = compute_averages(data)
    avg_df = pd.DataFrame(avg_data)
    print('\nAverages:')
    print(avg_df)
    print('\nStandard Deviations:')
    std_df = pd.DataFrame(std_data)
    print(std_df)

def save_data_average(data):
    avg_data, std_data = compute_averages(data)
    avg_df = pd.DataFrame(avg_data)
    avg_df.to_csv('run_avg.csv')
    std_df = pd.DataFrame(std_data)
    std_df.to_csv('run_std.csv')

def main(avg, save):
    data = {}
    i = 1
    new_run = 'run_' + str(i)

    while (path.exists(new_run)):
        new_run_dict = {}

        # host
        host_dict = {}
        host_path = new_run + '/host/'
        host_dict = get_values(host_path)
        new_run_dict['host'] = host_dict

        # Docker
        docker_dict = {}
        docker_path = new_run + '/docker/'
        docker_dict = get_values(docker_path)
        new_run_dict['docker'] = docker_dict

        data[new_run] = new_run_dict
        i += 1
        new_run = 'run_' + str(i)

    if (avg):
        if (save):
            save_data_average(data)
        else:
            print_data_average(data)

    else:
        if (save):
            save_data(data)
        else:
            print_data(data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Please input 2 arguments!')
        sys.exit()

    try:
        avg_int = int(sys.argv[1])
        if (avg_int > 1 or avg_int < 0):
            print('Please enter 0 or 1!')
            sys.exit()
        avg_bool = True if (avg_int == 1) else False
    except ValueError:
        print('Please use integers!')

    try:
        save_int = int(sys.argv[2])
        if (save_int > 1 or save_int < 0):
            print('Please enter 0 or 1!')
            sys.exit()
        save_bool = True if (save_int == 1) else False
    except ValueError:
        print('Please use integers!')

    main(avg_bool, save_bool)
