# -*- coding:utf-8 -*-
#批量把医生给到的词汇处理成字典形式
s1='柱状细胞增生/柱状细胞变/导管上皮柱状细胞变/柱状上皮化生腺病/导管上皮普通型增生/导管上皮呈普通型增生/导管上皮呈筛状增生/导管上皮呈旺炽性增生/导管普通型增生/筛孔状增生/导管上皮轻度增生/导管上皮增生脂肪组织坏死纤维胶原增生/间质纤维增生/间质胶原纤维增生/假血管瘤样间质增生大汗腺化生/腺病/'
s1=s1.replace('/','":0.01,"')
print(s1)


