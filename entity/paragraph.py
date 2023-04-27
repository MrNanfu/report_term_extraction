# -*- coding: utf-8 -*-
from entity.term  import Term
from entity.sentence  import Sentence
import copy
# 侧别
word_prob_sideway = {"左": 0.01, "右": 0.01, "左侧": 0.01, "右侧": 0.01}
word_prob_sideway_ultrasound = word_prob_sideway

# 部位
word_prob_part = {'左乳': 0.01,'右乳': 0.01,'双乳': 0.01,"左侧乳腺": 0.01,"右侧乳腺": 0.01,"双侧乳腺": 0.01,
                      "左侧乳房腺体": 0.01,"右侧乳房腺体": 0.01,"双侧乳房腺体": 0.01,"左侧乳头": 0.01,"右侧乳头": 0.01,
                      "左侧乳房": 0.01,"右侧乳房": 0.01,"双侧乳房": 0.01,
                      "切面": 0.01,"面部": 0.01, "左":0.01} #因为出现过 左乳乳房腺体这种事情的存在 导致提取了 左乳 病理空白 然后是 乳房腺体 加病 ，所以删除了单独的乳头、乳腺这类词汇
word_prob_part_ultrasound = word_prob_part
word_prob_left_breast = {"左乳": 0.01, "左侧乳头": 0.01, "左侧乳房": 0.01, "左侧乳腺": 0.01, "左侧副乳": 0.01, "左": 0.01}
word_prob_right_breast = {"右乳": 0.01, "右侧乳头": 0.01, "右侧乳房": 0.01, "右侧乳腺": 0.01, "右侧副乳": 0.01, "右": 0.01} 

# 部位拆分词典
word_prob_unfold_breast = { '双侧乳腺' : ['左侧乳腺', '右侧乳腺'], '双乳':[ '左乳', '右乳'], '双侧乳房':['左侧乳房', '右侧乳房'], '双侧乳头':['左侧乳头', '右侧乳头']}

#物理性质
word_prob_physical = {"无病变": 0.01,"囊性":0.01,"实性":0.01,"混合":0.01,"混合性":0.01,"囊实":0.01, "实质性":0.01, "类实性":0.01}
word_prob_physical_ultrasound = word_prob_physical

#除了直接找实性囊性词汇外，还通过如下病理性质推断出囊性，当时说除了这些都算实性(不过这个词典也是第一次皮下肿块的需求书里的词典，后续乳腺任务目前没给出实性囊性词典)
word_prob_physical_benign = {"导管扩张症":0.01,"积乳囊肿":0.01,"囊肿性病变":0.01,"纤维囊性变":0.01,"纤维囊性乳腺病":0.01,"囊肿": 0.01, "表皮样囊肿": 0.01, "皮样囊肿": 0.01, "皮脂腺囊肿": 0.01, "滑膜囊肿": 0.01, "粘液囊肿": 0.01,
                               "甲状舌管囊肿": 0.01, "间皮囊肿": 0.01, "腱鞘囊肿": 0.01, "毛根鞘囊肿": 0.01, "外毛根鞘囊肿": 0.01, "毛鞘囊肿": 0.01,
                               "毛囊源性囊肿": 0.01, "气管源性良性囊肿": 0.01, "鳃裂囊肿": 0.01}
word_prob_other = {"细胞":0.01,"导管":0.01,"腺体":0.01}

#良恶性
word_prob_benign_malignant = {"良": 0.01, "良性": 0.01, "恶": 0.01, "恶性": 0.01, "交界": 0.01, "交界性": 0.01, }#其实这里是重复的 但是开始时候文档给的是都带性的 后来发现实际里有不带性的 也应该识别上加上的
word_prob_benign_malignant_ultrasound = {"BI-RADS 1":0.01,"BI-RADS 2":0.01,"BI-RADS 3":0.01,'BI-RADSⅢ':0.01, "BI-RADS 4A":0.01,"BI-RADS 4B":0.01,"BI-RADS 4a":0.01,"BI-RADS 4b":0.01,"4a":0.01,"4b":0.01, "4A":0.01,"4B":0.01,"BI-RADS 4 a":0.01}


