#使用时需要先关掉打开的excel文件，否则没有读写权限，会读取目录下合并完成表2020年9月那个excel，生成目录下叫a的excel
from base_ import File_Add
import time
start_time = time.time()
from base_read_excel import get_final_data


# 获取文件所在位置
filelocation_bl = './病理/'
filelocation_us = './超声/'
filelocation_all = './新数据/'
f = File_Add()
# 读取所有数据
#print('读取病理excel数据......')
#data_bl = f.read_excel_file_by_list(filelocation_bl,'xls')
#print('读取超声excel数据......')
#data_us = f.read_excel_file_by_dict(filelocation_us,'xls')
# 将数据按照需求提取、合并
#print('开始合并......')
#final_list = f.get_excel_data(data_bl,data_us)
# 将数据写入excel
#excel_file = f.write_excel(final_list)
# 输出
#excel_file.to_excel('合并完成表.xlsx')

data_all = f.read_excel_file_by_list(filelocation_all, 'xlsx')

a = get_final_data(data_all)


b = f.write_excel_1(a)
b.to_excel('./b.xlsx')
end_time = time.time()
print('合并完成      运行时间为：%s Seconds '%(end_time-start_time))
