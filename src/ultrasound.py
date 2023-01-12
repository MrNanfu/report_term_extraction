# -*- coding:utf-8 -*-
#有一些demo只在pathological那边做了，比如否定词的处理，超声这边没加，主要否定词也是主要出现在病理那边，后续应该加上
from pathological import word_probbinglicebie,word_probbinglibuwei,word_probbingliwuli,word_probchaoshengwuli,word_probbingliliangexing,word_probchaoshengliangexing,word_probchaoshengcebie,word_probchaoshengbuwei

from pathological import findsegments

word_probexing_major={"浸润性乳头状癌":0.01,"浸润性导管癌":0.01,"浸润性癌":0.01, "浸润癌":0.01, "浸润性乳腺癌":0.01,"导管原位癌":0.01,"原位癌":0.01,"恶性叶状肿瘤":0.01,"包裹性乳头状癌":0.01,"实性乳头状癌":0.01,"导管内乳头状癌":0.01, "化生性癌":0.01, "BI-RADS 4C":0.01,"BI-RADS 4c":0.01,"4c":0.01,"4C":0.01,"BI-RADS 5":0.01,"BI-RADS 6":0.01}
word_probliang_or_e_major={"导管内瘤":0.01, "肿瘤病变":0.01, "导管内乳头状病变":0.01, "纤维上皮性病变":0.01, "肿瘤性病变":0.01, "导管内乳头状肿瘤":0.01,"叶状肿瘤":0.01,"放射状瘢痕〈B3,不确定的潜在恶性病变）":0.01,"非典型导管增生":0.01,"非典型导管上皮增生":0.01, "导管上皮不典型增生":0.01, "导管上皮非典型增生":0.01, "平坦型上皮非典型增生":0.01,"平坦上皮非典型性":0.01,"导管上皮轻度非典型增生":0.01,"不典型增生":0.01,"导管上皮增生活跃":0.01, "非典型增生":0.01, "不典型导管增生":0.01, "导管上皮增生":0.01,"导管上皮增生稍活跃(B3,不确定的潜在恶性病变）":0.01,"上皮源性肿瘤":0.01,"BI-RADS 0": 0.01}
word_probliangxing_major={"导管内沉积物":0.01,"普通型增生":0.01, "肉芽肿":0.01,"肉芽肿性炎":0.01, "硬化性腺病":0.01, "错构瘤":0.01, "导管内乳头状瘤":0.01, "导管内乳头状瘤炎性病变":0.01,"炎性":0.01,"炎症性改变":0.01,"炎症性":0.01,"炎症改变":0.01,"小叶性肉芽肿性乳腺炎":0.01,"小叶肉芽肿性乳腺炎":0.01,"肉芽肿性小叶炎":0.01,"肉芽肿性小叶性乳腺炎":0.01,"非特异性炎症性病变纤维上皮肿瘤":0.01, "梭形细胞病变":0.01, "非特异性炎症性病变":0.01, "纤维上皮性":0.01, "纤维上皮性肿瘤":0.01,"良性纤维上皮性肿瘤":0.01,"纤维腺瘤样增生":0.01,"纤维腺瘤":0.01,"纤维腺瘤改变":0.01,"幼年型纤维腺瘤":0.01,"良性叶状肿瘤":0.01,"泌乳性腺瘤":0.01,"管状腺瘤":0.01,"结节性泌乳性增生硬化性腺病":0.01, "结节性泌乳性增生":0.01, "错构瘤硬化性腺病":0.01, "复杂硬化性":0.01, "复杂性硬化性":0.01, "复杂硬化性病变":0.01, "表皮样囊肿":0.01, "复杂性硬化性病表皮样囊肿":0.01,"纤维囊性乳腺病":0.01,"纤维囊性变":0.01,"囊肿性病变":0.01, "积乳囊肿":0.01, "囊肿":0.01,"导管扩张症新辅助治疗后改变":0.01,"化疗后改变":0.01,"未见确切恶性肿瘤细胞":0.01,"未见肿瘤":0.01,"BI-RADS 1":0.01,"BI-RADS 2":0.01,"BI-RADS 3":0.01,'BI-RADSⅢ':0.01, "BI-RADS 4A":0.01,
                      "BI-RADS 4B":0.01,"BI-RADS 4a":0.01,"BI-RADS 4b":0.01,"4a":0.01,"4b":0.01, "4A":0.01,"4B":0.01,"BI-RADS 4 a":0.01}