# 病理词典（分别包含恶性主要、良性或恶性主要、良性主要、交界性主要、良性次要）
word_prob_malignant_major = {"浸润性乳头状癌":0.01,"浸润性小叶癌":0.01,"浸润性导管癌":0.01,"浸润性癌":0.01, "浸润癌":0.01, "浸润性乳腺癌":0.01,"导管原位癌":0.01,"原位癌":0.01,"恶性叶状肿瘤":0.01,"包裹性乳头状癌":0.01,"实性乳头状癌":0.01,"导管内乳头状癌":0.01, "化生性癌":0.01}
word_prob_benign_or_malignant_major = {"非典型小叶增生":0.01,"导管内瘤":0.01, "肿瘤病变":0.01, "导管内乳头状病变":0.01, "纤维上皮性病变":0.01, "肿瘤性病变":0.01,"导管内乳头状肿瘤":0.01,"叶状肿瘤":0.01,"放射状瘢痕〈B3,不确定的潜在恶性病变）":0.01,"非典型导管增生":0.01,"非典型导管上皮增生":0.01, "导管上皮不典型增生":0.01, "导管上皮非典型增生":0.01, "平坦型上皮非典型增生":0.01,"平坦上皮非典型性":0.01,"导管上皮轻度非典型增生":0.01,"不典型增生":0.01,"导管上皮增生活跃":0.01, "非典型增生":0.01, "不典型导管增生":0.01, "导管上皮增生":0.01,"导管上皮增生稍活跃(B3,不确定的潜在恶性病变）":0.01,"上皮源性肿瘤":0.01}
word_prob_benign_major = {"肉芽肿性乳腺炎":0.01,"泌乳腺瘤":0.01,"化脓性乳腺炎":0.01,"普通型增生":0.01, "肉芽肿":0.01,"肉芽肿性炎":0.01, "硬化性腺病":0.01, "错构瘤":0.01, "导管内乳头状瘤":0.01,"导管乳头状瘤":0.01, "导管内乳头状瘤炎性病变":0.01,"炎性":0.01,"炎症性改变":0.01,"炎症性":0.01,"炎症改变":0.01,"小叶性肉芽肿性乳腺炎":0.01,"小叶肉芽肿性乳腺炎":0.01,"肉芽肿性小叶炎":0.01,"肉芽肿性小叶性乳腺炎":0.01,"非特异性炎症性病变纤维上皮肿瘤":0.01, "梭形细胞病变":0.01, "非特异性炎症性病变":0.01, "纤维上皮性":0.01, "纤维上皮性肿瘤":0.01,"良性纤维上皮性肿瘤":0.01,"纤维腺瘤样增生":0.01,"纤维腺瘤":0.01,"纤维腺瘤改变":0.01,"幼年型纤维腺瘤":0.01,"良性叶状肿瘤":0.01,"泌乳性腺瘤":0.01,"管状腺瘤":0.01,"结节性泌乳性增生硬化性腺病":0.01, "结节性泌乳性增生":0.01, "错构瘤硬化性腺病":0.01, "复杂硬化性":0.01, "复杂性硬化性":0.01, "复杂硬化性病变":0.01, "表皮样囊肿":0.01, "复杂性硬化性病表皮样囊肿":0.01,"纤维囊性乳腺病":0.01,"纤维囊性变":0.01,"囊肿性病变":0.01, "积乳囊肿":0.01, "囊肿":0.01,"导管扩张症新辅助治疗后改变":0.01,"化疗后改变":0.01,"未见确切恶性肿瘤细胞":0.01,"未见肿瘤":0.011}
word_prob_junction_major = {"交界性叶状肿瘤" : 0.01}
# word_prob_benign_major_ultrasound = {"导管内沉积物":0.01,"普通型增生":0.01, "肉芽肿":0.01,"肉芽肿性炎":0.01, "硬化性腺病":0.01, "错构瘤":0.01, "导管内乳头状瘤":0.01, "导管内乳头状瘤炎性病变":0.01,"炎性":0.01,"炎症性改变":0.01,"炎症性":0.01,"炎症改变":0.01,"小叶性肉芽肿性乳腺炎":0.01,"小叶肉芽肿性乳腺炎":0.01,"肉芽肿性小叶炎":0.01,"肉芽肿性小叶性乳腺炎":0.01,"非特异性炎症性病变纤维上皮肿瘤":0.01, "梭形细胞病变":0.01, "非特异性炎症性病变":0.01, "纤维上皮性":0.01, "纤维上皮性肿瘤":0.01,"良性纤维上皮性肿瘤":0.01,"纤维腺瘤样增生":0.01,"纤维腺瘤":0.01,"纤维腺瘤改变":0.01,"幼年型纤维腺瘤":0.01,"良性叶状肿瘤":0.01,"泌乳性腺瘤":0.01,"管状腺瘤":0.01,"结节性泌乳性增生硬化性腺病":0.01, "结节性泌乳性增生":0.01, "错构瘤硬化性腺病":0.01, "复杂硬化性":0.01, "复杂性硬化性":0.01, "复杂硬化性病变":0.01, "表皮样囊肿":0.01, "复杂性硬化性病表皮样囊肿":0.01,"纤维囊性乳腺病":0.01,"纤维囊性变":0.01,"囊肿性病变":0.01, "积乳囊肿":0.01, "囊肿":0.01,"导管扩张症新辅助治疗后改变":0.01,"化疗后改变":0.01,"未见确切恶性肿瘤细胞":0.01,"未见肿瘤":0.01}
word_prob_benign_minor = {"胶原增生":0.01,"增生结节":0.01,"瘤样增生":0.01,"腺病":0.01,"间质纤维胶原组织增生":0.01,"假血管瘤样增生":0.01,"脂肪瘤":0.01,"囊肿": 0.01,"柱状细胞增生":0.01,"柱状细胞变":0.01,"导管上皮柱状细胞变":0.01,"柱状上皮化生腺病":0.01,"导管上皮普通型增生":0.01,"导管上皮呈普通型增生":0.01,"导管上皮呈筛状增生":0.01,"导管上皮呈旺炽性增生":0.01,"导管普通型增生":0.01,"筛孔状增生":0.01,"导管上皮轻度增生":0.01,"导管上皮增生脂肪组织坏死纤维胶原增生":0.01,"间质纤维增生":0.01,"间质胶原增生":0.01, "间质胶原纤维增生":0.01, "胶原纤维增生":0.01, "大汗腺化生":0.01, "假血管瘤样间质增生":0.01,"假血管瘤样间质增生大汗腺化生":0.01}

