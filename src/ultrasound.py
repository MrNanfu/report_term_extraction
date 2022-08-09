# -*- coding:utf-8 -*-
#有一些demo只在pathological那边做了，比如否定词的处理，超声这边没加，主要否定词也是主要出现在病理那边，后续应该加上
from pathological import word_probbinglicebie,word_probbinglibuwei,word_probbingliwuli,word_probchaoshengwuli,word_probbingliwulinangxing,word_probbingliliangexing,word_probchaoshengliangexing,word_probliangxing,word_probexing,word_probliang_or_e,word_probbinglibingli,word_probchaoshengcebie,word_probchaoshengbuwei,word_probchaoshengbingli,word_probexing_major,word_probliang_or_e_major,word_probliangxing_major,word_probliangxing_minor

from pathological import findsegments
def Merge(dict1, dict2, dict3, dict4):
    res = {**dict1, **dict2, **dict3, **dict4}
    return res
word_reliability = {"建议": 0.01, "鉴别": 0.01, "排除": 0.01, "待": 0.01, "需": 0.01, "进一步": 0.01}
word_prob_invalid = {'切缘': 0.01, '皮缘': 0.01, '新辅': 0.01, '化疗': 0.01, '副乳': 0.01}
word_probchaoshengall ={**word_probchaoshengbuwei, **word_probchaoshengwuli, **word_probchaoshengliangexing,**word_probchaoshengbingli,**word_prob_invalid}


def ultrasoundfuc(ultrasound_bodypart,ultrasound_report):
    global leninputchaosheng
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
        if segmentsc_merge[2*i] in word_probbinglicebie:
            segmentsc1.append(segmentsc_merge[2 * i])
            segmentsc1.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probbinglibuwei:
            segmentsc2.append(segmentsc_merge[2 * i])
            segmentsc2.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probbingliwuli:
            segmentsc3.append(segmentsc_merge[2 * i])
            segmentsc3.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probbingliliangexing:
            segmentsc4.append(segmentsc_merge[2 * i])
            segmentsc4.append(segmentsc_merge[2 * i + 1])
        if segmentsc_merge[2*i] in word_probbinglibingli:
            segmentsc5.append(segmentsc_merge[2 * i])
            segmentsc5.append(segmentsc_merge[2 * i + 1])

        if segmentsc_merge[2 * i] in word_prob_invalid:
            segmentsc5.append("无效语句")
            segmentsc5.append(0)


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

    word_prob_negative_word_all = {'排除': 0.01, '鉴别': 0.01, '不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01, '除外': 0.01,
                                   '未见': 0.01, '疑': 0.01}
    # 带未见的先注释掉 未见的那个句子里有时候会报错

    # word_prob_negative_word_all = {'排除': 0.01, '鉴别': 0.01, '不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01, '除外': 0.01}
    word_prob_negative_word1 = {'排除': 0.01, '鉴别': 0.01, '除外': 0.01, '未见': 0.01}
    # word_prob_negative_word1 = {'排除': 0.01, '鉴别': 0.01,'除外': 0.01,'未见': 0.01}
    # 和上面切面那个问题同理，都是利用最大匹配的算法，这里由于不除外不能除外虽然表达肯定意思，但是如果不把这些词放里，就会提取到除外这样的否定词
    word_prob_negative_word2 = {'不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01, '疑': 0.01}
    word_prob_comma = {'，': 0.01, '；': 0.01, '、': 0.01}  # 注意打字时候这里是中文标点
    word_prob_full_stop = {'。': 0.01}  # 中文句号
    # 就是通过表格数据找寻规律，比如出现排除这种词，它前面第一个逗号到后面第一个句号里的词可能都需要排除掉，具体看表格里不同医生的写法去总结共性，然后这里也可以以后用NLP

    segmentsc_negative_word_all = findsegments(input_str, word_prob_negative_word_all)
    segmentsc_negative_word1 = []
    segmentsc_negative_word2 = []
    for i in range(int(len(segmentsc_negative_word_all) / 2)):
        if segmentsc_negative_word_all[2 * i] in word_prob_negative_word1:
            segmentsc_negative_word1.append(segmentsc_negative_word_all[2 * i])
            segmentsc_negative_word1.append(segmentsc_negative_word_all[2 * i + 1])
        if segmentsc_negative_word_all[2 * i] in word_prob_negative_word2:
            segmentsc_negative_word2.append(segmentsc_negative_word_all[2 * i])
            segmentsc_negative_word2.append(segmentsc_negative_word_all[2 * i + 1])
    segmentsc_comma = findsegments(input_str, word_prob_comma)
    segmentsc_full_stop = findsegments(input_str, word_prob_full_stop)
    # print('segmentsb_negative_word,segmentsb_comma,segmentsb_full_stop为')
    # print(segmentsb_negative_word,segmentsb_comma,segmentsb_full_stop)
    if len(segmentsc_negative_word1) != 0:
        # 先按只有一个否定词来处理
        loc_negative_word = segmentsc_negative_word1[1]
        for i in range(int(len(segmentsc_full_stop) / 2)):
            if segmentsc_full_stop[2 * i + 1] > loc_negative_word:
                loc_full_stop = segmentsc_full_stop[2 * i + 1]
                break
        # print('句号位置为')
        # print(loc_full_stop)
        loc_comma = -1
        loc_full_stop = -1
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

        segmentsb5new = []

        for i in range(int(len(segmentsc5) / 2)):
            # print(loc_comma)
            # print(loc_full_stop)
            if segmentsc5[2 * i + 1] < loc_comma or segmentsc5[2 * i + 1] > loc_full_stop:
                segmentsb5new.append(segmentsc5[2 * i])
                segmentsb5new.append(segmentsc5[2 * i + 1])
        segmentsb5 = segmentsb5new
        # print('segmentsb5new为')
        # print(segmentsb5new)


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
    for icgy5 in range(len(segmentsc5)):
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
    lencldivc5 = int(len(segmentsc5) / 2)
    icldivc5 = 1
    while (1):
     if lencldivc5 == 0:
         break

     elif segmentsc5bf[2 * icldivc5 - 2] == '无效语句':
         segmentsc3.append('无效语句')
         segmentsc3.append(segmentsc5bf[2 * icldivc5 - 1])
         icldivc5 += 1
         if icldivc5 > lencldivc5:
             break

     elif segmentsc5bf[2 * icldivc5 - 2] in word_probbingliwulinangxing.keys():
         segmentsc3.append('囊性')
         segmentsc3.append(segmentsc5[2 * icldivc5 - 1])
         icldivc5 += 1
         if icldivc5 > lencldivc5:
             break
     else:
         segmentsc3.append('实性')
         segmentsc3.append(segmentsc5[2 * icldivc5 - 1])
         icldivc5 += 1
         if icldivc5 > lencldivc5:
             break


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
