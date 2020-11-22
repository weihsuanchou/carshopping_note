import psutil
from datetime import datetime as dt
import pandas as pd
import time
import os
import csv
import sys




def get_process_info(pid):

    p = psutil.Process(pid)

    with p.oneshot():
        
        """
        
        - RSS is the total memory actually held in RAM for a process

        - USS is the total private memory for a process, i.e. that memory that is completely ,unique to that process. 
        
            USS is an extremely useful number because it indicates the true incremental cost of running a particular process.
            
            aka “Unique Set Size”, this is the memory which is unique to a process and which would be freed if the process was terminated right now.

        - num_threads The number of threads currently used by this process (non cumulative).
        """
        create_time =  dt.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
        memory_usage_rss = p.memory_full_info().rss >> 20
        memory_usage_uss = p.memory_full_info().uss >> 20
        cpu_usage = p.cpu_percent()
        num_threads = p.num_threads()  
        current_time = dt.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")#.strftime("%Y-%m-%d %H:%M:%S") #dt.now().strftime("%Y-%m-%d %H:%M:%S")

        process_info = {
                'pid': pid, 'create_time': create_time, 'current_time': current_time, 
                'cpu_usage': cpu_usage, 'memory_usage_rss': memory_usage_rss, 
                'memory_usage_uss': memory_usage_uss, 'num_threads': num_threads
            }

    return process_info

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def write_to_csv(log_file_name, field_names, entry):

    new_file = not os.path.isfile(log_file_name)

    with open(log_file_name, 'a', newline='') as f:

        writer = csv.DictWriter(f, fieldnames=field_names)

        if new_file:
             writer.writeheader()

        writer.writerow(entry)


def show_chart(log_file_name):


    log_entries_pdf = pd.read_csv(log_file_name, encoding='utf8', header=0)
    
    # print(log_entries_pdf)

    mem_rss = log_entries_pdf[['current_time', 'memory_usage_rss']]
    mem_rss = mem_rss.rename(columns={"memory_usage_rss": "value"})
    mem_rss['metric'] = "Memory RSS"


    # mem_uss = log_entries_pdf[['current_time', 'memory_usage_uss']]
    # mem_uss = mem_uss.rename(columns={"memory_usage_uss": "value"})
    # mem_uss['metric'] = "Memory USS"
    
    data_df =  pd.concat([mem_rss])
    # print(mem_rss)
    # print(mem_uss)


    fig = px.line(data_df, x="current_time", y="value", color='metric')
    fig.show()





if __name__ == "__main__":

    pid = (sys.argv[1])
    time_interval_in_second = (sys.argv[2])
    
    print(f"\n ============ Track {pid} is started,  refresh in every {time_interval_in_second} second ============ ")


    log_file_name = f'pid_{pid}.csv'
    
    FIELD_NAMES = [ 'pid','create_time','current_time',
                    'cpu_usage', 'memory_usage_rss',
                    'memory_usage_uss', 'num_threads']
                    
    while True:
 
        process_info= get_process_info(int(pid))
        write_to_csv(log_file_name, FIELD_NAMES, process_info)
        time.sleep(float(time_interval_in_second))

    print(f"write to {log_file_name}")

    show_chart(log_file_name)
