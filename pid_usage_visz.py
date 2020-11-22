import psutil
from datetime import datetime as dt
import pandas as pd
import time
import os
import csv
import sys

import plotly.express as px



if __name__ == "__main__":

    pid = (sys.argv[1])
    
    print(f"\n ============ Open {pid} log ============ ")
    
    log_file_name = f'pid_{pid}.csv'
    log_entries_pdf = pd.read_csv(log_file_name, encoding='utf8', header=0)
    

    print(log_entries_pdf)

    mem_rss = log_entries_pdf[['current_time', 'memory_usage_rss']]
    mem_rss = mem_rss.rename(columns={"memory_usage_rss": "value"})
    mem_rss['metric'] = "Memory RSS"


    # mem_uss = log_entries_pdf[['current_time', 'memory_usage_uss']]
    # mem_uss = mem_uss.rename(columns={"memory_usage_uss": "value"})
    # mem_uss['metric'] = "Memory USS"
    
    data_df =  pd.concat([mem_rss])
    # print(mem_rss)
    # print(mem_uss)


    # FIELD_NAMES = [ 'pid','create_time','current_time',
    #                 'cpu_usage', 'memory_usage_rss',
    #                 'memory_usage_uss', 'num_threads']
    
    fig = px.line(data_df, x="current_time", y="value", color='metric')
    fig.show()


# else:

#     with open(log_file_name, 'a') as f:
#         writer = csv.DictWriter(f, fieldnames=field_names) 
#         writer.writerow(process_info)


# .strftime("%Y-%m-%d %H:%M:%S")


 
# print(os.path.isfile('.pid_15664csv'))




# df.to_csv(f'{pid}.csv', mode='a', header=False)

#for each PID log the CPU change and Mem change
#while PID exist collect stats every 1 second
#append the entry into pd
#save csv
#create line chart from it

# df = construct_dataframe(processes)
# if n == 0:
#     print(df.to_string())
# elif n > 0:
#     print(df.head(n).to_string())
# # print continuously

# while live_update:
#     # get all process info
#     processes = get_processes_info()
#     df = construct_dataframe(processes)
#     # clear the screen depending on your OS
#     os.system("cls") if "nt" in os.name else os.system("clear")
#     if n == 0:
#         print(df.to_string())
#     elif n > 0:
#         print(df.head(n).to_string())
#     time.sleep(0.7)




# def to_pd(proc):
#     # convert to pandas dataframe
#     df = pd.DataFrame(proc)
#     # set the process id as index of a process
#     # df.set_index('pid', inplace=True)
#     # sort rows by the column passed as argument
#     # df.sort_values(sort_by, inplace=True, ascending=not descending)
#     # convert to proper date format
#     df['create_time'] = df['create_time'].apply(dt.strftime, args=("%Y-%m-%d %H:%M:%S",))
#     df['current_time'] = df['current_time'].apply(dt.strftime, args=("%Y-%m-%d %H:%M:%S",))

#     return df

# df = to_pd(proccess_log)


    # print(f" p.create_time() {p.create_time()}")
    # print(f" p.cpu_times() {p.cpu_times()}")
    # print(f" p.cpu_percent() {p.cpu_percent()}")
    
    # print(f" p.memory_percent() {p.memory_percent(memtype="rss")}")
    # print(f" p.memory_percent() {round(p.memory_percent(), 3) * 100}%")
    # print(f" p.memory_maps() {p.memory_full_info().rss >> 20}")
    # print(f" p.memory_maps() {p.memory_full_info().uss >> 20}")