# 主要诊断、次要诊断
word_prob_major = {**word_prob_malignant_major, **word_prob_benign_or_malignant_major, **word_prob_benign_major}
word_prob_minor = {**word_prob_benign_minor}

# 整体恶性词典、整体良恶性均可词典、整体良性词典、整体交界词典
word_prob_malignant = word_prob_malignant_major
word_prob_benign_or_malignant = word_prob_benign_or_malignant_major
word_prob_benign = {**word_prob_benign_major, **word_prob_benign_minor}
word_probjiaojie = word_prob_junction_major

# 超声报告和病理报告不是共用一个病理性质词典
word_prob_pathological_property={**word_prob_malignant, **word_prob_benign_or_malignant,**word_prob_benign, **word_probjiaojie}



# 病理性质相关语义字典
word_prob_patological_property_semantics = {"建议免疫组化":0.01,  "待免疫组化":0.01,"免疫组化":0.01, "伴":0.01, "个别":0.01, "部分":0.01, "主体":0.01, "的": 0.01}

# 病理匹配结果可信度词典
word_prob_reliability = {"建议": 0.01, "鉴别": 0.01, "排除": 0.01, "待": 0.01, "需": 0.01, "进一步": 0.01}

# 无效语句词典
word_prob_invalid = {'切缘': 0.01, '皮缘': 0.01, '新辅': 0.01, '化疗': 0.01, '副乳': 0.01}

