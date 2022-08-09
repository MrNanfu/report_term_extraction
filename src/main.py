# -*- coding: utf-8 -*-
#这里用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本
from newmatch7 import parser


pathological_bodypart="左乳肿物2"
pathological_report="“二次补充报告：“左侧乳腺及肿物”见高级别导管原位癌（共3张切片见原位癌 X 4mm = 12mm,估记原位癌范围约12mm），部分乳腺间质见组织细胞，多核巨细胞及炎细胞浸润，未见浸润癌残留，基底切缘未见癌。"
ultrasound_bodypart="介入会诊：乳腺、腋窝及锁骨上下区（加弹性成像）"
ultrasound_report="左侧乳头深方导管局部扩张伴导管内异常回声：沉积物？左侧乳腺囊性结节，考虑BI-RADS 2类。右侧乳腺导管局部扩张，BI-RADS 2类。"
# ultrasound_report="左乳8-9点方位及右乳2点方位实性结节，BI-RADS 4a类，建议穿刺活检或密切动态观察。其余双侧乳腺内多发实质性团块：BI-RADS 3类。右侧乳腺内囊性结节，BI-RADS 2类。"
segmentsbnew_copy_step1, segmentscnew_copy_step1,segmentsbnew_copy_step2, segmentscnew_copy_step2,segmentsbfinal_output, segmentscfinal_output, matchresult_output=parser(pathological_bodypart,pathological_report,ultrasound_bodypart,ultrasound_report)
# segmentsbwithloc=[]
# segmentscwithloc=[]
# for i in range(len(pathological_report)):
#     segmentsbwithloc.append(pathological_report[i])
#     segmentsbwithloc.append(i)
# def findsegmentswithloc(report):
#     segmentswithloc = []
#     for i in range(len(report)):
#         segmentswithloc.append(report[i])
#         segmentswithloc.append(i)
#     return segmentswithloc
# segmentsbwithloc=findsegmentswithloc(pathological_report)
# segmentscwithloc=findsegmentswithloc(ultrasound_report)


print('\n')
print('提取到的原始病理信息为')
print(segmentsbnew_copy_step1)
print('提取到的原始超声信息为')
print(segmentscnew_copy_step1)
print("\n")
print('根据主要次要诊断筛选后的病理报告信息为')
print(segmentsbnew_copy_step2)
print('根据主要次要诊断筛选后的超声报告信息为')
print(segmentscnew_copy_step2)
print('\n')
print('归一化后的病理结果为')
print(segmentsbfinal_output)
print('归一化后的超声结果为')
print(segmentscfinal_output)
# print('\n')
print('匹配结果为')
print(matchresult_output)