import pandas as pd 
import datetime as dt

def get_start_end_date_by_month_batch(start_dt, end_dt, batch=3, debug=False):

      """
        This function will provide list of start_date and end_date tuple 
        based on the batch number of months want to slice the input data range

        Ex: 2020-01-01 to 2020-12-31 will return 4 date ranges

        Batch 1: Date range from 2020-01-01 to 2020-03-31
        Batch 2: Date range from 2020-04-01 to 2020-06-30
        Batch 3: Date range from 2020-07-01 to 2020-09-30
        Batch 4: Date range from 2020-10-01 to 2020-09-30
      """
      try:
        print(f"User entered start_dt:{start_dt}  end_dt:{end_dt}")
        #Handle for start_dt is not the first date of a month
        ip_start_date = dt.datetime.strptime(start_dt, "%Y-%m-%d") 
        ip_end_date = dt.datetime.strptime(end_dt, "%Y-%m-%d") 
        print(f"Date format is valid")
        print(f"Get batch start_date and end_date ...")
        first_date_of_start_date = ip_start_date.replace(day=1) 
        months = pd.date_range(first_date_of_start_date, ip_end_date, 
                        freq='MS').strftime("%Y-%m").tolist()
        if debug: print(months)
        lens = len(months)
  
        if debug: print("months lens:",lens)
        to_add = 1 if lens%batch > 0 else 0
        base = int(lens/batch)
        months_to_run = [] 
        batch_months = batch
        for i in range(0, base+to_add):
          months_to_run.append(months[i*batch_months])
        
        if debug: print(months_to_run)
        start_end_date=[]
        
        for i in range(len(months_to_run)):
          if i==0:
            start_date = ip_start_date
          else:
            start_date = dt.datetime.strptime(months_to_run[i]+"-01", "%Y-%m-%d")
            
          if i < len(months_to_run)-1:
            end_date = dt.datetime.strptime(months_to_run[i+1]+"-01", "%Y-%m-%d") - dt.timedelta(1)
          else:
            end_date =  ip_end_date
          
          print(f"Batch {i+1}:  Date range from {start_date.date()} to {end_date.date()}")
          start_end_date.append((str(start_date.date()), str(end_date.date())))
        return start_end_date

      except Exception as e:
        print(e)
        e_msg = f"invalid {start_dt}, {end_dt}"
        raise ValueError(e_msg)


if __name__ == "__main__":

    
    get_start_end_date_by_month_batch("2020-01-01", "2020-12-31", batch=3, debug=False)
    get_start_end_date_by_month_batch("2020-01-01", "2020-12-31", batch=4, debug=False)
    get_start_end_date_by_month_batch("2020-01-01", "2020-12-31", batch=5, debug=False)
    get_start_end_date_by_month_batch("2020-01-01", "2020-12-31", batch=12, debug=False)
    get_start_end_date_by_month_batch("2020-01-01", "2020-12-31", batch=13, debug=False)
    # get_start_end_date_by_month_batch("2020-01-05", "2020-06-19", batch=3, debug=False)
    # get_start_end_date_by_month_batch("2020-01-05", "2020-02-19", batch=3, debug=False)
    # get_start_end_date_by_month_batch("2019-01-05", "2020-12-31", batch=3, debug=False)