#否定词, 出现否定词的时候 它形容的那些病理性质需要排除掉或者取反，下面列出了一些需要排除的
word_prob_negative_false_word = {'不完全除外': 0.01, '不能除外': 0.01, '不除外': 0.01 ,'考虑': 0.01, '疑' : 0.01}    #和上面切面那个问题同理，都是利用最大匹配的算法，这里由于'不除外''不能除外'虽然表达肯定意思，但是如果不把这些词放里，就会提取到除外这样的否定词
word_prob_negative_word_all={'不支持':0.01,'有无': 0.01,'不排除':0.01,'排除':0.01,'鉴别':0.01,'不完全除外':0.01,'不能除外':0.01,'不除外':0.01,'除外':0.01,'未见': 0.01}

#语义词典汇总
word_prob_semantics = {**word_prob_patological_property_semantics, **word_prob_reliability, **word_prob_invalid,** word_prob_negative_word_all}

# 有效标点词典
word_prob_comma={'，':0.01,'；':0.01,'、':0.01}     # 注意打字时候这里是中文标点
word_prob_full_stop={'。':0.01}     # 中文句号
word_prob_semicolon = {';':0.01}
word_prob_sep = {**word_prob_full_stop, **word_prob_semicolon, **word_prob_comma}

# 病理报告关键词汇总词典
word_prob_pathological_all={**word_prob_part, **word_prob_physical,**word_prob_benign_malignant,**word_prob_pathological_property, **word_prob_semantics, **word_prob_sep, **word_prob_other}

# 超声关键词汇总
word_prob_ultrasound_all={**word_prob_part, **word_prob_physical,**word_prob_benign_malignant_ultrasound,**word_prob_pathological_property, **word_prob_semantics, **word_prob_sep, **word_prob_other}
# 部位归一化词典
word_probc2zhoubu = {"肘": 0.01} 
word_probb2shouwanbu = {"手": 0.02, "腕": 0.02, "指": 0.02, "虎口": 0.02} 
word_probb2xibu = {"膝": 0.01, "腘窝": 0.01}
word_probb2zuhuaibu = {"足": 0.01, "踝": 0.01, "趾": 0.01}
word_probb2xiongbi = {"胸": 0.01}
word_probb2fubi = {"腹": 0.01, "剑突": 0.01, "脐": 0.01}
word_probb2beibu = {"背": 0.01, "腰": 0.01, "胸背": 0.01}
word_probb2jianbu = {"肩": 0.01}
word_probb2kuanbu = {"腹股沟": 0.01, "髋": 0.01}
word_probb2tunbu = {"骶": 0.01, "臀": 0.01, "肛": 0.01}
word_probb2yanmianbu = {"颊": 0.01, "面": 0.01, "眼": 0.01, "眉": 0.01, "耳": 0.01, "颌": 0.01, "颏": 0.01}
word_probb2toubu = {"顶": 0.01, "额": 0.01, "枕": 0.01, "颞": 0.01, "头皮": 0.01}
word_probb2jingbu = {"颈": 0.01}
word_probb2yewosuogu = {"腋窝": 0.01, "锁骨": 0.01}
word_probb2yewosuoguleft={"左侧腋窝": 0.01,"左侧锁骨": 0.01,"左腋窝": 0.01,"左锁骨": 0.01}
word_probb2yewosuoguright = {"右侧腋窝": 0.01,"右侧锁骨": 0.01,"右腋窝": 0.01,"右锁骨": 0.01}
word_probb2yewosuogudouble= {"双侧腋窝": 0.01,"双侧锁骨": 0.01,"双腋窝": 0.01,"双锁骨": 0.01}

