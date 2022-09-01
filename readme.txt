base.py,base_read.py都是由main_excel文件调用的，main.py和main_excel.py都是输入输出的文件，这些文件都不需要管
只需要重点看pathological.py(处理病理信息)和几乎和它对应的ultrasound.py（处理超声信息），以及Newmatch7.py(处理匹配信息)
main文件用于自己调试代码时试验，调整Input的值，看各个情况下结果是否满足。用于单独的试验。批量跑excel数据批量试验用的是main_excel脚本。

在Main文件中输入pathological_bodypart、pathological_report、ultrasound_bodypart、ultrasound_report的值
执行parser函数后 得到结果 在Main中print出来

示例：
输入：

pathological_bodypart='右腋窝淋巴结;右乳腺肿物及周围组织'
pathological_report="1、“右乳”恶性肿瘤，见结节两枚，初步考虑为浸润性癌，伴导管原位癌，待免疫组化补充报告。2、“右腋窝淋巴结”。"
ultrasound_bodypart="介入会诊：乳腺、腋窝及锁骨上下区（加弹性成像）。"
ultrasound_report='右侧乳腺6点实性结节，BI-RADS 6类。右侧乳腺7点实性结节，BI-RADS 4c类。'

输出结果：

归一化后的病理结果为
[[['右乳'], ['右'], ['浸润性癌'], ['实性'], ['良性']]]
归一化后的超声结果为
[[['右乳'], ['右'], ['BI-RADS 6'], ['实性'], ['恶性']]]
匹配结果为
[[['右乳', '右乳', '0'], ['右', '右', '0'], ['浸润性癌', 'BI-RADS 6', '1'], ['实性', '实性', '0'], ['良性', '恶性', '1']]]


json格式结果：
病理结果：
[
    {
        "部位": "右乳",
        "侧别": "右",
        "病理性质": [
            "浸润性癌"
        ],
        "物理性质": "实性",
        "良恶性": "良性"
    }
]

超声结果：
[
    {
        "部位": "右乳",
        "侧别": "右",
        "病理性质": [
            "BI-RADS 6"
        ],
        "物理性质": "实性",
        "良恶性": "恶性"
    }
]

匹配结果：
[
    {
        "部位": "0",
        "侧别": "0",
        "病理性质": "1",
        "物理性质": "0",
        "良恶性": "1"
    }
]