word_probliangxing_minor={"胶原增生":0.01,"增生结节":0.01,"瘤样增生":0.01,"腺病":0.01,"间质纤维胶原组织增生":0.01,"假血管瘤样增生":0.01,"脂肪瘤":0.01,"囊肿": 0.01,"柱状细胞增生":0.01,"柱状细胞变":0.01,"导管上皮柱状细胞变":0.01,"柱状上皮化生腺病":0.01,"导管上皮普通型增生":0.01,"导管上皮呈普通型增生":0.01,"导管上皮呈筛状增生":0.01,"导管上皮呈旺炽性增生":0.01,"导管普通型增生":0.01,"筛孔状增生":0.01,"导管上皮轻度增生":0.01,"导管上皮增生脂肪组织坏死纤维胶原增生":0.01,"间质纤维增生":0.01,"间质胶原增生":0.01, "间质胶原纤维增生":0.01, "胶原纤维增生":0.01, "大汗腺化生":0.01, "假血管瘤样间质增生":0.01,"假血管瘤样间质增生大汗腺化生":0.01,"腺病":0.01}


#整体恶性词典、整体良恶性均可词典、整体良性词典
word_probexing=word_probexing_major
word_probliang_or_e=word_probliang_or_e_major
word_probliangxing={**word_probliangxing_major, **word_probliangxing_minor}

word_probchaoshengbingli={**word_probexing, **word_probliang_or_e_major,**word_probliangxing}

def Merge(dict1, dict2, dict3, dict4):
    res = {**dict1, **dict2, **dict3, **dict4}
    return res
word_reliability = {"建议": 0.01, "鉴别": 0.01, "排除": 0.01, "待": 0.01, "需": 0.01, "进一步": 0.01}
word_prob_invalid = {'切缘': 0.01, '皮缘': 0.01, '新辅': 0.01, '化疗': 0.01, '副乳': 0.01}
word_probchaoshengall ={**word_probchaoshengbuwei, **word_probchaoshengwuli, **word_probchaoshengliangexing,**word_probchaoshengbingli,**word_prob_invalid}


