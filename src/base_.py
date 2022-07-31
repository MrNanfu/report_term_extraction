import collections
import os.path

import pandas as pd
import glob
from datetime import datetime
from pandas import Timestamp

class File_Add():

    def read_excel_file_by_list(self,filelacation_bl,filesform = 'xls' ):
        '''
        读取excel文件
        :param filelacation: 文件路径
        :param filesform: 文件后缀
        :return: 返回列表
        '''

        part_bl = 0
        data = collections.deque([])
        for filename_bl in glob.glob(filelacation_bl + '*.' + filesform):
            filearray = collections.deque([])
            filearray.append(filename_bl)
            for i in range(len(filearray)):
                part_bl = pd.read_excel(filearray[i], converters={'身份证':str})
                # part_bl = pd.read_excel(filearray[i])#, converters={'身份证':str})
            data += part_bl.values.tolist()

        return data

    def read_excel_file_by_dict(self,filelacation_us, filesform ='xls'):
        '''
        读取excel文件
        :param filelacation: 文件路径
        :param filesform: 文件后缀
        :return: 返回列表
        '''

        part_bl = 0
        data = collections.deque([])
        dict_us = {}
        dict_0 = {}

        for filename_bl in glob.glob(filelacation_us + '*.' + filesform):
            filearray = collections.deque([])
            filearray.append(filename_bl)
            for i in range(len(filearray)):
                part_bl = pd.read_excel(filearray[i], converters={'身份证':str})
            data += part_bl.values.tolist()
        for j in range(len(data)):
            name1 = data[j][0]
            time_us = data[j][3]
            vals = data[j]
            if j == 0:
                dict_us[name1] = vals
            elif j > 0:
                for k in dict_us:
                    if name1 == dict_us[k][0] and time_us > dict_us[k][3]:
                        vals = data[j]
                    elif name1 != dict_us[k][0]:
                        dict_0[name1] = vals

        dict_us.update(dict_0)
        return dict_us

    def get_excel_data(self, data_bl, dict_us):
        '''
        获取文件中数据并提取、合并
        :param data_bl: 病理的所有数据
        :param dict_us: 超声的所有数据
        :return:
        '''

        name_bl = collections.deque([])           # 病理姓名存放列表
        new_excel = collections.deque([])          # 最终数据存放列表
        n = 0
        for i in data_bl:       # 在所有的病理表中循环
            name1 = str(i[0])
            data1 = i

            name_bl.append(name1)
            if name1 is None:
                pass
            else:
                if dict_us.get(name1) is None:
                    pass
                else:
                    data2 = dict_us.get(name1)
                    a = str(Timestamp.to_pydatetime(i[3]))
                    time_bl = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
                    time_us = datetime.strptime(str(data2[3]), '%Y-%m-%d %H:%M:%S')
                    # print(data2)
                    if 0 <= int((time_bl - time_us).days) < 90:
                        data = data1 + data2  # 符合条件则将病理数据与超声数据拼接
                        new_excel.append(data)
                    else:
                        pass

        return new_excel

    def write_excel(self,final_list):
        '''
        将数据写入excel
        :param final_list: 读取excel列表
        :return:
        '''

        excel_file = pd.DataFrame(columns = ('姓名', '检查部位', '检查时间', '年龄', '出生时间', '影像所见','影像诊断','检查部位','登记日期','检查所见', '诊断结果'))
        for i in range(len(final_list)):
            excel_file.loc[i] = [final_list[i][0], final_list[i][9], final_list[i][10], final_list[i][8],
                                 final_list[i][4], final_list[i][12], final_list[i][13], final_list[i][2],
                                  final_list[i][3], final_list[i][5], final_list[i][6]]
        return excel_file

    def write_excel_1(self,final_list):
        '''
        将数据写入excel
        :param final_list: 读取excel列表
        :return:
        '''

        excel_file = pd.DataFrame(columns=['病理-超市匹配结果'])
        for i in range(len(final_list)):
            excel_file.loc[i] = final_list[i]
        return excel_file