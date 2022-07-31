# coding:utf-8
from newmatch7 import parser


#该方法包含了其他程序使用CPU的时间

import datetime
import string

#
# pathological_bodypart='脚踝'
# pathological_report="左侧腰背部脂肪瘤"
# # input2="右手，考虑左侧腱鞘巨细胞瘤"
# ultrasound_bodypart="脚踝。"
# ultrasound_report='腰背部脂肪瘤。'
#
# pathological_bodypart=input("输入病理参考部位:")
# pathological_report=input("输入病理报告:")
# ultrasound_bodypart=input("输入超声参考部位:")
# ultrasound_report=input("输入超声报告:")
def findsegmentswithloc(report):
    segmentswithloc = []
    for i in range(len(report)):
        segmentswithloc.append(report[i])
        segmentswithloc.append(i)
    return segmentswithloc
def get_final_data(data_all):
    result2 = []
    pathological_bodypart = []
    pathological_report = []
    ultrasound_bodypart = []
    ultrasound_report = []
    for i in data_all:
        #print(i)
        if len(i) == 0 or i[0]==None or i[1]==None or  i[2]==None or  i[3]==None or  i[4]==None or  i[5]==None:
                    print("跳过以下内容：")
                    print('\n')
                    print(i)
                    pass
        else:
            pathological_bodypart= str(i[0])
            c = str(i[1])
            d = str(i[2])
            # pathological_report = c + d
            pathological_report = d
            ultrasound_bodypart= str(i[3])
            a = str(i[4])
            b = str(i[5])
            # ultrasound_report = a + b
            ultrasound_report = b
            # ultrasound_report.append(i[11])

            print(ultrasound_report)
            segmentsbnew_copy_step1, segmentscnew_copy_step1,segmentsbnew_copy_step2, segmentscnew_copy_step2, segmentsbfinal_output, segmentscfinal_output, matchresult_output = parser(pathological_bodypart,
                                                                                             pathological_report,
                                                                                             ultrasound_bodypart,
                                                                                             ultrasound_report)
            R1 = ['提取到的原始病理信息为：']
            R2 = ['提取到的原始超声信息为: ']
            R3=['根据主要次要诊断筛选后的病理报告信息为：']
            R4=['根据主要次要诊断筛选后的超声报告信息为: ']
            R5=['病理归一化结果为: ']
            R6=['超声归一化结果为: ']
            R7=['匹配结果: ']
            # results=[*R1, *segmentsbnew_copy_step1 ,";\n",
            #          *R2, *segmentscnew_copy_step1, ";\n",
            #          *R3, *segmentsbnew_copy_step2 ,";\n",
            #          *R4, *segmentscnew_copy_step2, ";\n",
            #          *R5, *segmentsbfinal_output ,";\n",
            #          *R6, *segmentscfinal_output ,";\n",
            #          *R7, *matchresult_output ,"\n"]
            results=[
                     *R5, *segmentsbfinal_output ,";\n",
                     *R6, *segmentscfinal_output ,";\n",
                     *R7, *matchresult_output ,"\n"]
            r2=",".join(str(v) for v in results)
            result2.append(r2)
            print("语义匹配结束")
    return result2