def ultrasoundfuc(ultrasound_bodypart,ultrasound_report):
    global leninputchaosheng
    global segmentsc_full_stop
    input_str = ultrasound_report
    leninputchaosheng = len(input_str)

    word_prob_combine = {"及": 0.01}
    global segmentsc_merge
    segmentsc_merge = []
    segmentsc_merge = findsegments(input_str,word_probchaoshengall)
    segmentsc_combine = findsegments(input_str, word_prob_combine)
    # 对于类似于“左乳8-9点方位及右乳2点方位”这样的部位要进行预处理，将其转化为双乳
    cnt = 0
    for i in range(int(len(segmentsc_merge) / 2) - 1):
        if segmentsc_merge[2 * i] in word_probchaoshengbuwei and segmentsc_merge[2 * (i + 1)] in word_probchaoshengbuwei:
            if len(segmentsc_combine) != 0:
                for j in range(int(len(segmentsc_combine) / 2)):
                    if segmentsc_merge[2 * i + 1] < segmentsc_combine[2 * j + 1] < segmentsc_merge[2 * (i + 1) + 1]:
                        cnt += 2
                        segmentsc_merge[2 * (i + 1)] = -1
                        segmentsc_merge[2 * (i + 1) + 1] = -1
                        segmentsc_merge[2 * i] = '双乳'
    for i in range(cnt):
        segmentsc_merge.remove(-1)

    reliability = findsegments(input_str, word_reliability)
    invalid_c = findsegments(input_str, word_prob_invalid)
    # print('segmentsc_merge为')
    # print(segmentsc_merge)

    global segmentsc1, segmentsc2, segmentsc3, segmentsc4, segmentsc5, segmentsc6
    segmentsc1=[]#注意这里又加了b1，虽然这次任务用不上
    segmentsc2=[]
    segmentsc3=[]
    segmentsc3_raw = []
    segmentsc4=[]
    segmentsc4_raw=[]
    segmentsc5=[]
    segmentsc6=[]


    for i in range(int(len(segmentsc_merge) / 2)):
        if segmentsc_merge[2*i] in word_probchaoshengcebie:
            segmentsc1.append(segmentsc_merge[2 * i])
            segmentsc1.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probchaoshengbuwei:
            segmentsc2.append(segmentsc_merge[2 * i])
            segmentsc2.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probchaoshengwuli:
            segmentsc3.append(segmentsc_merge[2 * i])
            segmentsc3.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probchaoshengliangexing:
            segmentsc4.append(segmentsc_merge[2 * i])
            segmentsc4.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probchaoshengbingli:
            segmentsc5.append(segmentsc_merge[2 * i])
            segmentsc5.append(segmentsc_merge[2 * i + 1])

        # if segmentsc_merge[2 * i] in word_prob_invalid:
        #     segmentsc5.append("无效语句")
        #     segmentsc5.append(0)


    if int(len(reliability)) != 0:
        for i in range(int(len(reliability)/2)):
            for j in range(int(len(segmentsc2)/2)):
                if( j < int(len(segmentsc2)/2) - 1):
                    if segmentsc2[2 * j + 1] < reliability[2 * i + 1] < segmentsc2[2 * j + 3]:
                        segmentsc6.append("匹配结果可信度低")
                    else:
                        segmentsc6.append("匹配结果可信度高")
                else :
                    if segmentsc2[2 * j + 1] < reliability[2 * i + 1]:
                        segmentsc6.append("匹配结果可信度低")
                    else:
                        segmentsc6.append("匹配结果可信度高")

    elif int(len(reliability)) == 0:
        if int(len(segmentsc2) / 2) != 0:
            for j in range(int(len(segmentsc2) / 2)):
                segmentsc6.append("匹配结果可信度高")
        else:
                segmentsc6.append("匹配结果可信度高")

    # global segmentsc1
    # segmentsc1 = findsegments(input_str, word_probchaoshengcebie)

    word_probc1zuo = {"左": 0.01, "左侧": 0.01}
    word_probc1you = {"右": 0.01, "右侧": 0.01}
    for icgy1 in range(len(segmentsc1)):
        if segmentsc1[icgy1] in word_probc1zuo.keys():
            segmentsc1[icgy1] = '左'
        if segmentsc1[icgy1] in word_probc1you.keys():
            segmentsc1[icgy1] = '右'


    # global segmentsc2
    global segmentsc2temp

    # segmentsc2 = findsegments(input_str, word_probchaoshengbuwei)
    segmentsc2temp = 0
    if len(segmentsc2) == 0:
        segmentsc2.append(ultrasound_bodypart)
        segmentsc2.append(0)
        segmentsc2temp = 1
    word_probc2zhoubu = {"肘": 0.01}
    word_probc2shouwanbu = {"手": 0.01, "腕": 0.01, "指": 0.01, "虎口": 0.01}
    word_probc2xibu = {"膝": 0.01, "腘窝": 0.01}
    word_probc2zuhuaibu = {"足": 0.01, "踝": 0.01, "趾": 0.01}
    word_probc2xiongbi = {"胸": 0.01}
    # word_probc2xiongbi = {"胸": 0.01, "乳腺": 0.01} 胸的完全改了 乳腺不能算胸
    word_probc2fubi = {"腹": 0.01, "剑突": 0.01,"剑突下": 0.01, "脐": 0.01}
    word_probc2beibu = {"背": 0.01, "腰": 0.01, "胸背": 0.01}
    # word_probc2jianbu = {"肩": 0.01, "腋": 0.01}
    word_probc2jianbu = {"肩": 0.01}
    word_probc2kuanbu = {"腹股沟": 0.01, "髋": 0.01}
    word_probc2tunbu = {"骶": 0.01, "臀": 0.01, "肛": 0.01}
    word_probc2yanmianbu = {"颊": 0.01, "面": 0.01, "眼": 0.01, "眉": 0.01, "耳": 0.01, "颌": 0.01, "颏": 0.01}
    word_probc2toubu = {"顶": 0.01, "额": 0.01, "枕": 0.01, "颞": 0.01, "头皮": 0.01}
    # word_probc2jingbu = {"颈": 0.01, "锁骨上": 0.01}
    word_probc2jingbu = {"颈": 0.01}
    word_probc2yewosuogu = {"腋窝": 0.01, "锁骨": 0.01}
    word_probc2yewosuoguleft={"左侧腋窝": 0.01,"左侧锁骨": 0.01,"左腋窝": 0.01,"左锁骨": 0.01}
    word_probc2yewosuoguright = {"右侧腋窝": 0.01,"右侧锁骨": 0.01,"右腋窝": 0.01,"右锁骨": 0.01}
    word_probc2yewosuogudouble= {"双侧腋窝": 0.01,"双侧锁骨": 0.01,"双腋窝": 0.01,"双锁骨": 0.01}

    ## 部位归一化操作
    for ibgy2 in range(len(segmentsc2)):
        if segmentsc2[ibgy2] in word_probc2zhoubu.keys():
            segmentsc2[ibgy2] = '肘部'
        if segmentsc2[ibgy2] in word_probc2shouwanbu.keys():
            segmentsc2[ibgy2] = '手腕部'
        if segmentsc2[ibgy2] in word_probc2xibu.keys():
            segmentsc2[ibgy2] = '膝部'
        if segmentsc2[ibgy2] in word_probc2zuhuaibu.keys():
            segmentsc2[ibgy2] = '足踝部'
        if segmentsc2[ibgy2] in word_probc2xiongbi.keys():
            segmentsc2[ibgy2] = '胸壁'
        if segmentsc2[ibgy2] in word_probc2fubi.keys():
            segmentsc2[ibgy2] = '腹壁'
        if segmentsc2[ibgy2] in word_probc2beibu.keys():
            segmentsc2[ibgy2] = '背部'
        if segmentsc2[ibgy2] in word_probc2jianbu.keys():
            segmentsc2[ibgy2] = '肩部'
        if segmentsc2[ibgy2] in word_probc2kuanbu.keys():
            segmentsc2[ibgy2] = '髋部'
        if segmentsc2[ibgy2] in word_probc2tunbu.keys():
            segmentsc2[ibgy2] = '臀部'
        if segmentsc2[ibgy2] in word_probc2yanmianbu.keys():
            segmentsc2[ibgy2] = '颜面部'
        if segmentsc2[ibgy2] in word_probc2toubu.keys():
            segmentsc2[ibgy2] = '头部'
        if segmentsc2[ibgy2] in word_probc2jingbu.keys():
            segmentsc2[ibgy2] = '颈部'
        if segmentsc2[ibgy2] == '乳房腺体':
            segmentsc2[ibgy2] = '乳腺'
        if segmentsc2[ibgy2] == '右侧乳房腺体':
            segmentsc2[ibgy2] = '右侧乳腺'
        if segmentsc2[ibgy2] == '左侧乳房腺体':
            segmentsc2[ibgy2] = '左侧乳腺'
        if segmentsc2[ibgy2] == '双侧乳房腺体':
            segmentsc2[ibgy2] = '双侧乳腺'
        if segmentsc2[ibgy2] == '右侧副乳腺肿物':
            segmentsc2[ibgy2] = '右侧副乳'
        if segmentsc2[ibgy2] == '左侧副乳腺肿物':
            segmentsc2[ibgy2] = '左侧副乳'
        if segmentsc2[ibgy2] == '双侧副乳腺肿物':
            segmentsc2[ibgy2] = '双侧副乳'
        if segmentsc2[ibgy2] in word_probc2yewosuogu.keys():
            segmentsc2[ibgy2] = '腋窝及锁骨区'
        if segmentsc2[ibgy2] in word_probc2yewosuoguleft.keys():
            segmentsc2[ibgy2] = '左侧腋窝及锁骨区'
        if segmentsc2[ibgy2] in word_probc2yewosuoguright.keys():
            segmentsc2[ibgy2] = '右侧腋窝及锁骨区'
        if segmentsc2[ibgy2] in word_probc2yewosuogudouble.keys():
            segmentsc2[ibgy2] = '双侧腋窝及锁骨区'
    # global segmentsc3
    # segmentsc3 = findsegments(input_str, word_probchaoshengwuli)
    #
    # global segmentsc4
    # segmentsc4 = findsegments(input_str, word_probchaoshengliangexing)
    #
    # global segmentsc5
    # segmentsc5 = findsegments(input_str, word_probchaoshengbingli)

    # 否定词 出现否定词的时候 它形容的那些病理性质需要排除掉或者取反，下面列出了一些需要排除的

    word_prob_negative_word_all={'不支持':0.01,'有无': 0.01,'不排除':0.01,'排除':0.01,'鉴别':0.01,'不完全除外':0.01,'不能除外':0.01,'不除外':0.01,'除外':0.01,'未见': 0.01}

    # word_prob_negative_word_all = {'排除': 0.01, '鉴别': 0.01, '不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01, '除外': 0.01}
    word_prob_negative_word1 = {'排除': 0.01, '鉴别': 0.01, '除外': 0.01, '未见': 0.01}
    # word_prob_negative_word1 = {'排除': 0.01, '鉴别': 0.01,'除外': 0.01,'未见': 0.01}
    # 和上面切面那个问题同理，都是利用最大匹配的算法，这里由于不除外不能除外虽然表达肯定意思，但是如果不把这些词放里，就会提取到除外这样的否定词
    word_prob_negative_word2 = {'不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01 ,'考虑': 0.01, '疑' : 0.01}
    word_prob_comma={'，':0.01,'；':0.01,'、':0.01}#注意打字时候这里是中文标点
    word_prob_full_stop={'。':0.01}#中文句号
    word_prob_semicolon = {';':0.01}
    word_prob_sep = {**word_prob_full_stop, **word_prob_semicolon, **word_prob_comma}
  # 就是通过表格数据找寻规律，比如出现排除这种词，它前面第一个逗号到后面第一个句号里的词可能都需要排除掉，具体看表格里不同医生的写法去总结共性，然后这里也可以以后用NLP
    segmentsc_negative_word_all = findsegments(input_str, word_prob_negative_word_all)
    segmentsc_wuxiao_word = findsegments(input_str, word_prob_invalid)
    segmentsc_negative_word1 = []
    segmentsc_negative_word2 = []
    for i in range(int(len(segmentsc_negative_word_all)/2)):
        if segmentsc_negative_word_all[2*i] in word_prob_negative_word1:
            segmentsc_negative_word1.append(segmentsc_negative_word_all[2*i])
            segmentsc_negative_word1.append(segmentsc_negative_word_all[2*i+1])
        if segmentsc_negative_word_all[2*i] in word_prob_negative_word2:
            segmentsc_negative_word2.append(segmentsc_negative_word_all[2*i])
            segmentsc_negative_word2.append(segmentsc_negative_word_all[2*i+1])
    segmentsc_comma=findsegments(input_str, word_prob_comma)
    segmentsc_full_stop=findsegments(input_str, word_prob_full_stop)
    segmentsc_semicolon = findsegments(input_str, word_prob_semicolon)
    segmentsc_sep = findsegments(input_str, word_prob_sep)
    # print('segmentsb_negative_word,segmentsb_comma,segmentsb_full_stop为')
    # print(segmentsb_negative_word,segmentsb_comma,segmentsb_full_stop)

    # 按有多个否定词来处理

    segmentsc_negative_word_all_copy = segmentsc_negative_word_all.copy()
    segmentsc5new = []
    interval_negative = []
    for k in range(int(len(segmentsc_negative_word_all) / 2)):
        if len(segmentsc_negative_word_all_copy) != 0:
            loc_comma = 0
            loc_full_stop = 0
            loc_negative_word = segmentsc_negative_word_all_copy[2 * k + 1]
            for i in range(int(len(segmentsc_sep) / 2)):
                if segmentsc_sep[2 * i + 1] > loc_negative_word:
                    loc_full_stop = segmentsc_sep[2 * i + 1]
                    break
            # print('句号位置为')
            # print(loc_full_stop)
            for j in range(int(len(segmentsc_comma) / 2)):
                if j < int(len(segmentsc_comma) / 2 - 1):
                    if (segmentsc_comma[2 * j + 1] < loc_negative_word) and (
                            segmentsc_comma[2 * j + 3] > loc_negative_word):
                        loc_comma = segmentsc_comma[2 * j + 1]
                        break
                if j == int(len(segmentsc_comma) / 2 - 1):
                    if (segmentsc_comma[2 * j + 1] < loc_negative_word):
                        loc_comma = segmentsc_comma[2 * j + 1]
                        break
            # print('逗号位置为')
            # print(loc_comma)
            # 还没写 2*j+3超出去的情况
            interval_negative.append(loc_comma)
            interval_negative.append(loc_full_stop)

    if len(reliability) != 0 and len(interval_negative) != 0:
        for i in range(int(len(segmentsc5) / 2)):
            if segmentsc5[2 * i + 1] < interval_negative[0] or segmentsc5[2 * i + 1] > interval_negative[-1]:
                segmentsc5new.append(segmentsc5[2 * i])
                segmentsc5new.append(segmentsc5[2 * i + 1])
            else:
                for j in range(int(len(interval_negative) / 2) - 1):
                    if segmentsc5[2 * i + 1] > interval_negative[2 * j + 1] and segmentsc5[2 * i + 1] < \
                            interval_negative[2 * (j + 1)]:
                        segmentsc5new.append(segmentsc5[2 * i])
                        segmentsc5new.append(segmentsc5[2 * i + 1])
                        break
        segmentsc5 = segmentsc5new

        # print('segmentsb5new为')
        # print(segmentsb5new)
    if len(segmentsc_negative_word_all) != 0:
        loc_full_stop1 = -1
        loc_full_stop2 = -1
        """
        切缘相关的句号和逗号位置信息提取
        """
        if int(len(segmentsc_sep) / 2) == 1:
            for i in range(int(len(segmentsc_merge) / 2)):
                if segmentsc_merge[2 * i] in word_prob_invalid:
                    segmentsc5.append("无效语句")
                    segmentsc5.append(segmentsc_merge[2 * i + 1])
                    break
        else:
            if len(segmentsc_wuxiao_word) != 0:
                # 先按只有一个切缘来处理
                loc_wuxiao_word = segmentsc_wuxiao_word[1]
                for i in range(int(len(segmentsc_sep) / 2)):
                    if segmentsc_sep[2 * i + 1] > loc_wuxiao_word:
                        loc_full_stop2 = segmentsc_sep[2 * i + 1]
                        if 2 * i - 1 < 0:
                            loc_full_stop1 = 1
                        else:
                            loc_full_stop1 = segmentsc_sep[2 * i - 1]
                        break
        segmentsc5new = []
        for i in range(int(len(segmentsc5) / 2)):
            if segmentsc5[2 * i + 1] < loc_full_stop1 or segmentsc5[2 * i + 1] > loc_full_stop2:
                segmentsc5new.append(segmentsc5[2 * i])
                segmentsc5new.append(segmentsc5[2 * i + 1])
        segmentsc5 = segmentsc5new

        segmentsc3new = []
        for i in range(int(len(segmentsc3_raw) / 2)):
            if segmentsc3_raw[2 * i + 1] < loc_full_stop1 or segmentsc3_raw[2 * i + 1] > loc_full_stop2:
                segmentsc3new.append(segmentsc3_raw[2 * i])
                segmentsc3new.append(segmentsc3_raw[2 * i + 1])
        segmentsc3_raw = segmentsc3new

        ## 良恶性也要依据否定词进行修改
        def remove_liange(segmentsc4_raw, segmentsc_negative_word1):
            segmentsc4_after = []
            if int(len(segmentsc_negative_word1)) != 0:
                for i in range(int(len(segmentsc4_raw) / 2)):
                    for j in range(int(len(segmentsc_negative_word1) / 2)):
                        if -5 < segmentsc4_raw[2 * i + 1] - segmentsc_negative_word1[2 * j + 1] < 5:
                            segmentsc4_after.append(segmentsc4_raw[2 * i])
                            segmentsc4_after.append(segmentsc4_raw[2 * i + 1])
            return segmentsc4_after

        segmentsbc4_raw = remove_liange(segmentsc4_raw, segmentsc_negative_word1)

    global segmentsc5bf
    segmentsc5bf=segmentsc5.copy()


    word_probb5zhifangliu = {"脂肪瘤": 0.01, "血管脂肪瘤": 0.01, "肌内脂肪瘤": 0.01, "软骨样脂肪瘤": 0.01, "梭形细胞脂肪瘤": 0.01,
                          "非典型梭形细胞脂肪瘤": 0.01, "多形性脂肪瘤": 0.01, "冬眠瘤": 0.01}
    word_probb5zhifangliubing = {"脂肪瘤病": 0.01, "神经脂肪瘤病": 0.01}
    word_probb5zhifangrouliu = {"脂肪肉瘤": 0.01, "高分化脂肪肉瘤": 0.01, "去分化脂肪肉瘤": 0.01, "粘液脂肪肉瘤": 0.01, "多形性脂肪肉瘤": 0.01,
                             "粘液性脂肪肉瘤": 0.01}
    word_probb5jinmoyan = {"结节性筋膜炎": 0.01, "增殖性筋膜炎": 0.01, "缺血性筋膜炎": 0.01}
    word_probb5jiyan = {"增殖性肌炎": 0.01, "骨化性肌炎": 0.01}
    word_probb5xianweiliu = {"纤维瘤": 0.01, "弹性纤维瘤": 0.01, "弹力纤维瘤": 0.01, "韧带样型纤维瘤": 0.01, "腱鞘纤维瘤": 0.01, "腱膜纤维瘤": 0.01,
                          "钙化性腱膜纤维瘤": 0.01, "细胞血管纤维瘤": 0.01, "血管纤维瘤": 0.01, "孤立性纤维瘤": 0.01}
    word_probb5xianweiliubing = {"纤维瘤病": 0.01, "青少年玻璃样纤维瘤病": 0.01, "包涵体纤维瘤病": 0.01, "侵袭性纤维瘤病": 0.01, "韧带型纤维瘤病": 0.01,
                              "韧带样瘤型纤维瘤病": 0.01, "韧带样型纤维瘤病": 0.01, "硬纤维瘤纤维瘤病": 0.01, "脂肪纤维瘤病": 0.01}
    word_probb5chengxianweixibaoliu = {"肌成纤维细胞瘤": 0.01, "促结缔组织增生的成纤维细胞瘤": 0.01, "血管肌成纤维细胞瘤": 0.01, "巨细胞成纤维细胞瘤": 0.01}
    word_probb5xianweirouliu = {"纤维肉瘤": 0.01, "隆突皮肤纤维肉瘤": 0.01, "低级别肌肉成纤维肉瘤": 0.01, "粘液炎性纤维母细胞肉瘤": 0.01,
                             "粘液纤维肉瘤": 0.01, "硬化性上皮样纤维肉瘤": 0.01}
    word_probb5juxibaoliu = {"巨细胞瘤": 0.01, "腱鞘巨细胞瘤": 0.01}
    word_probb5xueguanliu = {"血管瘤": 0.01, "滑膜血管瘤": 0.01, "肌内血管瘤": 0.01, "动静脉畸形/血管瘤": 0.01, "动静脉血管瘤": 0.01,
                          "动静脉畸形瘤": 0.01, "静脉性血管瘤": 0.01, "吻合性血管瘤": 0.01, "上皮样血管瘤": 0.01, "簇状血管瘤": 0.01}
    word_probb5linbaguanliu = {"淋巴管瘤": 0.01, "淋巴管瘤病": 0.01}
    word_probb5xueguanneipiliu = {"卡波西样血管内皮瘤": 0.01, "网状血管内皮瘤": 0.01, "乳头状淋巴内血管内皮瘤": 0.01, "复合性血管内皮瘤": 0.01,
                               "假性肌源性血管内皮瘤": 0.01, "上皮样血管内皮瘤": 0.01}
    word_probb5jiwaipixibaoliu = {"肌外皮细胞瘤": 0.01, "肌纤维瘤": 0.01}
    word_probb5pinghuajiliu = {"平滑肌瘤": 0.01, " EB病毒相关性平滑肌肿瘤": 0.01}
    word_probb5pinghuajirouliu = {"平滑肌肉瘤": 0.01, "炎症性平滑肌肉瘤": 0.01}
    word_probb5hengwenjirouliu = {"横纹肌肉瘤": 0.01, "胚胎性横纹肌肉瘤": 0.01, "泡状横纹肌肉瘤": 0.01, "多形性横纹肌肉瘤": 0.01,
                               "梭形细胞/硬化性横纹肌肉瘤": 0.01, "硬化性横纹肌肉瘤": 0.01, "梭形细胞横纹肌肉瘤": 0.01}
    word_probb5yanxing = {"炎症": 0.01, "炎性": 0.01, "慢性化脓性炎": 0.01}
    word_probb5rouyazhong = {"肉芽肿": 0.01, "肉芽肿性炎": 0.01, "异物伴肉芽肿": 0.01, "异物肉芽肿": 0.01, "异物性肉芽肿": 0.01}
    word_probb5daoguan = {'导管内瘤':0.01,'导管内乳头状肿瘤':0.01}
    word_probb5daoguan = {'导管内瘤': 0.01, '导管内乳头状肿瘤': 0.01}
    word_probb5xianbing = {'瘤样增生':0.01,'增生结节':0.01}
    for icgy5 in range(len(segmentsc5)):
       if segmentsc5[icgy5] in word_probb5xianbing.keys():
           segmentsc5[icgy5] = '腺病'
       if segmentsc5[icgy5] in word_probb5daoguan.keys():
           segmentsc5[icgy5] = '导管内瘤'
       if segmentsc5[icgy5] in word_probb5zhifangliu.keys():
           segmentsc5[icgy5] = '脂肪瘤'
       if segmentsc5[icgy5] in word_probb5zhifangliubing.keys():
           segmentsc5[icgy5] = '脂肪瘤病'
       if segmentsc5[icgy5] in word_probb5zhifangrouliu.keys():
           segmentsc5[icgy5] = '脂肪肉瘤'
       if segmentsc5[icgy5] in word_probb5jinmoyan.keys():
         segmentsc5[icgy5] = '筋膜炎'
       if segmentsc5[icgy5] in word_probb5jiyan.keys():
         segmentsc5[icgy5] = '肌炎'
       if segmentsc5[icgy5] in word_probb5xianweiliu.keys():
        segmentsc5[icgy5] = '纤维瘤'
       if segmentsc5[icgy5] in word_probb5xianweiliubing.keys():
         segmentsc5[icgy5] = '纤维瘤病'
       if segmentsc5[icgy5] in word_probb5chengxianweixibaoliu.keys():
        segmentsc5[icgy5] = '成纤维细胞瘤'
       if segmentsc5[icgy5] in word_probb5xianweirouliu.keys():
         segmentsc5[icgy5] = '纤维肉瘤'
       if segmentsc5[icgy5] in word_probb5juxibaoliu.keys():
         segmentsc5[icgy5] = '巨细胞瘤'
       if segmentsc5[icgy5] in word_probb5xueguanliu.keys():
         segmentsc5[icgy5] = '血管瘤'
       if segmentsc5[icgy5] in word_probb5linbaguanliu.keys():
         segmentsc5[icgy5] = '淋巴管瘤'
       if segmentsc5[icgy5] in word_probb5xueguanneipiliu.keys():
         segmentsc5[icgy5] = '血管内皮瘤'
       if segmentsc5[icgy5] in word_probb5jiwaipixibaoliu.keys():
        segmentsc5[icgy5] = '肌外皮细胞瘤'
       if segmentsc5[icgy5] in word_probb5pinghuajiliu.keys():
         segmentsc5[icgy5] = '平滑肌瘤'
       if segmentsc5[icgy5] in word_probb5pinghuajirouliu.keys():
        segmentsc5[icgy5] = '平滑肌肉瘤'
       if segmentsc5[icgy5] in word_probb5hengwenjirouliu.keys():
         segmentsc5[icgy5] = '横纹肌肉瘤'
       if segmentsc5[icgy5] in word_probb5yanxing.keys():
           segmentsc5[icgy5] = '炎性'
       if segmentsc5[icgy5] in word_probb5rouyazhong.keys():
          segmentsc5[icgy5] = '肉芽肿'
       if segmentsc5[icgy5] =="BI-RADS 4A":
            segmentsc5[icgy5] = "BI-RADS 4a"
       if segmentsc5[icgy5] =="BI-RADS 4 a":
            segmentsc5[icgy5] = "BI-RADS 4a"
       if segmentsc5[icgy5] =="BI-RADS 4B":
            segmentsc5[icgy5] = "BI-RADS 4b"
       if segmentsc5[icgy5] =="BI-RADS 4C":
            segmentsc5[icgy5] = "BI-RADS 4c"
       if segmentsc5[icgy5] =="4A":
            segmentsc5[icgy5] = "BI-RADS 4a"
       if segmentsc5[icgy5] =="4B":
            segmentsc5[icgy5] = "BI-RADS 4b"
       if segmentsc5[icgy5] =="4C":
            segmentsc5[icgy5] = "BI-RADS 4c"
       if segmentsc5[icgy5] =="4a":
            segmentsc5[icgy5] = "BI-RADS 4a"
       if segmentsc5[icgy5] =="4b":
            segmentsc5[icgy5] = "BI-RADS 4b"
       if segmentsc5[icgy5] =="4c":
            segmentsc5[icgy5] = "BI-RADS 4c"



    # lencldivc5 = int(len(segmentsc5) / 2)
    # icldivc5 = 1
    # while (1):
    #  if lencldivc5 == 0:
    #      break
    #
    #  elif segmentsc5bf[2 * icldivc5 - 2] == '无效语句':
    #      segmentsc3.append('无效语句')
    #      segmentsc3.append(segmentsc5bf[2 * icldivc5 - 1])
    #      icldivc5 += 1
    #      if icldivc5 > lencldivc5:
    #          break
    #
    #  elif segmentsc5bf[2 * icldivc5 - 2] in word_probbingliwulinangxing.keys():
    #      segmentsc3.append('囊性')
    #      segmentsc3.append(segmentsc5[2 * icldivc5 - 1])
    #      icldivc5 += 1
    #      if icldivc5 > lencldivc5:
    #          break
    #  else:
    #      segmentsc3.append('实性')
    #      segmentsc3.append(segmentsc5[2 * icldivc5 - 1])
    #      icldivc5 += 1
    #      if icldivc5 > lencldivc5:
    #          break


    lencldivc5 = int(len(segmentsc5) / 2)
    icldivc5 = 1
    while (1):
     if lencldivc5 == 0:
         break
     elif segmentsc5bf[2 * icldivc5 - 2] in word_probliangxing.keys():
         segmentsc4.append('良性')
         segmentsc4.append(segmentsc5bf[2 * icldivc5 - 1])
         icldivc5 += 1
         if icldivc5 > lencldivc5:
             break
     elif segmentsc5bf[2 * icldivc5 - 2] in word_probexing.keys():
         segmentsc4.append('恶性')
         segmentsc4.append(segmentsc5bf[2 * icldivc5 - 1])
         icldivc5 += 1
         if icldivc5 > lencldivc5:
             break
     elif segmentsc5bf[2 * icldivc5 - 2] in word_probliang_or_e.keys():
         segmentsc4.append('良性或恶性待定')
         segmentsc4.append(segmentsc5bf[2 * icldivc5 - 1])
         icldivc5 += 1
         if icldivc5 > lencldivc5:
             break
     else:
        segmentsc4.append('无效语句')
        segmentsc4.append(segmentsc5bf[2 * icldivc5 - 1])
        icldivc5 += 1
        if icldivc5 > lencldivc5:
            break

    word_probc4liangxing = {"良性": 0.01, "良": 0.01}
    word_probc4exing = {"恶性": 0.01, "恶": 0.01}
    for icgy4 in range(len(segmentsc4)):
     if segmentsc4[icgy4] in word_probc4liangxing.keys():
         segmentsc4[icgy4] = '良性'
     if segmentsc4[icgy4] in word_probc4exing.keys():
         segmentsc4[icgy4] = '恶性'
