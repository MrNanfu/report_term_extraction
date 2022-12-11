# -*- coding: utf-8 -*-
#这里用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本
from newmatch7 import parser

import json


pathological_bodypart = "右乳肿物2"
pathological_report = "1、“右侧乳腺”浸润性癌，Ⅱ级（腺管形成3分，核异型2分，核分裂1分，总分6分），伴导管原位癌（中级别，待免疫组化明确比例），肿物最大径约1.3cm，周围乳腺呈腺病改变，乳头、乳头基底、肿物表面皮肤、基底切缘未见癌。2、“右侧腋窝淋巴结”淋巴结见转移癌（2/10），均为宏转移。免疫组化结果待二次报告。"
ultrasound_bodypart = "介入会诊：乳腺、腋窝及锁骨上下区（加弹性成像）"
ultrasound_report ="左乳切除术后：左胸壁实质性结节，建议穿刺活检。右乳9点实质性团块，BI-RADS 6类。右乳腺内导管扩张并导管内占位，BI-RADS 4a类。右腋窝转移淋巴结。左胸骨旁、左锁骨下区异常淋巴结，建议FNA。"
# def convert_matching_results_dict_list(result_list):
#     result_dict_list = []
#     result_dict = {}
#
#     bodypart_index = 0
#     side_index = 1
#     pathological_index = 2
#     physical_property_index = 3
#     benign_or_malignant_index = 4
#
#     for i in range(len(result_list)):
#         bodypart_dict = {
#             "pathological": result_list[i][bodypart_index][0],
#             "ultrasound": result_list[i][bodypart_index][1],
#             "matching_degree": result_list[i][bodypart_index][2]
#         }
#         side_dict = {
#             "pathological": result_list[i][side_index][0],
#             "ultrasound": result_list[i][side_index][1],
#             "matching_degree": result_list[i][side_index][2]
#         }
#         pathological_dict = {
#             "pathological": result_list[i][pathological_index][0],
#             "ultrasound": result_list[i][pathological_index][1],
#             "matching_degree": result_list[i][pathological_index][2]
#         }
#         physical_property_dict = {
#             "pathological": result_list[i][physical_property_index][0],
#             "ultrasound": result_list[i][physical_property_index][1],
#             "matching_degree": result_list[i][physical_property_index][2]
#         }
#         benign_or_malignant_dict = {
#             "pathological": result_list[i][benign_or_malignant_index][0],
#             "ultrasound": result_list[i][benign_or_malignant_index][1],
#             "matching_degree": result_list[i][benign_or_malignant_index][2]
#         }
#         result_dict['bodypart'] = bodypart_dict
#         result_dict['side'] = side_dict
#         result_dict['results'] = {}
#         result_dict['results']['pathological'] = pathological_dict
#         result_dict['results']['physical_property'] = physical_property_dict
#         result_dict['results']['benign_or_malignant'] = benign_or_malignant_dict
#
#         result_dict_list.append(result_dict)
#
#     return result_dict_list
#
# # 将转成字典数组
# def convert_pathological_or_ultrasound_results_dict_list(results):
#     result_dict_list = []
#     for i in range(len(results)):
#         result_dict = {
#             "bodypart": results[i][0][0],
#             "side": results[i][1][0],
#             "pathological": results[i][2][0],
#             "physical_property": results[i][3][0],
#             "benign_or_malignant": results[i][4][0]}
#         result_dict_list.append(result_dict)
#     return result_dict_list
#
# def json_file(pathological_bodypart,pathological_report,ultrasound_bodypart,ultrasound_report):
#     _, _, _,_,  pathological_results, ultrasound_results, matching_results = parser(pathological_bodypart,pathological_report,ultrasound_bodypart,ultrasound_report)
#     matching_results_dict_list = convert_matching_results_dict_list(matching_results)
#
#     # 字典类型
#     result_dict = {}
#     result_dict['pathological_results'] = convert_pathological_or_ultrasound_results_dict_list(pathological_results)
#     result_dict['ultrasound_results'] = convert_pathological_or_ultrasound_results_dict_list(ultrasound_results)
#     result_dict['matching_results'] = matching_results_dict_list
#
#     # 返回json字符串
#     return json.dumps(result_dict)
#
# result_json_str= json_file(pathological_bodypart, pathological_report, ultrasound_bodypart, ultrasound_report)
#
# print('result_json_str: ')
# print(result_json_str)

_, _, _,_, segmentsbfinal_output, segmentscfinal_output, matchresult_output = parser(pathological_bodypart,pathological_report,  ultrasound_bodypart,ultrasound_report)
print("病理归一化结果：")
print(segmentsbfinal_output)

print("超声归一化结果：")
print(segmentscfinal_output)

print("匹配结果：")
print(matchresult_output)
