# -*- coding: utf-8 -*-
#这里用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本
from newmatch7 import parser


# pathological_bodypart = "左乳肿物"
# pathological_report = "结果：镜下计数细胞40个；HER2信号总数88个，HER2信号均值2.73/细胞，CEP17信号总数79个，CEP17信号均值1.98/细胞，HER2/CEP17比值：1.11。肿瘤异质性：不明显。信号分布情况：点状分布。参考标准：乳腺癌HER2检测指南（2019版），中华病理学杂志，2019年3月。"
# ultrasound_bodypart = "乳腺|甲状腺|子宫附件|(女)肾输尿管膀胱|肝胆脾胰"
# ultrasound_report = ""

# pathological_bodypart = "左乳肿物"
# pathological_report = "“右乳”穿刺组织，符合腺病改变，伴囊肿形成。"
# ultrasound_bodypart = "乳腺"
# ultrasound_report = "右侧乳腺内实质性结节，BI-RADS 4a类。左侧乳腺局部导管扩张，BI-RADS 2类。"

segmentsbnew_copy_step1, segmentscnew_copy_step1,segmentsbnew_copy_step2, segmentscnew_copy_step2,pathological_results, ultrasound_results, matching_results=parser(pathological_bodypart,pathological_report,ultrasound_bodypart,ultrasound_report)
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
print(pathological_results)
print('归一化后的超声结果为')
print(ultrasound_results)
# print('\n')
print('匹配结果为')
print(matching_results)