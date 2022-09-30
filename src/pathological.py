# -*- coding:utf-8 -*-
# 定义需要的字典 word_probbinglicebie病理侧别字典、word_probbinglibuwei病理部位字典、word_probbingliwulinangxing病理物理性质囊性字典、
# word_probbingliliangexing 病理直接含有良恶性字样的字典、word_probliangxing良性字典（超声病理一样）、word_probexing恶性字典（超声病理一样）
# word_probbinglibingli病理报告的病理性质字典、word_probchaoshengcebie：超声的侧别字典、word_probchaoshengbuwei 超声的部位字典、
# word_probchaoshengwuli超声的物理性质字典、word_probchaoshengliangexin超声的良恶性字典

#侧别
word_probbinglicebie = {"左": 0.01, "右": 0.01, "左侧": 0.01, "右侧": 0.01}
word_probchaoshengcebie=word_probbinglicebie

#部位
word_probbinglibuwei={'左乳': 0.01,'右乳': 0.01,'双乳': 0.01,"左侧乳腺": 0.01,"右侧乳腺": 0.01,"双侧乳腺": 0.01,
                      "左侧乳房腺体": 0.01,"右侧乳房腺体": 0.01,"双侧乳房腺体": 0.01,"左侧乳头": 0.01,"右侧乳头": 0.01,
                      "左侧乳房": 0.01,"右侧乳房": 0.01,"双侧乳房": 0.01,
                      "切面": 0.01,"面": 0.01, "左":0.01}#因为出现过 左乳乳房腺体这种事情的存在 导致提取了 左乳 病理空白 然后是 乳房腺体 加病 ，所以删除了单独的乳头、乳腺这类词汇
word_probchaoshengbuwei =word_probbinglibuwei

#物理性质
word_probbingliwuli = {"囊性":0.01,"实性":0.01,"混合性":0.01,"囊实":0.01, "实质性":0.01}
word_probchaoshengwuli=word_probbingliwuli
#除了直接找实性囊性词汇外，还通过如下病理性质推断出囊性，当时说除了这些都算实性(不过这个词典也是第一次皮下肿块的需求书里的词典，后续乳腺任务目前没给出实性囊性词典)
word_probbingliwulinangxing = {"囊肿": 0.01, "表皮样囊肿": 0.01, "皮样囊肿": 0.01, "皮脂腺囊肿": 0.01, "滑膜囊肿": 0.01, "粘液囊肿": 0.01,
                               "甲状舌管囊肿": 0.01, "间皮囊肿": 0.01, "腱鞘囊肿": 0.01, "毛根鞘囊肿": 0.01, "外毛根鞘囊肿": 0.01, "毛鞘囊肿": 0.01,
                               "毛囊源性囊肿": 0.01, "气管源性良性囊肿": 0.01, "鳃裂囊肿": 0.01}

#良恶性
word_probbingliliangexing = {"良": 0.01, "良性": 0.01, "恶": 0.01, "恶性": 0.01, "交界": 0.01, "交界性": 0.01, }#其实这里是重复的 但是开始时候文档给的是都带性的 后来发现实际里有不带性的 也应该识别上加上的
word_probchaoshengliangexing =word_probbingliliangexing

#病理匹配结果可信度问题
word_reliability = {"建议": 0.01, "鉴别": 0.01, "排除": 0.01, "待": 0.01, "需": 0.01, "进一步": 0.01}

#除了直接找良性恶性词汇外，还通过如下病理性质推断出良性



#注意每次改完 记得往下面大字典里添加 因为之前有一段合并字典的代码 不知道怎么报错了，后来手动合并这个了
#病理报告的病理性质


