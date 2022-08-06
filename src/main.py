# -*- coding: utf-8 -*-
#这里用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本
from newmatch7 import parser

pathological_bodypart="左乳肿物及周围腺体;切缘3补充组织"
pathological_report="三次报告1、“左乳肿物及周围腺体”化疗后标本：乳腺导管扩张，局灶呈腺病，纤维腺瘤样增生，导管上皮柱状细胞变，小叶硬化，局灶间质泡沫样组织细胞聚集，淋巴细胞浸润，局灶钙化，未见确切癌组织。新辅助治疗反应的评估：5级。2、“切缘3补充组织”乳腺组织，呈腺病改变，导管内见出血、泡沫样组织细胞、钙化，周围见吞噬含铁血黄素细胞，数个钙化灶，间质淋巴细胞浸润，结合免疫组化，未见确切癌组织。"
ultrasound_bodypart="介入会诊：乳腺、腋窝及锁骨上下区（加弹性成像"
ultrasound_report="左侧乳腺内实质性团块，BI-RADS 6类（病灶较2020.8.19缩小）。左侧乳腺内囊性结节，BI-RADS 2类。右侧乳腺BI-RADS 2类。"
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