import os.path
from yolosplitter import YoloSplitter
from datetime import datetime
def split_and_save(input_path):
    # input_path = input("Enter path to input dataset: ")
    try:
        ys = YoloSplitter(imgFormat=['.jpg','.jpeg','.png'],labelFormat=['.json'])

        df=ys.from_mixed_dir(input_dir=input_path,ratio=(0.8,0.1,0.1))
        date_month_year_hour = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        output_name = f'{os.path.basename(input_path)}_{date_month_year_hour}'
        # print(ys.show_dataframe)
        # output_path = os.path.join(os.path.dirname(input_path),f"{output_name}")
        output_path = os.path.join(input_path,f"{output_name}")
        ys.save_split(output_dir=output_path)

        return output_path
    except Exception as E:
        print(E)
        return -1

input_path = input("Enter root path to datasets: ")
split_and_save(input_path)