#新的字典
#主要诊断里的恶性 良恶性均可 良性 以及次要诊断（都是良性）
word_probexing_major={"浸润性导管癌":0.01,"浸润性癌":0.01, "浸润癌":0.01, "浸润性乳腺癌":0.01,"导管原位癌":0.01,"原位癌":0.01,"恶性叶状肿瘤":0.01,"包裹性乳头状癌":0.01,"实性乳头状癌":0.01,"导管内乳头状癌":0.01, "化生性癌":0.01, "BI-RADS 4C":0.01,"BI-RADS 4c":0.01,"4c":0.01,"4C":0.01,"BI-RADS 5":0.01,"BI-RADS 6":0.01}
word_probliang_or_e_major={"肿瘤病变":0.01, "导管内乳头状病变":0.01, "纤维上皮性病变":0.01, "肿瘤性病变":0.01, "导管内乳头状肿瘤":0.01,"叶状肿瘤":0.01,"放射状瘢痕〈B3,不确定的潜在恶性病变）":0.01,"非典型导管增生":0.01,"非典型导管上皮增生":0.01, "导管上皮不典型增生":0.01, "导管上皮非典型增生":0.01, "平坦型上皮非典型增生":0.01,"平坦上皮非典型性":0.01,"导管上皮轻度非典型增生":0.01,"不典型增生":0.01,"导管上皮增生活跃":0.01, "非典型增生":0.01, "不典型导管增生":0.01, "导管上皮增生":0.01,"导管上皮增生稍活跃(B3,不确定的潜在恶性病变）":0.01,"上皮源性肿瘤":0.01,"BI-RADS 0": 0.01}
word_probliangxing_major={"普通型增生":0.01, "肉芽肿":0.01,"肉芽肿性炎":0.01, "硬化性腺病":0.01, "错构瘤":0.01, "导管内乳头状瘤":0.01, "导管内乳头状瘤炎性病变":0.01,"炎性":0.01,"炎症性改变":0.01,"炎症性":0.01,"炎症改变":0.01,"小叶性肉芽肿性乳腺炎":0.01,"小叶肉芽肿性乳腺炎":0.01,"肉芽肿性小叶炎":0.01,"肉芽肿性小叶性乳腺炎":0.01,"非特异性炎症性病变纤维上皮肿瘤":0.01, "梭形细胞病变":0.01, "非特异性炎症性病变":0.01, "纤维上皮性":0.01, "纤维上皮性肿瘤":0.01,"良性纤维上皮性肿瘤":0.01,"纤维腺瘤样增生":0.01,"纤维腺瘤":0.01,"纤维腺瘤改变":0.01,"幼年型纤维腺瘤":0.01,"良性叶状肿瘤":0.01,"泌乳性腺瘤":0.01,"管状腺瘤":0.01,"结节性泌乳性增生硬化性腺病":0.01, "结节性泌乳性增生":0.01, "错构瘤硬化性腺病":0.01, "复杂硬化性":0.01, "复杂性硬化性":0.01, "复杂硬化性病变":0.01, "表皮样囊肿":0.01, "复杂性硬化性病表皮样囊肿":0.01,"纤维囊性乳腺病":0.01,"纤维囊性变":0.01,"囊肿性病变":0.01, "积乳囊肿":0.01, "囊肿":0.01,"导管扩张症新辅助治疗后改变":0.01,"化疗后改变":0.01,"未见确切恶性肿瘤细胞":0.01,"未见肿瘤":0.01,"BI-RADS 1":0.01,"BI-RADS 2":0.01,"BI-RADS 3":0.01,'BI-RADSⅢ':0.01, "BI-RADS 4A":0.01,
                      "BI-RADS 4B":0.01,"BI-RADS 4a":0.01,"BI-RADS 4b":0.01,"4a":0.01,"4b":0.01, "4A":0.01,"4B":0.01}
word_probjiaojie_major={"交界性叶状肿瘤" : 0.01}
word_probliangxing_minor={"柱状细胞增生":0.01,"柱状细胞变":0.01,"导管上皮柱状细胞变":0.01,"柱状上皮化生腺病":0.01,"导管上皮普通型增生":0.01,"导管上皮呈普通型增生":0.01,"导管上皮呈筛状增生":0.01,"导管上皮呈旺炽性增生":0.01,"导管普通型增生":0.01,"筛孔状增生":0.01,"导管上皮轻度增生":0.01,"导管上皮增生脂肪组织坏死纤维胶原增生":0.01,"间质纤维增生":0.01,"间质胶原增生":0.01, "间质胶原纤维增生":0.01, "胶原纤维增生":0.01, "大汗腺化生":0.01, "假血管瘤样间质增生":0.01,"假血管瘤样间质增生大汗腺化生":0.01,"腺病":0.01}

# 语义字典
word_prob_yuyi = {"建议免疫组化":0.01, "免疫组化":0.01, "伴":0.01, "个别":0.01, "部分":0.01, "主体":0.01}


#整体恶性词典、整体良恶性均可词典、整体良性词典
word_probexing=word_probexing_major
word_probliang_or_e=word_probliang_or_e_major
word_probliangxing={**word_probliangxing_major, **word_probliangxing_minor}
word_probjiaojie = word_probjiaojie_major

