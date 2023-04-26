from entity.sentence import Sentence
from entity.paragraph import *

# 部位归一化词典
word_prob_part_left_breast_normalize = {"左乳": 0.01, "左侧乳头": 0.01, "左侧乳房": 0.01, "左侧乳腺": 0.01,"左侧副乳": 0.01, "左":0.01 }
word_prob_part_right_breast_normalize =  {"右乳": 0.01, "右侧乳头": 0.01, "右侧乳房": 0.01, "右侧乳腺": 0.01, "右侧副乳": 0.01, "右":0.01 }

# 实性囊性归一化词典
word_prob_physical_solid  = {"实性": 0.05, "实质性": 0.045, "类实性": 0.048}
word_prob_physical_cystic = {"无病变": 0.01,"囊性": 0.03}

class Normalize:
    def __init__(self) -> None:
        pass
    
    def normalize_part(self, sentence : Sentence):
        part_term = sentence.part
        sideway = sentence.sideway
        part_word = part_term.word
        if sideway == '左':
            if part_word in word_prob_part_left_breast_normalize:
                part_term.word = '左乳'
        elif sideway == '右':
            if part_word in word_prob_part_right_breast_normalize:
                part_term.word = '右乳'
    
    def normalize_physical_property(self, sentence : Sentence):
        for physical_property_term in sentence.physical_property_list:
            if physical_property_term.word in word_prob_physical_solid:
                physical_property_term.word = '囊性'
            elif physical_property_term.word in word_prob_physical_cystic:
                physical_property_term.word = '实性'