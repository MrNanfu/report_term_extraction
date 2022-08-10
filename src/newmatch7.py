# coding:utf-8
import copy

from pathological import word_probbinglicebie, word_probbinglibuwei, word_probbingliwuli, word_probchaoshengwuli, \
    word_probbingliwulinangxing, word_probbingliliangexing, word_probchaoshengliangexing, word_probliangxing, \
    word_probexing, word_probliang_or_e, word_probbinglibingli, word_probchaoshengcebie, word_probchaoshengbuwei, \
    word_probchaoshengbingli, word_probexing_major, word_probliang_or_e_major, word_probliangxing_major, \
    word_probliangxing_minor

# 顺序 侧别1 部位2 bp 物理性质3 pp 良恶性4 bm 病理性质5
from pathological import pathologicalfuc
from ultrasound import ultrasoundfuc


# 主函数
def parser(pathological_bodypart, pathological_report, ultrasound_bodypart, ultrasound_report):
    lenstringb = len(pathological_report)
    lenstringc = len(ultrasound_report)
    pathologicalfuc(pathological_bodypart, pathological_report)
    ultrasoundfuc(ultrasound_bodypart, ultrasound_report)
    from pathological import segmentsb1, segmentsb2, segmentsb3, segmentsb4, segmentsb5, segmentsb6, segmentsb_yuyi, leninputbingli, segmentsb2temp, \
        segmentsb5bf  # 引入之前两个函数中得到的列表信息
    from ultrasound import segmentsc1, segmentsc2, segmentsc3, segmentsc4, segmentsc5, segmentsc6, leninputchaosheng, segmentsc2temp
    global segmentsb1, segmentsb2, segmentsb3, segmentsb4, segmentsb5, segmentsc1, segmentsc2, segmentsc3, segmentsc4, segmentsc5, leninputbingli, leninputchaosheng, segmentsb5bf

    #生成一个整体列表的形式
    def fuc1(segments2, segments3, segments4, segments5, segments6, lenstring):
        segmentsall = []
        # 整体大列表 的第一层列表数和部位数目相同
        lenalldiv = int(len(segments2) / 2)  # 带着位置信息，注意除以二
        for ialldiv in range(lenalldiv):
            segmentsall.append([])
        # 整体大列表 的第二层列表数为5
        for ialldiv in range(lenalldiv):
            for j in range(6):
                segmentsall[ialldiv].append([])
        # 填入“部位分割标志”字样
        for ialldiv in range(lenalldiv):
            (segmentsall[ialldiv])[0].append('部位分割标志')
        # 填入 部位
        for ialldiv in range(lenalldiv):  # 注意这里不除二,前面除过了
            (segmentsall[ialldiv])[1].append(segments2[2 * ialldiv])
            (segmentsall[ialldiv])[1].append(segments2[int(2 * ialldiv + 1)])

        # 建立一个填两两部位之间的位置都有哪些的列表
        lenalldiv = int(len(segments2) / 2)
        segmentsnum = []
        for inum in range(lenalldiv):
            segmentsnum.append([])
        # 开始填入位置信息
        idiv = 0
        while (1):
            if lenalldiv == 0:
                break
            if idiv < lenalldiv - 1:
                segmentsnum[idiv].extend(range(segments2[2 * idiv + 1], segments2[2 * idiv + 3]))
                idiv = idiv + 1
            if idiv == lenalldiv - 1:
                segmentsnum[idiv].extend(range(segments2[2 * idiv + 1], lenstring))
                break

        # 把病理项、良性恶性、实性囊性放到列表里，如果某个病理信息的位置，在两个器官位置的中间，那它应该放入前一个器官所在的列表
        for j5 in range(int(len(segments5) / 2)):
            for jnum in range(len(segmentsnum)):
                if segments5[2 * j5 + 1] in segmentsnum[jnum] :
                    (segmentsall[jnum])[4].append(segments5[2 * j5])
                    (segmentsall[jnum])[4].append(segments5[2 * j5 + 1])

                elif segments5[2 * j5] == "无效语句":    ##无效语句的情况
                    (segmentsall[jnum])[4].append(segments5[2 * j5])
                    (segmentsall[jnum])[4].append(segments5[2 * j5 + 1])


        for j4 in range(int(len(segments4) / 2)):
            for jnum in range(len(segmentsnum)):
                if segments4[2 * j4 + 1] in segmentsnum[jnum]:
                    (segmentsall[jnum])[3].append(segments4[2 * j4])
                    (segmentsall[jnum])[3].append(segments4[2 * j4 + 1])

                elif segments4[2 * j4] == "无效语句":  ##无效语句的情况
                    (segmentsall[jnum])[3].append(segments4[2 * j4])
                    (segmentsall[jnum])[3].append(segments4[2 * j4 + 1])



        for j3 in range(int(len(segments3) / 2)):
            for jnum in range(len(segmentsnum)):
                if segments3[2 * j3 + 1] in segmentsnum[jnum]:
                    (segmentsall[jnum])[2].append(segments3[2 * j3])
                    (segmentsall[jnum])[2].append(segments3[2 * j3 + 1])

                elif segments3[2 * j3] == "无效语句":
                    (segmentsall[jnum])[2].append(segments3[2 * j3])
                    (segmentsall[jnum])[2].append(segments3[2 * j3 + 1])


        # for jnum in range(len(segmentsnum)):
        #     (segmentsall[jnum])[5].append(segments6[jnum])



        return (segmentsall, segmentsnum)

    segmentsball, segmentsbnum = fuc1(segmentsb2, segmentsb3, segmentsb4, segmentsb5, segmentsb6, lenstringb)
    segmentscall, segmentscnum = fuc1(segmentsc2, segmentsc3, segmentsc4, segmentsc5, segmentsc6, lenstringc)

    # 对于segmentsb_yuyi，利用segmentsbnum的位置信息按照部位进行分割操作
    segmentsb_yuyi_sep = []
    lenalldiv = int(len(segmentsb2) / 2)  # 带着位置信息，注意除以二
    for ialldiv in range(lenalldiv):
        segmentsb_yuyi_sep.append([])
    for j6 in range((int)(len(segmentsb_yuyi) / 2)):
        for jnum in range(len(segmentsbnum)):
            if segmentsb_yuyi[2 * j6 + 1] in segmentsbnum[jnum]:
                (segmentsb_yuyi_sep[jnum]).append(segmentsb_yuyi[2 * j6])
                (segmentsb_yuyi_sep[jnum]).append(segmentsb_yuyi[2 * j6 + 1])

    # 对于出现双乳，语义segments6也需要展开,使其与segmentsall的索引保持一致
    def unfold_yuyi(segmentsb_yuyi, segments2, string1):
        for i in range(int(len(segments2) / 2)):
            if segments2[2 * i] == string1:
                r = segmentsb_yuyi[i].copy()
                segmentsb_yuyi.insert(i + 1, r)

    segmentsb_yuyi = unfold_yuyi(segmentsb_yuyi, segmentsb2, '双侧乳腺')
    segmentsb_yuyi = unfold_yuyi(segmentsb_yuyi, segmentsb2, '双乳')
    segmentsb_yuyi = unfold_yuyi(segmentsb_yuyi, segmentsb2, '双侧乳房')
    segmentsb_yuyi = unfold_yuyi(segmentsb_yuyi, segmentsb2, '双侧乳头')
    segmentsb_yuyi = unfold_yuyi(segmentsb_yuyi, segmentsb2, '双侧腋窝及锁骨区')

    # 出现双乳，需要展开，下面的字典需要根据数据里出现过什么不断补充，而且得注意需求是调整超声 病理 还是都调整
    def unfold(segmentsall, segments2, string1, string2, string3):
        lenalldiv = int(len(segments2) / 2)
        i = 0
        while (1):
            if ((segmentsall[i])[1])[0] == string1:
                sleft = (segmentsall[i])[1].copy()
                sleft[0] = string2
                sright = (segmentsall[i])[1].copy()
                sright[0] = string3
                m = (segmentsall[i]).copy()
                m[1] = sleft
                n = (segmentsall[i]).copy()
                n[1] = sright
                left = m
                right = n
                segmentsall[i] = left
                segmentsall.insert(i + 1, right)
                lenalldiv += 1
            i = i + 1
            if i == lenalldiv:
                break
        return segmentsall

    segmentscall = unfold(segmentscall, segmentsc2, '双侧乳腺', '左侧乳腺', '右侧乳腺')
    segmentscall = unfold(segmentscall, segmentsc2, '双乳', '左乳', '右乳')
    segmentscall = unfold(segmentscall, segmentsc2, '双侧乳房', '左侧乳房', '右侧乳房')
    segmentscall = unfold(segmentscall, segmentsc2, '双侧乳头', '左侧乳头', '右侧乳头')
    segmentscall = unfold(segmentscall, segmentsc2, '双侧腋窝及锁骨区', '左侧腋窝及锁骨区', '右侧腋窝及锁骨区')

    segmentsball = unfold(segmentsball, segmentsb2, '双侧乳腺', '左侧乳腺', '右侧乳腺')
    segmentsball = unfold(segmentsball, segmentsb2, '双乳', '左乳', '右乳')
    segmentsball = unfold(segmentsball, segmentsb2, '双侧乳房', '左侧乳房', '右侧乳房')
    segmentsball = unfold(segmentsball, segmentsb2, '双侧乳头', '左侧乳头', '右侧乳头')
    segmentsball = unfold(segmentsball, segmentsb2, '双侧腋窝及锁骨区', '左侧腋窝及锁骨区', '右侧腋窝及锁骨区')  # 注意要填归一化后的，即不能让它检测双侧腋窝



    ## 输出segmentsall语句时，存在某些句子只有部位，因此需要进行删除。当时超声报告有时候会出现"左侧乳头深方导管局部扩张伴导管内异常回声：沉积物？"类似的语句，对于这样的不能删除，应该对其病理加上BI-RADS 6
    def remove(segmentstall, flg):
        segmentall_new = []
        if flg == 0:    # 病理报告的remove方法
            for j in range(int(len(segmentstall))):
                if len((segmentstall[j])[2]) != 0 :
                    segmentall_new.append((segmentstall[j]))
        elif flg == 1:  # 超声报告的remove方法
            for j in range(int(len(segmentstall))):
                if len((segmentstall[j])[4]) == 0 :
                    segmentstall[j][4].append('BI-RADS 6')
                    if j < len(segmentstall) - 1:
                        segmentstall[j][4].append(segmentstall[j + 1][1][1] - 1)    # 由于BI-RADS 6没有出现在语句中，假设其位置为下一个句子的钱一个位置
                    else:
                        segmentstall[j][4].append(segmentstall[j][1][1] + 1)    # 句子为最后一个句子时，假设其位置为当前句首加一
                segmentall_new.append((segmentstall[j]))
        return segmentall_new

    segmentsball = remove(segmentsball, 0);
    segmentscall = remove(segmentscall, 1)

    # 去掉位置信息
    def new(segmentsall):
        # 整体的嵌套大列表
        segmentsnew = []
        # 整体大列表 的第一层列表数和部位数目相同
        lennewdiv = int(len(segmentsall))
        for inewdiv in range(lennewdiv):
            segmentsnew.append([])
        # 整体大列表 的第二层列表数为6
        for inewdiv in range(lennewdiv):
            for j in range(5):
                segmentsnew[inewdiv].append([])
        for inewdiv in range(lennewdiv):
            (segmentsnew[inewdiv])[0].append('部位分割标志')

        for inewdiv in range(lennewdiv):
            segmentsnew[inewdiv].append((segmentsall[inewdiv])[5])


        for i in range(len(segmentsall)):
            for j in range(1, 5):
                lendiv = int(len((segmentsall[i])[j]) / 2)
                for k in range(lendiv):
                    (segmentsnew[i])[j].append(((segmentsall[i])[j])[2 * k])

        return (segmentsnew)

    segmentsbnew = new(segmentsball)
    segmentscnew = new(segmentscall)
    # print('\n')
    # print('提取到的原始病理信息为')
    # print(segmentsbnew)
    # print('提取到的原始超声信息为')
    # print(segmentscnew)

    # 拷贝一个作为输出，这里是提取到的原始病理信息和提取到的原始超声信息
    segmentsbnew_copy_step1 = copy.deepcopy(segmentsbnew)
    segmentscnew_copy_step1 = copy.deepcopy(segmentscnew)

    # 越严重的病对应越高的数值，用于后续归一化
    def get_key(dict, value):
        return [k for k, v in dict.items() if v == value]

    word_prob3 = {"无病变": 0.01, "混合性": 0.02, "囊性": 0.03, "囊实": 0.04, "实性": 0.05}
    # 注意实性囊性这里，医生之前没有给出严重的排名，我是根据网上查的写了一个，乳腺任务这里不用实性囊性，但接下来其他部位的时候需要医生确定下他们之间的排序
    word_prob4 = {"良性": 0.01, "良性或恶性待定": 0.015, "恶性": 0.02}

    # 多个实性囊性出现时进行归一化
    def normalization3(segments):
        mark = 0
        for i in range(len(segments)):
            if segments[i] == '无效语句':
                mark = 1
        if mark :
            new_s = ['无效语句']
            return new_s
        else:
            valueside = 0.01
            for i in range(len(segments)):
                valuesidetemp = word_prob3[segments[i]]
                if valuesidetemp > valueside:
                    valueside = valuesidetemp
            segments = get_key(word_prob3, valueside)
            return segments

    for i in range(len(segmentsbnew)):
        segmentsbnew[i][2] = normalization3(segmentsbnew[i][2])
    for i in range(len(segmentscnew)):
        segmentscnew[i][2] = normalization3(segmentscnew[i][2])

    # 多个良性恶性出现时进行归一化
    def normalization4(segments):
        mark = 0
        for i in range(len(segments)):
            if segments[i] == '无效语句':
                mark = 1
        if mark :
            new_s = ['无效语句']
            return new_s
        else:
            valueside = 0.01
            for i in range(len(segments)):
                if segments[i] in word_prob4:
                    valuesidetemp = word_prob4[segments[i]]
                    if valuesidetemp > valueside:
                        valueside = valuesidetemp
            segments = get_key(word_prob4, valueside)
            return segments

    for i in range(len(segmentsbnew)):
        segmentsbnew[i][3] = normalization4(segmentsbnew[i][3])
    for i in range(len(segmentscnew)):
        segmentscnew[i][3] = normalization4(segmentscnew[i][3])

    # #主要诊断次要诊断需要进行筛选，注意逻辑图中主要次要病分类有问题，后来医生将所有的良恶性待定（绿色的）都放入主要诊断里了，我下面的四个字典也是根据调整后的进行构建的
    # #找到对应的数值
    # def normalization_major_minor_temp(segments):
    #     segments_temp=[]
    #     if len(segments)!=0:
    #         for i in range(len(segments)):
    #             if segments[i] in word_probexing_major:
    #                 segments_temp.append(0.04)
    #
    #             elif segments[i] in word_probliang_or_e_major:
    #                 segments_temp.append(0.03)
    #
    #             elif segments[i] in word_probliangxing_major:
    #                 segments_temp.append(0.02)
    #
    #             elif segments[i] in word_probliangxing_minor:
    #                 segments_temp.append(0.01)
    #
    #             else:
    #                 break
    #     return segments_temp
    #
    # #找到其中最大的数值，以及其对应的字典是哪个
    # def get_temp_dictionary(segments_temp):
    #     valuetemp = 0.01
    #     for i in range(len(segments_temp)):
    #         if segments_temp[i]>valuetemp:
    #             valuetemp = segments_temp[i]
    #
    #     if valuetemp==0.04:
    #         return word_probexing_major
    #     if valuetemp==0.03:
    #         return word_probliang_or_e_major
    #     if valuetemp==0.02:
    #         return word_probliangxing_major
    #     if valuetemp==0.01:
    #         return word_probliangxing_minor
    #
    # #归一化
    # def normalization_major_minor(segments):
    #     segments_temp = normalization_major_minor_temp(segments)
    #     valuetemp_dictionary = get_temp_dictionary(segments_temp)
    #     segments_normalization_major_minor=[]
    #     for i in range(len(segments)):
    #         if segments[i] in valuetemp_dictionary.keys():
    #             segments_normalization_major_minor.append(segments[i])
    #             break
    #     return segments_normalization_major_minor

    # 寻找某个语义词后最近的病理, flg = 0代表寻找的病理为良恶未知， flg = 1代表寻找的病理为良性
    def find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, str_yuyi, flg):
        related_seg_idx = -1
        segments_pos = segmentsball[idx][4]
        # print(segments_pos)
        segmentsb_yuyi_pos = segmentsb_yuyi_sep[idx]
        pos_yuyi = -1
        for i in range(int(len(segmentsb_yuyi_pos) / 2)):
            if segmentsb_yuyi_pos[2 * i] == str_yuyi:
                pos_yuyi = segmentsb_yuyi_pos[2 * i + 1]
        if pos_yuyi == -1:
            return -1
        for i in range(int(len(segments_pos) / 2)):
            if flg == 0:
                if segments_pos[2 * i] in word_probliang_or_e_major or segments_pos[2 * i] in word_probliangxing_major:
                    related_seg_idx += 1
                    if segments_pos[2 * i + 1] > pos_yuyi:
                        # related_seg_idx = i
                        return related_seg_idx
            elif flg == 1:
                if segments_pos[2 * i] in word_probliangxing_major:
                    related_seg_idx += 1
                    if segments_pos[2 * i + 1] > pos_yuyi:
                        # related_seg_idx = i
                        return related_seg_idx
        return -1

    #找到其中最大的数值，以及其对应的字典是哪个
    def get_temp_dictionary(segments_temp):
        valuetemp = 0.01
        for i in range(len(segments_temp)):
            if segments_temp[i]>valuetemp:
                valuetemp = segments_temp[i]

        if valuetemp==0.04:
            return word_probexing_major
        if valuetemp==0.03:
            return word_probliang_or_e_major
        if valuetemp==0.02:
            return word_probliangxing_major
        if valuetemp==0.01:
            return word_probliangxing_minor

    #归一化
    def normalization_major_minor(segments, idx):
        mark = 0
        for i in range(len(segments)):
            if segments[i] == '无效语句':
                mark = 1
        if mark :
            new_s = ['无效语句']
            return new_s
        else:
            flg_mianyi = 0
            cnt_list = [0, 0, 0, 0]  # 主要诊断的恶性、良恶待定、良性、次要诊断的良性的计数数组
            segments_normalization_major_minor = []
            if len(segments) != 0:
                for i in range(len(segments)):
                    if segments[i] in word_probexing_major:
                        cnt_list[0] += 1

                    elif segments[i] in word_probliang_or_e_major:
                        cnt_list[1] += 1

                    elif segments[i] in word_probliangxing_major:
                        cnt_list[2] += 1

                    elif segments[i] in word_probliangxing_minor:
                        cnt_list[3] += 1

                    else:
                        break
            if cnt_list[0] + cnt_list[1] + cnt_list[2] == 0:  # 没有主要诊断
                if cnt_list[3] != 0:
                    for i in range(len(segments)):
                        if segments[i] in word_probliangxing_minor:
                            segments_normalization_major_minor.append(segments[i])
                            break
            else:  # 存在主要诊断，下面良恶性未定和良性的病理的筛选需要结合语义
                if cnt_list[0] != 0:  # 存在恶性输出所有恶性
                    for i in range(len(segments)):
                        if segments[i] in word_probexing_major:
                            segments_normalization_major_minor.append(segments[i])
                else:  # 不存在恶性
                    if '免疫组化' in segmentsb_yuyi_sep[idx]:  # 存在免疫组化关键词时，提取最近的后面一个病理
                        idx_mianyi = -1
                        for i in range(int(len(segmentsb_yuyi_sep[idx]) / 2)):
                            if segmentsb_yuyi_sep[idx][2 * i] == '免疫组化':
                                idx_mianyi = segmentsb_yuyi_sep[idx][2 * i + 1]
                                break
                        flg = 0
                        for i in range(len(segments)):
                            for j in range(int(len(segmentsball[idx][4]) / 2)):
                                if segments[i] == segmentsball[idx][4][2 * j]:
                                    if segmentsball[idx][4][2 * j + 1] > idx_mianyi:
                                        segments_normalization_major_minor.append(segments[i])
                                        flg_mianyi = 1
                                        break
                            if flg_mianyi:
                                break
                    if flg_mianyi == 1:  # 有‘免疫组化’语义字段，但是其后没有病理，因此需要特判
                        return segments_normalization_major_minor
                    if cnt_list[1] != 0:  # 不存在恶性但是存在良恶未知
                        if cnt_list[1] == 1:  # 只存在一个良恶未知
                            for i in range(len(segments)):
                                if segments[i] in word_probliang_or_e_major:
                                    segments_normalization_major_minor.append(segments[i])
                                    return segments_normalization_major_minor
                        else:  # 存在多个良恶未知，需要用语义信息去判断
                            prio_list = [0 for _ in range(cnt_list[1])]
                            # 首先对于在部分语义后面的病理的优先级进行扣分
                            idx_ban = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '伴', 0)
                            idx_gebie = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '个别', 0)
                            idx_bufen = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '部分', 0)
                            if idx_ban != -1: prio_list[idx_ban] -= 1
                            if idx_gebie != -1: prio_list[idx_gebie] -= 1
                            if idx_bufen != -1: prio_list[idx_bufen] -= 1
                            # 然后对于出现在主体近后的病理加分
                            idx_zhuti = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '主体', 0)
                            if idx_zhuti != -1: prio_list[idx_zhuti] += 1
                            # 查看优先级最大的病理
                            max_val = max(prio_list)
                            min_val = min(prio_list)
                            if max_val == 0 and min_val == 0:  # 对于没有出现上下文语义信息的，选取最后一个良恶性未知病理即可
                                for i in range(len(segments), -1, -1):
                                    if segments[i] in word_probliang_or_e_major:
                                        segments_normalization_major_minor.append(segments[i])
                            else:  # 对于出现了语义信息的，选取优先级最高的良恶性病理输出
                                print(prio_list)
                                max_idx = prio_list.index(max(prio_list))
                                idx = -1
                                for i in range(len(segments)):
                                    if (segments[i] in word_probliang_or_e_major):
                                        idx += 1
                                        if idx == max_idx:
                                            segments_normalization_major_minor.append(segments[i])
                    elif cnt_list[2] != 0:
                        if cnt_list[2] == 1:  # 只存在一个良性
                            for i in range(len(segments)):
                                if segments[i] in word_probliangxing_major:
                                    segments_normalization_major_minor.append(segments[i])
                                    return segments_normalization_major_minor
                        else:  # 存在多个良性
                            prio_list = [0 for _ in range(cnt_list[2])]
                            # 首先对于在部分语义后面的病理的优先级进行扣分
                            idx_ban = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '伴', 1)
                            idx_gebie = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '个别', 1)
                            idx_bufen = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '部分', 1)
                            if idx_ban != -1: prio_list[idx_ban] -= 1
                            if idx_gebie != -1: prio_list[idx_gebie] -= 1
                            if idx_bufen != -1: prio_list[idx_bufen] -= 1
                            # 然后对于出现在主体近后的病理加分
                            idx_zhuti = find_related_bl_by_yuyi(segments, segmentsb_yuyi_sep, idx, '主体', 1)
                            if idx_zhuti != -1: prio_list[idx_zhuti] += 1
                            # 查看优先级最大的病理
                            max_val = max(prio_list)
                            min_val = min(prio_list)
                            if max_val == 0 and min_val == 0:  # 对于没有出现上下文语义信息的，选取最后一个良恶性未知病理即可
                                for i in range(len(segments)):
                                    if segments[i] == '导管内乳头状瘤':
                                        segments_normalization_major_minor.append(segments[i])
                                        return segments_normalization_major_minor
                                for i in range(len(segments) - 1, -1, -1):
                                    # print(i)
                                    if segments[i] in word_probliangxing_major:
                                        segments_normalization_major_minor.append(segments[i])
                            else:  # 对于出现了语义信息的，选取优先级最高的良恶性病理输出
                                max_idx = prio_list.index(max(prio_list))
                                idx = -1
                                for i in range(len(segments)):
                                    if (segments[i] in word_probliangxing_major):
                                        idx += 1
                                        if idx == max_idx:
                                            segments_normalization_major_minor.append(segments[i])
            
            return segments_normalization_major_minor

    for i in range(len(segmentsbnew)):
        segmentsbnew[i][4] = normalization_major_minor(segmentsbnew[i][4], i)
        # 医生给的字典里只有病理性质，所以不知道超声要不要也这样提取，先不加，加上后可能需要调整代码
        # segmentscnew[i][4] = normalization_major_minor(segmentscnew[i][4])

    # 拷贝一个作为输出，这里是根据主要次要诊断筛选后的信息
    segmentsbnew_copy_step2 = copy.deepcopy(segmentsbnew)
    segmentscnew_copy_step2 = copy.deepcopy(segmentscnew)

    # # 病理主次要诊断筛选后再利用筛选后的病理进行良恶性归一化
    # for i in range(len(segmentsbnew)):
    #     segmentsbnew[i][3]=normalization4(segmentsbnew[i][3])
    # for i in range(len(segmentscnew)):
    #     segmentscnew[i][3]=normalization4(segmentscnew[i][3])

    def get_key(dict, value):
        return [k for k, v in dict.items() if v == value]

    word_prob3 = {"无病变": 0.01, "混合性": 0.02, "囊性": 0.03, "囊实": 0.04, "实性": 0.05}
    word_prob4 = {"良性": 0.01, "良性或恶性待定": 0.015, "恶性": 0.02}

    # 合并左乳 合并右乳，即如左乳腺、左乳房、左乳头的信息都合并到一起作为左乳
    def combine(word_prob2left, word_prob2right, segmentsnew):

        segments3left = []
        segments4left = []
        segments5left = []
        segments6left = []
        segments3right = []
        segments4right = []
        segments5right = []
        segments6right = []

        # print('segmentsnew为')
        # print(segmentsnew)
        for i in range(len(segmentsnew)):
            if ((segmentsnew[i])[1])[0] in word_prob2left:
                segments6left.extend((segmentsnew[i])[5])
                segments5left.extend((segmentsnew[i])[4])
                segments4left.extend((segmentsnew[i])[3])
                segments3left.extend((segmentsnew[i])[2])


            if ((segmentsnew[i])[1])[0] in word_prob2right:
                segments6right.extend((segmentsnew[i])[5])
                segments5right.extend((segmentsnew[i])[4])
                segments4right.extend((segmentsnew[i])[3])
                segments3right.extend((segmentsnew[i])[2])

        return segments3left, segments3right, segments4left, segments4right, segments5left, segments5right, segments6left, segments6right

    segmentsb3left_breast, segmentsb3right_breast, segmentsb4left_breast, segmentsb4right_breast, segmentsb5left_breast, segmentsb5right_breast, segmentsb6left_breast, segmentsb6right_breast = combine(
        {"左乳": 0.01, "左侧乳头": 0.01, "左侧乳房": 0.01, "左侧乳腺": 0.01,"左侧副乳": 0.01, "左":0.01 }, {"右乳": 0.01, "右侧乳头": 0.01, "右侧乳房": 0.01, "右侧乳腺": 0.01, "右侧副乳": 0.01, "右":0.01 },
        segmentsbnew)
    segmentsb3left_axilla, segmentsb3right_axilla, segmentsb4left_axilla, segmentsb4right_axilla, segmentsb5left_axilla, segmentsb5right_axilla, segmentsb6left_axilla, segmentsb6right_axilla  = combine(
        {"左侧腋窝": 0.01, "左侧锁骨": 0.01, "左腋窝": 0.01, "左锁骨": 0.01, "左侧腋窝及锁骨区": 0.01},
        {"右侧腋窝": 0.01, "右侧锁骨": 0.01, "右腋窝": 0.01, "右锁骨": 0.01, "右侧腋窝及锁骨区": 0.01}, segmentsbnew)
    segmentsc3left_breast, segmentsc3right_breast, segmentsc4left_breast, segmentsc4right_breast, segmentsc5left_breast, segmentsc5right_breast, segmentsc6left_breast, segmentsc6right_breast= combine(
        {"左乳": 0.01, "左侧乳头": 0.01, "左侧乳房": 0.01, "左侧乳腺": 0.01,"左侧副乳": 0.01 , "左":0.01 }, {"右乳": 0.01, "右侧乳头": 0.01, "右侧乳房": 0.01, "右侧乳腺": 0.01, "右侧副乳": 0.01, "右":0.01 },
        segmentscnew)
    segmentsc3left_axilla, segmentsc3right_axilla, segmentsc4left_axilla, segmentsc4right_axilla, segmentsc5left_axilla, segmentsc5right_axilla, segmentsc6left_axilla, segmentsc6right_axilla = combine(
        {"左侧腋窝": 0.01, "左侧锁骨": 0.01, "左腋窝": 0.01, "左锁骨": 0.01, "左侧腋窝及锁骨区": 0.01},
        {"右侧腋窝": 0.01, "右侧锁骨": 0.01, "右腋窝": 0.01, "右锁骨": 0.01, "右侧腋窝及锁骨区": 0.01}, segmentscnew)

    # 不是左乳右乳都要输出，要看病理报告提到了哪侧，属于之前都准备好左乳右乳信息了，这里哪侧不为空，输出哪侧
    def findnotnone(segmentsnew):
        segmentsnew_temp = []
        for i in range(len(segmentsnew)):
            if ((segmentsnew[i])[1])[0] in {"左乳": 0.01, "左侧乳头": 0.01, "左侧乳房": 0.01, "左侧乳腺": 0.01,  "左侧副乳": 0.01, "左":0.01}:
                segmentsnew_temp.append(0)
            if ((segmentsnew[i])[1])[0] in {"右乳": 0.01, "右侧乳头": 0.01, "右侧乳房": 0.01, "右侧乳腺": 0.01,  "右侧副乳": 0.01, "右":0.01 }:
                segmentsnew_temp.append(1)
            if ((segmentsnew[i])[1])[0] in {"左侧腋窝": 0.01, "左侧锁骨": 0.01, "左腋窝": 0.01, "左锁骨": 0.01, "左侧腋窝及锁骨区": 0.01}:
                segmentsnew_temp.append(2)
            if ((segmentsnew[i])[1])[0] in {"右侧腋窝": 0.01, "右侧锁骨": 0.01, "右腋窝": 0.01, "右锁骨": 0.01, "右侧腋窝及锁骨区": 0.01}:
                segmentsnew_temp.append(3)
        return segmentsnew_temp

    segmentsbnew_temp = findnotnone(segmentsbnew)
    segmentscnew_temp = findnotnone(segmentscnew)

    segmentsbfinal = [[['部位分割标志'], ['左乳'], segmentsb3left_breast, segmentsb4left_breast, segmentsb5left_breast,segmentsb6left_breast ],
                      [['部位分割标志'], ['右乳'], segmentsb3right_breast, segmentsb4right_breast, segmentsb5right_breast, segmentsb6right_breast],
                      [['部位分割标志'], ['左侧腋窝及锁骨区'], segmentsb3left_axilla, segmentsb4left_axilla, segmentsb5left_axilla, segmentsb6left_axilla],
                      [['部位分割标志'], ['右侧腋窝及锁骨区'], segmentsb3right_axilla, segmentsb4right_axilla,segmentsb5right_axilla,segmentsb6right_axilla]]

    segmentscfinal = [[['部位分割标志'], ['左乳'], segmentsc3left_breast, segmentsc4left_breast, segmentsc5left_breast, segmentsc6left_breast],
                      [['部位分割标志'], ['右乳'], segmentsc3right_breast, segmentsc4right_breast, segmentsc5right_breast, segmentsc6right_breast],
                      [['部位分割标志'], ['左侧腋窝及锁骨区'], segmentsc3left_axilla, segmentsc4left_axilla, segmentsc5left_axilla, segmentsc6left_axilla],
                      [['部位分割标志'], ['右侧腋窝及锁骨区'], segmentsc3right_axilla, segmentsc4right_axilla, segmentsc5right_axilla, segmentsc6right_axilla]]

    segmentsb3right_breast = normalization3(segmentsb3right_breast)
    segmentsc3right_breast = normalization3(segmentsc3right_breast)
    segmentsb3left_breast = normalization3(segmentsb3left_breast)
    segmentsc3left_breast = normalization3(segmentsc3left_breast)
    segmentsb3left_axilla = normalization3(segmentsb3left_axilla)
    segmentsb3right_axilla = normalization3(segmentsb3right_axilla)
    segmentsc3left_axilla = normalization3(segmentsc3left_axilla)
    segmentsc3right_axilla = normalization3(segmentsc3right_axilla)

    segmentsb4right_breast = normalization4(segmentsb4right_breast)
    segmentsc4right_breast = normalization4(segmentsc4right_breast)
    segmentsb4left_breast = normalization4(segmentsb4left_breast)
    segmentsc4left_breast = normalization4(segmentsc4left_breast)
    segmentsb4left_axilla = normalization4(segmentsb4left_axilla)
    segmentsb4right_axilla = normalization4(segmentsb4right_axilla)
    segmentsc4left_axilla = normalization4(segmentsc4left_axilla)
    segmentsc4right_axilla = normalization4(segmentsc4right_axilla)

    # 这个不删除 这个是有用的
    word_prob5 = {"BI-RADS 0": 0.005, "BI-RADS 1": 0.01, "BI-RADS 2": 0.02, "BI-RADS 3": 0.03, 'BI-RADSⅢ':0.03, "BI-RADS 4a": 0.041,
                  "BI-RADS 4b": 0.042, "BI-RADS 4c": 0.043, "BI-RADS 5": 0.05, "BI-RADS 6": 0.06}

    # 有时候超声报告里不全是BIRADS，偶尔因为过去的病史可以推断出具体的疾病，过去超声的逻辑是按BIRADS写的，包括它们之间归一化的比较，这里需要加一个区分开的函数，BIRADS和BIRADS之间归一化，不能混到一起
    def divide5(segments):
        segments_BIRADS = []
        segments_others = []
        for i in range(len(segments)):
            if segments[i] in word_prob5:
                segments_BIRADS.append(segments[i])
            else:
                segments_others.append(segments[i])
        return segments_BIRADS, segments_others

    # 超声的病理性质信息中BIRADS归一化函数
    def normalization5_BIRADS(segments):
        if int(len(segments))==0:
            return segments
        else:
            valueside = 0.01
            for i in range(len(segments)):
                valuesidetemp = word_prob5[segments[i]]
                if valuesidetemp > valueside:
                    valueside = valuesidetemp
            segments = get_key(word_prob5, valueside)
            if len(segments) > 0:
                return [segments[0]]
            return segments

    # 超声的病理性质信息整体归一化函数
    def normalization5c_all(segments):
        segments_BIRADS, segments_others = divide5(segments)
        segments_BIRADS = normalization5_BIRADS(segments_BIRADS)
        segments_BIRADS_copy = segments_BIRADS.copy()
        segments_BIRADS_copy.extend(segments_others)
        # print('segments_BIRADS_copy为')
        # print(segments_BIRADS_copy)
        segments = segments_BIRADS_copy
        return segments

    segmentsc5left_breast = normalization5c_all(segmentsc5left_breast)
    segmentsc5right_breast = normalization5c_all(segmentsc5right_breast)
    segmentsc5left_axilla = normalization5c_all(segmentsc5left_axilla)
    segmentsc5right_axilla = normalization5c_all(segmentsc5right_axilla)

    # 超声报告的良恶性需要以BIRADS为依据，因此在进行病理归一化后需要重新对良恶性进行归一化
    def normalization4c(segmentsc5_breast):
        segmentsc4 = []
        mark = 0
        for i in range(len(segmentsc5_breast)):
            if segmentsc5_breast[i] == '无效语句':
                mark += 1
        if mark == 1 and len(segmentsc5_breast) == mark:
            new_s = ['无效语句']
            return new_s
        else:
            for i in range(len(segmentsc5_breast)):
                if segmentsc5_breast[i] in word_prob5:
                    if segmentsc5_breast[i] in word_probliangxing:
                        segmentsc4.append('良性')
                    elif segmentsc5_breast[i] in word_probliang_or_e:
                        segmentsc4.append('良性或恶性待定')
                    elif segmentsc5_breast[i] in word_probexing:
                        segmentsc4.append('恶性')
            segmentsc4 = normalization4(segmentsc4)
        return segmentsc4

    segmentsc4left_breast = normalization4c(segmentsc5left_breast)
    segmentsc4right_breast = normalization4c(segmentsc5right_breast)
    segmentsc4left_axilla = normalization4c(segmentsc5left_axilla)
    segmentsc4right_axilla = normalization4c(segmentsc5right_axilla)

    def normalization5b(segmentsb4_breast,segmentsb5_breast):#这里是已经归一化的良恶性 和还未归一化的病理性质
        mark = 0
        for i in range(len(segmentsb5_breast)):
            if segmentsb5_breast[i] == '无效语句':
                mark = 1
        if mark :
            new_s = ['无效语句']
            return new_s
        else:
            segments = []
            if len(segmentsb4_breast) != 0:
                if len(segmentsb5_breast) != 0:
                    # 注意这里 良性或恶性待定 字符串要和前文写得保持一致 比如良恶性均可 就不会识别到
                    # 医生逻辑：有恶性输出所有恶性，不输出其它病理。没有恶性优先输出良恶未知，良性优先级最低。
                    # if segmentsb4_breast[0]=='恶性'or segmentsb4_breast[0]=='良性或恶性待定':
                    if segmentsb4_breast[0] == '恶性':  # 由于之前进行了normalization4归一化，这里的良恶性代表严重程度最高的良恶性
                        if len(segmentsb5_breast) != 0:
                            for i in range(len(segmentsb5_breast)):
                                if segmentsb5_breast[i] in word_probexing.keys():
                                    segments.append(segmentsb5_breast[i])
                                else: # 不在恶性字典中的，也需要进行输出（病理语句中详细说明了该病是恶性）
                                    segments.append(segmentsb5_breast[i])
                                # if segmentsb5_breast[i] in word_probliang_or_e.keys():
                                #     segments.append(segmentsb5_breast[i])
                                # if len(segments) == 0:  # 此情况为特殊情况，即出现了‘免疫组化’后的良性病理，它优先级比良恶未知病理还高
                                #     segments.append(segmentsb5_breast[i])
                    elif segmentsb4_breast[0] == '良性或恶性待定':  # 当良恶性归一化结果为良恶未知时，其病理可能是良恶性未知或者良性，优先输出良恶未知的病理
                        if len(segmentsb5_breast) != 0:
                            for i in range(len(segmentsb5_breast)):
                                if segmentsb5_breast[i] in word_probliang_or_e_major.keys():
                                    segments.append(segmentsb5_breast[i])
                                    break
                            if len(segments) == 0:
                                for i in range(len(segmentsb5_breast)):
                                    if segmentsb5_breast[i] in word_probliangxing.keys():
                                        segments.append(segmentsb5_breast[i])
                                        break

                    else:  # 良恶性归一化结果为良性时，输出任意一个良性病理即可 #存在某些情况，词典是良恶性不定，但是语句中表明是良性，此时便不方便进行查词典输出，可以直接输出原来的性质
                        for i in range(len(segmentsb5_breast)):
                            if segmentsb5_breast[i] not in word_probliangxing.keys() and segmentsb4_breast[i] == '良性':
                                segments.append(segmentsb5_breast[i])
                            elif segmentsb5_breast[i] in word_probliangxing.keys():
                                segments.append(segmentsb5_breast[i])
                                break
            return segments
    segmentsb5left_breast=normalization5b(segmentsb4left_breast,segmentsb5left_breast)
    segmentsb5right_breast = normalization5b(segmentsb4right_breast, segmentsb5right_breast)
    
    
    def normalization4b(segmentsb4_breast, segmentsb5_breast):  # 为了解决良恶性和病理不一致问题，这里需要根据病理来对良恶性重新进行归一化
        mark = 0
        for i in range(len(segmentsb5_breast)):
            if segmentsb5_breast[i] == '无效语句':
                mark = 1
        if mark :
            new_s = ['无效语句']
            return new_s
        else:
            segments = []
            if len(segmentsb4_breast) != 0 and len(segmentsb5_breast) != 0:
                if segmentsb4_breast[0] == '恶性':
                    # len_e = len(segmentsb5_breast)
                    len_e = 1  # 为了便于后面的match，对于多个恶性只输出一个即可
                    segments = ['恶性' for i in range(len_e)]
                else:
                    if segmentsb5_breast[0] in word_probliang_or_e_major:
                        if segmentsb4_breast[0] == '良性':  ## 虽然某些病理性质在词典中属于良恶性不定，但是如果语句中明确是良性了，则需要输出良性
                            segments = ['良性']
                        else:
                            segments = ['良性或恶性待定']
                    elif segmentsb5_breast[0] in word_probliangxing:
                        segments = ['良性']
            return segments

    segmentsb4left_breast = normalization4b(segmentsb4left_breast, segmentsb5left_breast)
    segmentsb4right_breast = normalization4b(segmentsb4right_breast, segmentsb5right_breast)

    def normalization6(segments6_breast):  # 这里是已经归一化的良恶性 和还未归一化的病理性质
        if len(segments6_breast) == 0:
            return segments6_breast
        else :
            return segments6_breast[0]


    segmentsb6left_breast=normalization6(segmentsb6left_breast)
    segmentsb6right_breast = normalization6(segmentsb6right_breast)
    segmentsc6left_breast=normalization6(segmentsc6left_breast)
    segmentsc6right_breast = normalization6(segmentsc6right_breast)


    # 因为最后都是拆开的 我要哪个就自己写就可以，比如这里不要实性囊性，就没加入segmentsb3left_breast这类的项
    # 下面都写了腋窝项，后来医生说乳腺项目里不谈腋窝，但下面那些也不用管它，改动这里的形式 后面的索引也需要跟着改，我在开始字典里删除了腋窝，腋窝这些不会提取到，不用管它
    print("\n")

    segmentsbfinal = [[['部位分割标志'], ['左乳'],segmentsb3left_breast,  segmentsb4left_breast, segmentsb5left_breast, segmentsb6left_breast],
                      [['部位分割标志'], ['右乳'],segmentsb3right_breast, segmentsb4right_breast, segmentsb5right_breast, segmentsb6right_breast],
                      [['部位分割标志'], ['左侧腋窝及锁骨区'],segmentsb3left_axilla,  segmentsb4left_axilla, segmentsb5left_axilla, segmentsb6left_axilla],
                      [['部位分割标志'], ['右侧腋窝及锁骨区'],segmentsb3right_axilla, segmentsb4right_axilla,
                       segmentsb5right_axilla, segmentsb6right_axilla]]

    segmentscfinal = [[['部位分割标志'], ['左乳'],segmentsc3left_breast,  segmentsc4left_breast, segmentsc5left_breast, segmentsc6left_breast],
                      [['部位分割标志'], ['右乳'], segmentsc3right_breast, segmentsc4right_breast, segmentsc5right_breast, segmentsc6right_breast],
                      [['部位分割标志'], ['左侧腋窝及锁骨区'],segmentsc3left_axilla, segmentsc4left_axilla, segmentsc5left_axilla, segmentsc6left_axilla],
                      [['部位分割标志'], ['右侧腋窝及锁骨区'], segmentsc3right_axilla,segmentsc4right_axilla,
                       segmentsc5right_axilla, segmentsc6right_axilla]]

    def match(segmentsbfinal, segmentscfinal, m, n):
        # m表示部位，0表示左乳，1表示右乳，2表示左腋窝锁骨，3表示右腋窝锁骨
        # n表示哪一个性质，2是良恶性,3是物理性质
        # 第一个判断语句为零这个到底输出什么需要确认下 好像不应该输出为1（不符合） 应该细化到缺少哪边信息 这里看后续需求书确认 而且我应该都是有初始值的 不应该有空的存在
        # 0: 符合  1: 不符合  2: 超声不明确  3: 病理不明确  4: 无法判断

        if (segmentscfinal[m])[n] == (segmentsbfinal[m])[n]:
            match = '0'
        if len((segmentscfinal[m])[n]) == 0 and len((segmentsbfinal[m])[n]) != 0:
            match = '2'
        if len((segmentscfinal[m])[n]) != 0 and len((segmentsbfinal[m])[n]) == 0:
            match = '3'
        if len((segmentscfinal[m])[n]) == 0 and len((segmentsbfinal[m])[n]) == 0:
            match = '4'
        elif (segmentscfinal[m])[n] != (segmentsbfinal[m])[n]:
            match = '1'

        return match

    matchleft3_breast = match(segmentsbfinal, segmentscfinal, 0, 2)      ##左乳良恶性匹配
    matchright3_breast = match(segmentsbfinal, segmentscfinal, 1, 2)
    matchleft4_breast = match(segmentsbfinal, segmentscfinal, 0, 3)      ##左乳物理性质匹配
    matchright4_breast = match(segmentsbfinal, segmentscfinal, 1, 3)
    matchleft5_breast = match(segmentsbfinal, segmentscfinal, 0, 4)  ##左乳物理性质匹配
    matchright5_breast = match(segmentsbfinal, segmentscfinal, 1, 4)
    # matchleft3_axilla = match(segmentsbfinal, segmentscfinal, 2, 2)
    # matchright3_axilla = match(segmentsbfinal, segmentscfinal, 3, 2)
    # matchleft4_axilla = match(segmentsbfinal, segmentscfinal, 2, 3)
    # matchright4_axilla = match(segmentsbfinal, segmentscfinal, 3, 3)

    matchleft_breast = ['部位分割标志', '左乳',  matchleft3_breast, matchleft4_breast, matchleft5_breast]
    matchright_breast = ['部位分割标志', '右乳',  matchright3_breast, matchright4_breast, matchright5_breast]
    # matchleft_axilla = ['部位分割标志', '左侧腋窝及锁骨区', matchleft4_axilla, matchleft4_axilla]
    # matchright_axilla = ['部位分割标志', '右侧腋窝及锁骨区', matchright4_axilla, matchleft4_axilla]


    # 这里没写错，病理性质确实他就是按照良性恶性来匹配的，都是良性可以，两边都出现恶性也可以，即按两边最恶性的来匹配，和良恶性方法是一样的
    # 即我病理报告的病理性质没有做归一化，可能有多个，可能没有，我是直接去匹配的
    # matchresult = [matchleft_breast, matchright_breast, matchleft_axilla, matchright_axilla]
    matchresult = [matchleft_breast, matchright_breast]

    segmentsbfinal_output = []
    if 0 in segmentsbnew_temp:
        segmentsbfinal_output.append(segmentsbfinal[0])
    if 1 in segmentsbnew_temp:
        segmentsbfinal_output.append(segmentsbfinal[1])
    if 2 in segmentsbnew_temp:
        segmentsbfinal_output.append(segmentsbfinal[2])
    if 3 in segmentsbnew_temp:
        segmentsbfinal_output.append(segmentsbfinal[3])

    segmentscfinal_output = []
    # 超声不同 超声是左乳右乳有没有出现都要补全的
    if 0 in segmentsbnew_temp:
        segmentscfinal_output.append(segmentscfinal[0])
    if 1 in segmentsbnew_temp:
        segmentscfinal_output.append(segmentscfinal[1])
    if 2 in segmentscnew_temp:
        segmentscfinal_output.append(segmentscfinal[2])
    if 3 in segmentscnew_temp:
        segmentscfinal_output.append(segmentscfinal[3])

    # 病理谈到哪些侧别，匹配结果跟病理保持一致
    matchresult_output = []
    if 0 in segmentsbnew_temp:
        matchresult_output.append(matchresult[0])
    if 1 in segmentsbnew_temp:
        matchresult_output.append(matchresult[1])
    if 2 in segmentsbnew_temp:
        matchresult_output.append(matchresult[2])
    if 3 in segmentsbnew_temp:
        matchresult_output.append(matchresult[3])
    # print(segmentsbnew_copy_step1)
    # print(segmentscnew_copy_step1)
    # print(segmentsbnew_copy_step2)
    # print(segmentscnew_copy_step2)
    # print('aaaaaa')
    return segmentsbnew_copy_step1, segmentscnew_copy_step1, segmentsbnew_copy_step2, segmentscnew_copy_step2, segmentsbfinal_output, segmentscfinal_output, matchresult_output
