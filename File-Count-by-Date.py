import os
import datetime

# مسیر پوشه مورد نظر
folder_path = r'C:\Users\Ramin_Csy\Desktop\فایل های دفتر'

# لیستی از نام فایل‌ها در پوشه
files = os.listdir(folder_path)

# با توجه به تاریخ‌های فایل‌ها، لیستی از تاپل‌ها به شکل (نام فایل، تاریخ ایجاد) ایجاد می‌شود
file_dates = [(file, datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(folder_path, file)))) for file in files]

# دیکشنری‌ای که تعداد فایل‌های هر روز را در آن نگهداری می‌کنیم
file_counts = {}

# بررسی هر تاریخ و افزودن تعداد فایل‌های موجود در آن تاریخ به دیکشنری
for file_date in file_dates:
    date_str = file_date[1].strftime("%Y-%m-%d")
    if date_str in file_counts:
        file_counts[date_str] += 1
    else:
        file_counts[date_str] = 1

# نام فایلی که نتیجه را در آن ذخیره می‌کنیم
output_file_name = os.path.join("C:\\Users\\Ramin_Csy\\Desktop", "result.txt")


# ایجاد فایل خروجی و نوشتن تعداد فایل‌های هر روز در آن
with open(output_file_name, "w") as f:
    for date_str, count in file_counts.items():
        f.write(f"{date_str}: {count}\n")
