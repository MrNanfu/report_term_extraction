#这里用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本
from newmatch7 import parser

pathological_bodypart='右乳肿物'
pathological_report="“右乳”穿刺组织，初步考虑为乳腺纤维腺瘤，部分导管上皮增生活跃，建议免疫组化协诊。如同意做免疫组化请来病理科。"
ultrasound_bodypart="浅表彩超：乳腺、腋窝及锁骨上下区"
ultrasound_report="右侧乳腺10-2点方位实质性团块，考虑BI-RADS 4a类，建议密切随诊复查，必要时穿刺活检。双侧乳腺实质性结节，BI-RADS 3类，建议定期复查。"
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