# 病理性质归一化词典
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
word_probb5daoguan = {'导管内瘤': 0.01, '导管内乳头状肿瘤': 0.01}
word_probb5xianbing = {'瘤样增生':0.01,'增生结节':0.01}

class Paragraph:
    """
    The structure of a paragraph is (sentence1, ... ,  sentenceN), the number of sentence is more or equal to 1
    Args:
        report_type: 0 -> pathological_report, 1 -> ultrasound_report
    """
    def __init__(self, input : str = '', report_type : int = 0) -> None:
        self.input = input
        self.report_type = report_type
        self.position_start = 0
        self.position_end = len(input) - 1
        self.raw_term_list = []
        self.processed_term_list = []
        self.sentence_list = []
        self.sentence_list_left = []
        self.sentence_list_right = []
        self.sentence_conclusion_left = None
        self.sentence_conclusion_right = None
        
    
    @ staticmethod
    def findsegments(input, word_prob):     # 最长字符匹配函数， 返回的list中偶数位为匹配字符，奇数位为在input中的位置
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
    
    def constrcut_raw_term_list(self):
        """
        1. find out the all raw_words of input
        2. set the word, position, type of the term according to raw_word and append the raw_term to raw_term_list
        """
        # find out the all raw_words of input
        raw_word_list = []
        if self.report_type == 0:
            raw_word_list = Paragraph.findsegments(self.input, word_prob_pathological_all)
        else:
            raw_word_list = Paragraph.findsegments(self.input, word_prob_ultrasound_all)
        for i in range(int(len(raw_word_list) / 2)):
            raw_word = raw_word_list[2 * i]
            position_paragraph = raw_word_list[2 * i + 1]
            # type: 1->sideway, 2->part, 3->pathological_property, 4->benign_malignant_property, 5->physical_property, 6->semantics, 7->sep, 8->others
            if raw_word in word_prob_sideway:
                type = 1
            if raw_word in word_prob_part:  
                type = 2
            if raw_word in word_prob_pathological_property:  
                type = 3
            # if self.report_type == 0 and raw_word in word_prob_benign_malignant:  
            #     type = 4
            if self.report_type == 1 and raw_word in word_prob_benign_malignant_ultrasound:  
                type = 4
            if raw_word in word_prob_physical:  
                type = 5
            if raw_word in word_prob_semantics:
                type = 6     
            if raw_word in word_prob_sep:
                type = 7
            if raw_word  in word_prob_other:
                type = 8       
            # set the word, position, type of the term according to raw_word and append the raw_term to raw_term_list
            self.raw_term_list.append(Term(raw_word, position_paragraph, type)) 
    
    def select_specific_term_list(self, term_list : list, type : int):
        specific_term_list = []
        for term in term_list:
            if term.type == type:
                specific_term_list.append(term)
        return specific_term_list
        
    
    def process_raw_term_list(self):
        """
        1. normalize sideway
        2. normalize part 
        3. process part to convert '左乳xxx右乳' into '双乳'
        4. normalize benigh_malignant
        """
        processed_term_list = []
        raw_term_list = self.raw_term_list
        processed_term_list = copy.deepcopy(self.raw_term_list) 
        # normalize sideway
        for term in processed_term_list:
            if term.type == 1:
                if term.word in {"左": 0.01, "左侧": 0.01}:
                    term.word = '左'
                if term.word in {"右": 0.01, "右侧": 0.01}:
                    term.word = '右'
                    
        #  normalize part 
        for term in processed_term_list:
            if term.type != 2:
                continue
            if term.word in word_probc2zhoubu.keys():
                term.word = '肘部'
            if term.word in word_probb2shouwanbu.keys():
                term.word = '手腕部'
            if term.word in word_probb2xibu.keys():
                term.word = '膝部'
            if term.word in word_probb2zuhuaibu.keys():
                term.word = '足踝部'
            if term.word in word_probb2xiongbi.keys():
                term.word = '胸壁'
            if term.word in word_probb2fubi.keys():
                term.word = '腹壁'
            if term.word in word_probb2beibu.keys():
                term.word = '背部'
            if term.word in word_probb2jianbu.keys():
                term.word = '肩部'
            if term.word in word_probb2kuanbu.keys():
                term.word = '髋部'
            if term.word in word_probb2tunbu.keys():
                term.word = '臀部'
            if term.word in word_probb2yanmianbu.keys():
                term.word = '颜面部'
            if term.word in word_probb2toubu.keys():
                term.word = '头部'
            if term.word in word_probb2jingbu.keys():
                term.word = '颈部'
            if term.word=='乳房腺体':
                term.word = '乳腺'
            if term.word=='右侧乳房腺体':
                term.word = '右侧乳腺'
            if term.word=='左侧乳房腺体':
                term.word = '左侧乳腺'
            if term.word=='双侧乳房腺体':
                term.word = '双侧乳腺'
            if term.word=='右侧副乳腺肿物':
                term.word = '右侧副乳'
            if term.word=='左侧副乳腺肿物':
                term.word = '左侧副乳'
            if term.word=='双侧副乳腺肿物':
                term.word = '双侧副乳'
            if term.word in word_probb2yewosuogu.keys():
                term.word = '腋窝及锁骨区'
            if term.word in word_probb2yewosuoguleft.keys():
                term.word = '左侧腋窝及锁骨区'
            if term.word in word_probb2yewosuoguright.keys():
                term.word = '右侧腋窝及锁骨区'
            if term.word in word_probb2yewosuogudouble.keys():
                term.word = '双侧腋窝及锁骨区'

        # process part to convert '左乳xxx右乳' into '双乳'
        eps = 15
        flg = 0
        part_term_list = []
        part_term_list = self.select_specific_term_list(processed_term_list, 2)
        for i in range(len(part_term_list) - 1):
            pre_word = part_term_list[i].word
            next_word = part_term_list[i + 1].word
            pre_position_paragraph = part_term_list[i].position_paragraph
            next_position_paragraph = part_term_list[i + 1].position_paragraph
            if pre_word in word_prob_left_breast and next_word in word_prob_right_breast and (next_position_paragraph - pre_position_paragraph) <= eps:
                part_term_list[i].word = '双乳'
                if i == len(part_term_list) - 2:
                    flg = 1
                # delete next term in processed_term_list
                for term in processed_term_list:
                    if term.position_paragraph == next_position_paragraph:
                        processed_term_list.remove(term)
                        break
                i += 1

        
        # normalize benigh_malignant
        if self.report_type == 0:
            for term in processed_term_list:
                if term.type == 4:
                    if term.word in {"良性": 0.01, "良": 0.01}:
                        term.word = '良性'
                    if term.word in  {"恶性": 0.01, "恶": 0.01}:
                        term.word = '恶性'
        else:
            for term in processed_term_list: 
                if term.type == 4:
                    if term.word =="BI-RADS 4A":
                        term.word = "BI-RADS 4a"
                    if term.word =="BI-RADS 4 a":
                        term.word = "BI-RADS 4a"
                    if term.word =="BI-RADS 4B":
                        term.word = "BI-RADS 4b"
                    if term.word =="BI-RADS 4C":
                        term.word = "BI-RADS 4c"
                    if term.word =="4A":
                        term.word = "BI-RADS 4a"
                    if term.word =="4B":
                        term.word = "BI-RADS 4b"
                    if term.word =="4C":
                        term.word = "BI-RADS 4c"
                    if term.word =="4a":
                        term.word = "BI-RADS 4a"
                    if term.word =="4b":
                        term.word = "BI-RADS 4b"
                    if term.word =="4c":
                        term.word = "BI-RADS 4c"
        
        # physical and benigh_malignant generation acoording to pathological property will be done after construct sentence_list
        self.processed_term_list = processed_term_list
    
    @ staticmethod
    def is_contain_term_type_from_positiona_to_positionb(processed_term_list : list, positiona : int, positionb : int, type : int, is_paragraphy : bool = True):
        assert positiona < positionb
        for term in processed_term_list:
            if is_paragraphy:
                if term.type == type and term.position_paragraph < positionb and term.position_paragraph > positiona:
                    return True
            else:
                if term.type == type and term.position_sentence < positionb and term.position_sentence > positiona:
                    return True     
        return False
    
    def add_term_to_sentence_from_positiona_to_positionb(self, s : Sentence, positiona : int, positionb : int):
        assert positiona < positionb
        cnt = 0
        for term in self.processed_term_list:
            if term.position_paragraph >= positiona and term.position_paragraph < positionb:
                s.add_term(term, position_sentence=cnt)
                cnt += 1
        if positionb == self.position_end:
            s.add_term(self.processed_term_list[-1], position_sentence=cnt)
        s.classify_term_into_property_list()
        s.locate_position_start_end()
        
    
    def construct_sentence_list(self):
        """
        Construct the sentence list according to processed_term_list
        The structure of a sentence is ('part', 'pathological_propert1', ... 'pathological_propertN', ..., others)
        """
        processed_term_list = self.processed_term_list
        part_term_list = []
        part_term_list = self.select_specific_term_list(processed_term_list, 2)
        sentence_check_type = 3
        if self.report_type == 1:
            sentence_check_type = 4
        eps = 10
        for i in range(len(part_term_list)):
            s = Sentence()
            if i == len(part_term_list) - 1:
                if Paragraph.is_contain_term_type_from_positiona_to_positionb(self.processed_term_list, part_term_list[i].position_paragraph, self.position_end, sentence_check_type):
                    self.add_term_to_sentence_from_positiona_to_positionb(s=s, positiona=part_term_list[i].position_paragraph, positionb=self.position_end)
                    self.sentence_list.append(s)
            else:
                if (part_term_list[i + 1].position_paragraph - part_term_list[i].position_paragraph) > eps and Paragraph.is_contain_term_type_from_positiona_to_positionb(self.processed_term_list,  part_term_list[i].position_paragraph,  part_term_list[i + 1].position_paragraph, sentence_check_type):
                    self.add_term_to_sentence_from_positiona_to_positionb(s=s, positiona=part_term_list[i].position_paragraph, positionb=part_term_list[i + 1].position_paragraph)
                    self.sentence_list.append(s)
                
    def convert_input_to_sentence_list(self):
        """
        1. convert input to term_list
        2. process term_list
        3. convert term_list into sentence_list
        """
        self.constrcut_raw_term_list()  # extraction keywords
        self.process_raw_term_list()    # process the keywords
        self.construct_sentence_list()  # seperate keywords into different sentences
    
    def process_sentence_list(self):
        """
        1. define invalid pathological sentence
        2. process negative keywords
        3. unfold '双乳'
        4. generate physics according  pathological property
        """

        # define invalid pathological sentence
        for sentence in self.sentence_list:
            for term in sentence.term_list:
                if term.word in word_prob_invalid:
                    sentence.valid = 0
                    break
        
        # process negative keywords
        for sentence in self.sentence_list:
            if sentence.valid == 0:
                continue
            
            # select comma, spe, negative terms
            term_list_comma = []
            term_list_sep = []
            term_list_negative = []
            for term in sentence.term_list:
                if (term.word in word_prob_negative_word_all) and (term.word not in word_prob_negative_false_word):
                    term_list_negative.append(term)
                if term.word in word_prob_comma:
                    term_list_comma.append(term)
                if term.word in word_prob_sep:
                    term_list_sep.append(term)
            
            # select position_l on the left of negative_term and  position_r on the right of negative_term
            position_list_l = []
            position_list_r = []
            for negative_term in term_list_negative:
                flg_r = 0
                flg_l = 0
                for sep_term in term_list_sep:
                    if sep_term.position_paragraph > negative_term.position_paragraph:
                        position_list_r.append(sep_term.position_paragraph)
                        flg_r = 1
                        break
                if flg_r == 0:
                    position_list_r.append(self.position_end)
                
                for i in range(len(term_list_comma) - 1):
                    if term_list_comma[i].position_paragraph < negative_term.position_paragraph and term_list_comma[i + 1].position_paragraph > negative_term.position_paragraph:
                        position_list_l.append(term_list_comma[i].position_paragraph)
                        flg_l = 1
                        break
                if term_list_comma[len(term_list_comma) - 1].position_paragraph < negative_term.position_paragraph:
                    position_list_l.append(term_list_comma[len(term_list_comma) - 1].position_paragraph)
                    flg_l = 1
                if flg_l == 0:
                    position_list_l.append(self.position_start)
            
            # filter terms by using position_list_l and position_list_r
            if len(position_list_l) != 0:
                term_list_new = []
                for term in sentence.term_list:
                    if term.position_paragraph <= position_list_l[0] or term.position_paragraph >= position_list_r[-1]:
                        term_list_new.append(term)
                    else:
                        for i in range(len(position_list_l)):
                            if term.position_paragraph > position_list_l[i] and term.position_paragraph < position_list_r[i]:
                                continue
                            term_list_new.append(term)
            
                sentence.term_list = term_list_new
                sentence.classify_term_into_property_list   # it is always done if sentence.term_list changed
                sentence.locate_position_start_end
        
        # unfold '双乳' 
        sentence_list_new = []
        for sentence in self.sentence_list:
            if sentence.part.word not in word_prob_unfold_breast:
                sentence_list_new.append(sentence)
            if sentence.part.word in word_prob_unfold_breast:
                part = ''
                for key in word_prob_unfold_breast.keys():
                    if sentence.part.word == key:
                        part = key
                part_l = word_prob_unfold_breast[part][0]
                part_r = word_prob_unfold_breast[part][1]
                sentence_l = copy.deepcopy(sentence)
                sentence_r = copy.deepcopy(sentence)
                sentence_l.part.word = '左乳'
                sentence_l.sideway = '左'
                sentence_r.part.word = '右乳'
                sentence_r.sideway = '右'
                sentence_list_new.append(sentence_l)
                sentence_list_new.append(sentence_r)
        self.sentence_list = sentence_list_new
        
        # generate pathological according  pathological property
        for sentence in self.sentence_list:
            for pathological_property in sentence.pathological_property_list:
                if pathological_property in word_prob_physical_benign:
                    sentence.add_term(Term('囊性', pathological_property.position_paragraph, 5))
                else:
                    sentence.add_term(Term('实性', pathological_property.position_paragraph, 5))
            sentence.classify_term_into_property_list()
                    
    def convert_input_to_paragraph(self):  
        self.convert_input_to_sentence_list()
        self.process_sentence_list()

if __name__ == '__main__':
    # input = "“左乳肿物”①良性囊肿；②乳腺腺病，部分导管上皮增生，倾向为普通型增生，建议行免疫组化协诊排除不典型增生。※如同意做免疫组化请于工作日至外科楼二楼病理科办理相关手续。"
    # print(input)
    # paragraph_0 = Paragraph(input, 0)
    # paragraph_0.convert_input_to_paragraph()
    # print(paragraph_0)
    
    input = "双侧乳腺内实质性结节（M1），BI-RADS 4a类。"
    print(input)
    paragraph_1 = Paragraph(input, 1)
    paragraph_1.convert_input_to_paragraph()
    print(paragraph_1)