#病理报告的病理性质，把形容超声的BIRADS也写在里面了，这样超声和病理公用一个词典，因为病理报告里本身也不会出现BIRADS词汇，所以没有影响
# word_probbinglibingli={"肿瘤病变":0.01,"浸润性导管癌":0.01,"浸润性癌":0.01,"导管原位癌":0.01,"原位癌":0.01,"恶性叶状肿瘤":0.01,"包裹性乳头状癌":0.01,"实性乳头状癌":0.01,"导管内乳头状癌":0.01,"BI-RADS 4C":0.01,"BI-RADS 4c":0.01,"4c":0.01,"4C":0.01,"BI-RADS 5":0.01,"BI-RADS 6":0.01,"导管内乳头状肿瘤":0.01,"叶状肿瘤":0.01,"放射状瘢痕〈B3,不确定的潜在恶性病变）":0.01,"非典型导管增生":0.01,"非典型导管上皮增生":0.01,"平坦型上皮非典型增生":0.01,"平坦上皮非典型性":0.01,"导管上皮轻度非典型增生":0.01,"不典型增生":0.01,"导管上皮增生活跃":0.01,"导管上皮增生稍活跃(B3,不确定的潜在恶性病变）":0.01,"BI-RADS 0": 0.01,"导管内乳头状瘤炎性病变":0.01,"炎性":0.01,"炎症性改变":0.01,"炎症性":0.01,"炎症改变":0.01,"小叶性肉芽肿性乳腺炎":0.01,"小叶肉芽肿性乳腺炎":0.01,"肉芽肿性小叶炎":0.01,"肉芽肿性炎":0.01,"肉芽肿性小叶性乳腺炎":0.01,"非特异性炎症性病变纤维上皮肿瘤":0.01,"纤维上皮性肿瘤":0.01,"良性纤维上皮性肿瘤":0.01,"纤维腺瘤样增生":0.01,"纤维腺瘤改变":0.01,"幼年型纤维腺瘤":0.01,"良性叶状肿瘤":0.01,"泌乳性腺瘤":0.01,"管状腺瘤":0.01,"结节性泌乳性增生硬化性腺病":0.01,"复杂硬化性病变":0.01,"复杂性硬化性病表皮样囊肿":0.01,"纤维囊性乳腺病":0.01,"纤维囊性变":0.01,"囊肿性病变":0.01,"导管扩张症新辅助治疗后改变":0.01,"化疗后改变":0.01,"未见确切恶性肿瘤细胞":0.01,"未见肿瘤":0.01,"BI-RADS 1":0.01,"BI-RADS 2":0.01,"BI-RADS 3":0.01,'BI-RADSⅢ':0.01, "BI-RADS 4A":0.01,
#                       "BI-RADS 4B":0.01,"BI-RADS 4a":0.01,"BI-RADS 4b":0.01,"4a":0.01,"4b":0.01, "4A":0.01,"4B":0.01,"柱状细胞增生":0.01,"柱状细胞变":0.01,"导管上皮柱状细胞变":0.01,"柱状上皮化生腺病":0.01,"导管上皮普通型增生":0.01,"导管上皮呈普通型增生":0.01,"导管上皮呈筛状增生":0.01,"导管上皮呈旺炽性增生":0.01,"导管普通型增生":0.01,"筛孔状增生":0.01,"导管上皮轻度增生":0.01,"导管上皮增生脂肪组织坏死纤维胶原增生":0.01,"间质纤维增生":0.01,"间质胶原纤维增生":0.01,"假血管瘤样间质增生大汗腺化生":0.01,"腺病":0.01}
word_probbinglibingli={**word_probexing, **word_probliang_or_e_major,**word_probliangxing, **word_probjiaojie}
word_probchaoshengbingli = word_probbinglibingli

## 无效语句词典
word_prob_invalid = {'切缘': 0.01, '皮缘': 0.01, '新辅': 0.01, '化疗': 0.01, '副乳': 0.01}

##原始语句病理对应良恶性的词典
b4_raw_dict = {}

# 接下来所有的12345分别对应着： 侧别1 部位2 物理性质3 良恶性4 病理性质5 病理结果匹配可信度问题6
#segments就是放这些找到的片段的列表，b是病理，c是超声，如segmentsb1就是病理侧别，segmentsc2就是超声部位
def findsegments(input, word_prob):#最大匹配的那个函数
    max_len = max(len(w) for w in word_prob.keys())
    i = 0
    j = i + max_len
    segments = []
    while True:
        if input[i:j] in word_prob.keys():
            if j >= len(input):
                segments.append(input[i:j])
                segments.append(i)
                break
            segments.append(input[i:j])
            segments.append(i)
            i = j
            j = i + max_len
        else:
            j -= 1
            if j == i:
                i = i + 1
                j = i + max_len
            if i == len(input) + 1:
                break
    return segments



