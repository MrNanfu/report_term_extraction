#这里用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本
from newmatch7 import parser

# pathological_bodypart='右乳肿物'
# pathological_report="“左乳肿物”叶状肿瘤，考虑为良性。需予随诊观察，监测有无复发。“右乳肿物”纤维腺瘤。"
# ultrasound_bodypart="浅表彩超：乳腺。"
# ultrasound_report='双侧乳腺内实质性团块，BI-RADS 3类。'

pathological_bodypart='右乳肿物'
pathological_report="二次报告：“左乳腺”主体为导管原位癌（共2处病变，最大径分别约2.8cm及1.0cm；中-高级核：实性型、筛状型、粉刺样型），伴小叶癌化；局灶腺体结构欠规则，结合免疫组化，符合浸润性癌（非特殊型），共2个主病灶，最大径分别约3.0mm及1.1mm，2级（腺管形成3分，核异型2分，核分裂1分，总分6分）。注：加做浸润性癌ER、PR、HER2、Ki67免疫组化进行中，结果待补充报告。"
ultrasound_bodypart="浅表彩超：乳腺。"
ultrasound_report='左侧乳腺10点方位低回声结节，增强超声（CEUS）考虑BI-RADS 3类，粘稠囊肿可能。'

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