#合并成一个大字典，用这个字典进去一起找，找完之后再区分开是部位还是性质等等
word_probbingliall={**word_probbinglibuwei,**word_probbingliwuli,**word_probbingliliangexing,**word_probbinglibingli, **word_prob_invalid}
# print(word_probbingliall)

## 切缘、皮缘等词的出现，定义为无效病理语句


def pathologicalfuc(pathological_bodypart, pathological_report):#给parse输入的四个参数里的前两个有关病理的参数赋值给该函数
    global leninputbingli #输入字符串长度
    input_str = pathological_report
    leninputbingli = len(input_str)

    #用大字典找到的列表
    global segmentsb_merge
    segmentsb_merge = []
    segmentsb_merge = findsegments(input_str,word_probbingliall)
    reliability = findsegments(input_str, word_reliability)
    invalid_b = findsegments(input_str, word_prob_invalid)


    # print('segmentsb_merge为')
    # print(segmentsb_merge)

    # global segmentsb1
    # segmentsb1=[]
    # segmentsb1=findsegments(input_str, word_probbinglicebie)

    global segmentsb1,segmentsb2,segmentsb3,segmentsb4,segmentsb5, segmentsb6, segmentsb_yuyi
    #1代表侧别、2代表部位、3代表物理性质、4代表良恶
    segmentsb1=[]#注意这里又加了b1，虽然这次任务用不上
    segmentsb2=[]
    segmentsb3=[]
    segmentsb3_raw = []
    segmentsb4=[]
    segmentsb4_raw=[]
    segmentsb5=[]

    segmentsb6=[]
    segmentsb_yuyi = [] # 存放语义信息

    # 提取语义关键词
    segmentsb_yuyi = findsegments(input_str, word_prob_yuyi)


    #根据来源的字典分别将其放入每个列表
    for i in range(int(len(segmentsb_merge)/2)):
        if segmentsb_merge[2*i] in word_probbinglicebie:
            segmentsb1.append(segmentsb_merge[2*i])
            segmentsb1.append(segmentsb_merge[2*i+1])
        if segmentsb_merge[2*i] in word_probbinglibuwei:
            segmentsb2.append(segmentsb_merge[2*i])
            segmentsb2.append(segmentsb_merge[2*i+1])
        if segmentsb_merge[2*i] in word_probbingliwuli:
            segmentsb3_raw.append(segmentsb_merge[2*i])
            segmentsb3_raw.append(segmentsb_merge[2*i+1])
        if segmentsb_merge[2*i] in word_probbingliliangexing:
            segmentsb4_raw.append(segmentsb_merge[2*i])
            segmentsb4_raw.append(segmentsb_merge[2*i+1])
        if segmentsb_merge[2*i] in word_probbinglibingli:
            segmentsb5.append(segmentsb_merge[2*i])
            segmentsb5.append(segmentsb_merge[2*i+1])

        if segmentsb_merge[2 * i] in word_prob_invalid:
            segmentsb5.append("无效语句")
            segmentsb5.append(0)


    if int(len(reliability)) != 0:
        for i in range(int(len(reliability)/2)):
            for j in range(int(len(segmentsb2)/2)):
                if( j < int(len(segmentsb2)/2) - 1):
                    if segmentsb2[2 * j + 1] < reliability[2 * i + 1] < segmentsb2[2 * j + 3]:
                        segmentsb6.append("匹配结果可信度低")
                    else:
                        segmentsb6.append("匹配结果可信度高")
                else :
                    if segmentsb2[2 * j + 1] < reliability[2 * i + 1]:
                        segmentsb6.append("匹配结果可信度低")
                    else:
                        segmentsb6.append("匹配结果可信度高")

    elif int(len(reliability)) == 0:
        if int(len(segmentsb2) / 2) != 0:
            for j in range(int(len(segmentsb2) / 2)):
                segmentsb6.append("匹配结果可信度高")
        else:
                segmentsb6.append("匹配结果可信度高")

    # print('segmentsb5为')
    # print(segmentsb5)



    word_probb1zuo = {"左": 0.01, "左侧": 0.01}
    word_probb1you = {"右": 0.01, "右侧": 0.01}
    for ibgy1 in range(len(segmentsb1)):
            if segmentsb1[ibgy1] in word_probb1zuo.keys():
                segmentsb1[ibgy1] = '左'
            if segmentsb1[ibgy1] in word_probb1you.keys():
                segmentsb1[ibgy1] = '右'

    #我们输入四项，病理检查的器官，病理报告，超声检查的器官，超声的报告，之前医生说报告里如果没出现器官的话，就用病理检查时候那个器官填里面，这里基本用不上，但用一个标志位segmentsb2temp做一下
    global segmentsb2temp
    segmentsb2temp=0
    if len(segmentsb2) == 0:#没有就把给到的参考部位信息放里，标志位置1，也给一个默认的位置信息（因为后续代码按都带着位置信息来的，即按整体数目是偶数来操作的）
        segmentsb2.append(pathological_bodypart)
        segmentsb2.append(0)
        segmentsb2temp = 1

    #这里很多归一化也是最开始需求书里的 这里用不上 但是下面那些乳腺归一化是新加的 是能用上的
    word_probc2zhoubu = {"肘": 0.01} #########
    word_probb2shouwanbu = {"手": 0.02, "腕": 0.02, "指": 0.02, "虎口": 0.02} ###########
    word_probb2xibu = {"膝": 0.01, "腘窝": 0.01}
    word_probb2zuhuaibu = {"足": 0.01, "踝": 0.01, "趾": 0.01}
    word_probb2xiongbi = {"胸": 0.01}
    # word_probb2xiongbi = {"胸": 0.01, "乳腺": 0.01} 胸的完全改了 乳腺不能算胸
    word_probb2fubi = {"腹": 0.01, "剑突": 0.01, "脐": 0.01}
    word_probb2beibu = {"背": 0.01, "腰": 0.01, "胸背": 0.01}
    # word_probb2jianbu = {"肩": 0.01, "腋": 0.01}
    word_probb2jianbu = {"肩": 0.01}
    word_probb2kuanbu = {"腹股沟": 0.01, "髋": 0.01}
    word_probb2tunbu = {"骶": 0.01, "臀": 0.01, "肛": 0.01}
    word_probb2yanmianbu = {"颊": 0.01, "面": 0.01, "眼": 0.01, "眉": 0.01, "耳": 0.01, "颌": 0.01, "颏": 0.01}
    word_probb2toubu = {"顶": 0.01, "额": 0.01, "枕": 0.01, "颞": 0.01, "头皮": 0.01}
    # word_probb2jingbu = {"颈": 0.01, "锁骨上": 0.01}
    word_probb2jingbu = {"颈": 0.01}
    word_probb2yewosuogu = {"腋窝": 0.01, "锁骨": 0.01}
    word_probb2yewosuoguleft={"左侧腋窝": 0.01,"左侧锁骨": 0.01,"左腋窝": 0.01,"左锁骨": 0.01}
    word_probb2yewosuoguright = {"右侧腋窝": 0.01,"右侧锁骨": 0.01,"右腋窝": 0.01,"右锁骨": 0.01}
    word_probb2yewosuogudouble= {"双侧腋窝": 0.01,"双侧锁骨": 0.01,"双腋窝": 0.01,"双锁骨": 0.01}
    dict_word_probb2 = {'0.01': "肘部", '0.02': "手腕部"}

    #归一化操作，把部位信息在上面字典里找，翻译成标准的部位信息
    for ibgy2 in range(len(segmentsb2)):
        # segmentsb2[ibgy2] = dict_word_probb2[str(word_probc2zhoubu[segmentsb2[ibgy2]])]
            if segmentsb2[ibgy2] in word_probc2zhoubu.keys():
                segmentsb2[ibgy2] = '肘部'
            if segmentsb2[ibgy2] in word_probb2shouwanbu.keys():
                segmentsb2[ibgy2] = '手腕部'
            if segmentsb2[ibgy2] in word_probb2xibu.keys():
                segmentsb2[ibgy2] = '膝部'
            if segmentsb2[ibgy2] in word_probb2zuhuaibu.keys():
                segmentsb2[ibgy2] = '足踝部'
            if segmentsb2[ibgy2] in word_probb2xiongbi.keys():
                segmentsb2[ibgy2] = '胸壁'
            if segmentsb2[ibgy2] in word_probb2fubi.keys():
                segmentsb2[ibgy2] = '腹壁'
            if segmentsb2[ibgy2] in word_probb2beibu.keys():
                segmentsb2[ibgy2] = '背部'
            if segmentsb2[ibgy2] in word_probb2jianbu.keys():
                segmentsb2[ibgy2] = '肩部'
            if segmentsb2[ibgy2] in word_probb2kuanbu.keys():
                segmentsb2[ibgy2] = '髋部'
            if segmentsb2[ibgy2] in word_probb2tunbu.keys():
                segmentsb2[ibgy2] = '臀部'
            if segmentsb2[ibgy2] in word_probb2yanmianbu.keys():
                segmentsb2[ibgy2] = '颜面部'
            if segmentsb2[ibgy2] in word_probb2toubu.keys():
                segmentsb2[ibgy2] = '头部'
            if segmentsb2[ibgy2] in word_probb2jingbu.keys():
                segmentsb2[ibgy2] = '颈部'
            if segmentsb2[ibgy2]=='乳房腺体':
                segmentsb2[ibgy2] = '乳腺'
            if segmentsb2[ibgy2]=='右侧乳房腺体':
                segmentsb2[ibgy2] = '右侧乳腺'
            if segmentsb2[ibgy2]=='左侧乳房腺体':
                segmentsb2[ibgy2] = '左侧乳腺'
            if segmentsb2[ibgy2]=='双侧乳房腺体':
                segmentsb2[ibgy2] = '双侧乳腺'
            if segmentsb2[ibgy2]=='右侧副乳腺肿物':
                segmentsb2[ibgy2] = '右侧副乳'
            if segmentsb2[ibgy2]=='左侧副乳腺肿物':
                segmentsb2[ibgy2] = '左侧副乳'
            if segmentsb2[ibgy2]=='双侧副乳腺肿物':
                segmentsb2[ibgy2] = '双侧副乳'
            if segmentsb2[ibgy2] in word_probb2yewosuogu.keys():
                segmentsb2[ibgy2] = '腋窝及锁骨区'
            if segmentsb2[ibgy2] in word_probb2yewosuoguleft.keys():
                segmentsb2[ibgy2] = '左侧腋窝及锁骨区'
            if segmentsb2[ibgy2] in word_probb2yewosuoguright.keys():
                segmentsb2[ibgy2] = '右侧腋窝及锁骨区'
            if segmentsb2[ibgy2] in word_probb2yewosuogudouble.keys():
                segmentsb2[ibgy2] = '双侧腋窝及锁骨区'
            # if segmentsb2[ibgy2]=='切面':
            #     del segmentsb2[ibgy2]
    # print(segmentsb2)


    #这段代码为了解决出现如 切面这种词汇时候，因为部位词典里有面，而提取到 面这个字，先不用管它
    #解决的思想就是，利用了最大匹配算法时候有长的我们不会提短的，所以把切面也放进词典，这样会提到切面，不会提到面，然后再删去切面就好
    visit = [0] * len(segmentsb2)
    # print(visit)
    for idx, value in enumerate(segmentsb2):
        if value == '切面':
            visit[idx] = 1
            visit[idx+1]=1
    new_list = []
    for idx in range(len(visit)):
        if not visit[idx]:
            new_list.append(segmentsb2[idx])
    segmentsb2 = new_list



    #否定词 出现否定词的时候 它形容的那些病理性质需要排除掉或者取反，下面列出了一些需要排除的

    word_prob_negative_word_all={'排除':0.01,'鉴别':0.01,'不完全除外':0.01,'不能除外':0.01,'不除外':0.01,'除外':0.01,'未见': 0.01}

    #word_prob_negative_word_all = {'排除': 0.01, '鉴别': 0.01, '不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01, '除外': 0.01}
    word_prob_negative_word1 = {'排除': 0.01, '鉴别': 0.01,'除外': 0.01, '未见': 0.01}
    # word_prob_negative_word1 = {'排除': 0.01, '鉴别': 0.01,'除外': 0.01,'未见': 0.01}
    #和上面切面那个问题同理，都是利用最大匹配的算法，这里由于不除外不能除外虽然表达肯定意思，但是如果不把这些词放里，就会提取到除外这样的否定词
    word_prob_negative_word2 = {'不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01 ,'考虑': 0.01, '疑' : 0.01}
    word_prob_comma={'，':0.01,'；':0.01,'、':0.01}#注意打字时候这里是中文标点
    word_prob_full_stop={'。':0.01}#中文句号

    #就是通过表格数据找寻规律，比如出现排除这种词，它前面第一个逗号到后面第一个句号里的词可能都需要排除掉，具体看表格里不同医生的写法去总结共性，然后这里也可以以后用NLP

    segmentsb_negative_word_all = findsegments(input_str, word_prob_negative_word_all)
    segmentsb_negative_word1=[]
    segmentsb_negative_word2=[]
    for i in range(int(len(segmentsb_negative_word_all)/2)):
        if segmentsb_negative_word_all[2*i] in word_prob_negative_word1:
            segmentsb_negative_word1.append(segmentsb_negative_word_all[2*i])
            segmentsb_negative_word1.append(segmentsb_negative_word_all[2*i+1])
        if segmentsb_negative_word_all[2*i] in word_prob_negative_word2:
            segmentsb_negative_word2.append(segmentsb_negative_word_all[2*i])
            segmentsb_negative_word2.append(segmentsb_negative_word_all[2*i+1])
    segmentsb_comma=findsegments(input_str, word_prob_comma)
    segmentsb_full_stop=findsegments(input_str, word_prob_full_stop)
    # print('segmentsb_negative_word,segmentsb_comma,segmentsb_full_stop为')
    # print(segmentsb_negative_word,segmentsb_comma,segmentsb_full_stop)
    if len(segmentsb_negative_word_all)!=0:
        loc_comma = 0
        loc_full_stop = 0
        #先按只有一个否定词来处理
        loc_negative_word=segmentsb_negative_word_all[1]
        for i in range(int(len(segmentsb_full_stop)/2)):
            if segmentsb_full_stop[2*i+1]>loc_negative_word:
                loc_full_stop=segmentsb_full_stop[2*i+1]
                break
        # print('句号位置为')
        # print(loc_full_stop)

        for j in range(int(len(segmentsb_comma)/2)):
            if j<int(len(segmentsb_comma)/2-1):
                if (segmentsb_comma[2*j+1]<loc_negative_word) and (segmentsb_comma[2*j+3]>loc_negative_word):
                    loc_comma=segmentsb_comma[2*j+1]
                    break
            if j==int(len(segmentsb_comma)/2-1):
                if (segmentsb_comma[2*j+1]<loc_negative_word):
                    loc_comma =segmentsb_comma[2*j+1]
                    break
        # print('逗号位置为')
        # print(loc_comma)
        #还没写 2*j+3超出去的情况

        if len(invalid_b)==0:
            segmentsb5new = []
            for i in range(int(len(segmentsb5) / 2)):
                if segmentsb5[2 * i + 1] < loc_comma or segmentsb5[2 * i + 1] > loc_full_stop:
                    segmentsb5new.append(segmentsb5[2 * i])
                    segmentsb5new.append(segmentsb5[2 * i + 1])
            segmentsb5 = segmentsb5new

        # print('segmentsb5new为')
        # print(segmentsb5new)

        ## 良恶性也要依据否定词进行修改
        def remove_liange(segmentsb4_raw, segmentsb_negative_word1):
            segmentsb4_after=[]
            if int(len(segmentsb_negative_word1)) != 0:
                for i in range(int(len(segmentsb4_raw)/2)):
                    for j in range(int(len(segmentsb_negative_word1)/2)):
                        if -5< segmentsb4_raw[2*i+1]-segmentsb_negative_word1[2*j+1] < 5:
                            segmentsb4_after.append(segmentsb4_raw[2 * i ])
                            segmentsb4_after.append(segmentsb4_raw[2 * i + 1])
            return segmentsb4_after
        segmentsb4_raw = remove_liange(segmentsb4_raw, segmentsb_negative_word1)


    global segmentsb5bf
    segmentsb5bf = segmentsb5.copy()  # 归一化前的segmentsb5 用来后续判断良恶性和物理性质，因为判断病理性质对应的良恶性和物理性质的字典是按照病理性质归一化前的名称来写的，所以必须保存一个没有归一化的病理信息

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
    word_probb5xianweirouliu = {"纤维肉瘤": 0.01, "隆突皮肤纤维肉瘤": 0.01, "低级别肌肉成纤维肉瘤": 0.01, "粘液炎性纤维母细胞肉瘤": 0.01, "粘液纤维肉瘤": 0.01,
                                "硬化性上皮样纤维肉瘤": 0.01}
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
    for ibgy5 in range(len(segmentsb5)):
        if segmentsb5[ibgy5] in word_probb5zhifangliu.keys():
            segmentsb5[ibgy5] = '脂肪瘤'
        if segmentsb5[ibgy5] in word_probb5zhifangliubing.keys():
            segmentsb5[ibgy5] = '脂肪瘤病'
        if segmentsb5[ibgy5] in word_probb5zhifangrouliu.keys():
            segmentsb5[ibgy5] = '脂肪肉瘤'
        if segmentsb5[ibgy5] in word_probb5jinmoyan.keys():
            segmentsb5[ibgy5] = '筋膜炎'
        if segmentsb5[ibgy5] in word_probb5jiyan.keys():
            segmentsb5[ibgy5] = '肌炎'
        if segmentsb5[ibgy5] in word_probb5xianweiliu.keys():
            segmentsb5[ibgy5] = '纤维瘤'
        if segmentsb5[ibgy5] in word_probb5xianweiliubing.keys():
            segmentsb5[ibgy5] = '纤维瘤病'
        if segmentsb5[ibgy5] in word_probb5chengxianweixibaoliu.keys():
            segmentsb5[ibgy5] = '成纤维细胞瘤'
        if segmentsb5[ibgy5] in word_probb5xianweirouliu.keys():
            segmentsb5[ibgy5] = '纤维肉瘤'
        if segmentsb5[ibgy5] in word_probb5juxibaoliu.keys():
            segmentsb5[ibgy5] = '巨细胞瘤'
        if segmentsb5[ibgy5] in word_probb5xueguanliu.keys():
            segmentsb5[ibgy5] = '血管瘤'
        if segmentsb5[ibgy5] in word_probb5linbaguanliu.keys():
            segmentsb5[ibgy5] = '淋巴管瘤'
        if segmentsb5[ibgy5] in word_probb5xueguanneipiliu.keys():
            segmentsb5[ibgy5] = '血管内皮瘤'
        if segmentsb5[ibgy5] in word_probb5jiwaipixibaoliu.keys():
            segmentsb5[ibgy5] = '肌外皮细胞瘤'
        if segmentsb5[ibgy5] in word_probb5pinghuajiliu.keys():
            segmentsb5[ibgy5] = '平滑肌瘤'
        if segmentsb5[ibgy5] in word_probb5pinghuajirouliu.keys():
            segmentsb5[ibgy5] = '平滑肌肉瘤'
        if segmentsb5[ibgy5] in word_probb5hengwenjirouliu.keys():
            segmentsb5[ibgy5] = '横纹肌肉瘤'
        if segmentsb5[ibgy5] in word_probb5yanxing.keys():
            segmentsb5[ibgy5] = '炎性'
        if segmentsb5[ibgy5] in word_probb5rouyazhong.keys():
            segmentsb5[ibgy5] = '肉芽肿'



    #根据病理性质所对应的实性囊性来给出实性囊性信息
    lencldivb5 = int(len(segmentsb5) / 2)
    icldivb5 = 1
    while (1):
        if lencldivb5 == 0:
            break

        elif segmentsb5bf[2 * icldivb5 - 2] == '无效语句':
            segmentsb3.append('无效语句')
            segmentsb3.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break

        elif segmentsb5bf[2 * icldivb5 - 2] in word_probbingliwulinangxing.keys():#注意这段里有时候角标是5有时候是3，因为是根据5病理信息列表里的某一项的信息，来在3实性囊性里添加
            segmentsb3.append('囊性')
            segmentsb3.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break

        else:
            segmentsb3.append('实性')
            segmentsb3.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break



    #根据病理性质所对应的良恶性来给出良恶性信息
    lencldivb5 = int(len(segmentsb5) / 2)
    icldivb5 = 1
    while (1):
        if lencldivb5 == 0:
            break
        if len(segmentsb4_raw) != 0:

            segmentsb4_raw_temp = segmentsb4_raw
            for j in range(int(len(segmentsb4_raw_temp)/2)):
                if -15<= segmentsb4_raw_temp[2 * j + 1] - segmentsb5bf[2 * icldivb5 - 1] <= 15 :
                    segmentsb4.append(segmentsb4_raw_temp[2 * j])
                    segmentsb4.append(segmentsb4_raw_temp[2 * j + 1])
                    b4_raw_dict[segmentsb5bf[2 * icldivb5 -2]] = segmentsb4_raw_temp[2 * j]

                    segmentsb4_raw.reverse()
                    segmentsb4_raw.pop()
                    segmentsb4_raw.pop()

            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break

        elif segmentsb5bf[2 * icldivb5 - 2] in word_probliangxing.keys():
            segmentsb4.append('良性')
            segmentsb4.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break
        elif segmentsb5bf[2 * icldivb5 - 2] in word_probexing.keys():
            segmentsb4.append('恶性')
            segmentsb4.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break
        elif segmentsb5bf[2 * icldivb5 - 2] in word_probliang_or_e.keys():
            segmentsb4.append('良性或恶性待定')
            segmentsb4.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break
        else:
            segmentsb4.append('无效语句')
            segmentsb4.append(segmentsb5bf[2 * icldivb5 - 1])
            icldivb5 += 1
            if icldivb5 > lencldivb5:
                break




    word_probb4liangxing = {"良性": 0.01, "良": 0.01}
    word_probb4exing = {"恶性": 0.01, "恶": 0.01}
    for ibgy4 in range(len(segmentsb4)):
        if segmentsb4[ibgy4] in word_probb4liangxing.keys():
            segmentsb4[ibgy4] = '良性'
        if segmentsb4[ibgy4] in word_probb4exing.keys():
            segmentsb4[ibgy4] = '恶性'


