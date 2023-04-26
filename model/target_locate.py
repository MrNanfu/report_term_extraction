from entity.paragraph import *
from entity.sentence import Sentence
word_prob_birads_weight = {"BI-RADS 0": 0.042, "BI-RADS 1": 0.01, "BI-RADS 2": 0.02, "BI-RADS 3": 0.03, 'BI-RADSⅢ':0.03, "BI-RADS 4a": 0.041,
                  "BI-RADS 4b": 0.043, "BI-RADS 4c": 0.044, "BI-RADS 5": 0.05, "BI-RADS 6": 0.04}
class TargetSentenceLocate:
    def __init__(self, paragraph : Paragraph) -> None:
        self.paragraph = paragraph
        self.paragraph_type = paragraph.report_type
        self.sentence_list = paragraph.sentence_list
    
    def divide_sentence_list_into_left_and_right(self):
        for sentence in self.sentence_list:
            if sentence.sideway == '左':
                self.paragraph.sentence_list_left.append(sentence)
            elif sentence.sideway == '右':
                self.paragraph.sentence_list_right.append(sentence)
                
    def get_max_indexes(lst):
        max_indexes = []
        max_val = max(lst)
        for i, val in enumerate(lst):
            if val == max_val:
                max_indexes.append(i)
        return max_indexes
    
    def locate_target_sentence_by_one_side(self, sentence_list):
        if self.paragraph_type == 0:
            if len(sentence_list) == 1:
                sentence_list[0].located = 1
            elif len(sentence_list) > 1:
                cnt_list = [0 for _ in range(len(sentence_list))]
                for idx, sentence in enumerate(sentence_list):
                    if sentence.valid == 0:
                        continue
                    pathological_property_list = sentence.pathological_property_list
                    if len(pathological_property_list) < 1:
                        continue
                    pathological_property_word = pathological_property_list[0].word
                    if pathological_property_word in word_prob_malignant or pathological_property_word in word_prob_benign_or_malignant or pathological_property_word in word_prob_junction_major:
                        cnt_list[idx] += 3
                    elif pathological_property_word in word_prob_benign_major:
                        cnt_list[idx] += 2
                    elif pathological_property_word in word_prob_benign_minor:
                        cnt_list[idx] += 1
                max_indexes = self.get_max_indexes(cnt_list)
                for idx in max_indexes:
                    sentence_list[idx].located = 1
        elif self.paragraph_type == 1:
            if len(sentence_list) == 1:
                sentence_list[0].located = 1
            elif len(sentence_list) > 1:
                cnt_list = [0 for _ in range(len(sentence_list))]
                for idx, sentence in enumerate(sentence_list): 
                    if  sentence.valid == 0:
                        continue
                    benign_malignant_property_list = sentence.benign_malignant_property_list
                    if len(benign_malignant_property_list) < 1:
                        continue
                    w =   word_prob_birads_weight[benign_malignant_property_list[0]]
                    cnt_list[idx] += w
                max_indexes = self.get_max_indexes(cnt_list)
                for idx in max_indexes:
                    sentence_list[idx].located = 1
            
            
    def locate_target_sentence(self):
        self.divide_sentence_list_into_left_and_right()
        self.locate_target_sentence_by_one_side(self.paragraph.sentence_list_left)
        self.locate_target_sentence_by_one_side(self.paragraph.sentence_list_right)
        sentence_list_left_located = []
        sentence_list_right_located = []
        for sentence in self.paragraph.sentence_list_left:
            if sentence.located == 1:
                sentence_list_left_located.append(sentence)
        for sentence in self.paragraph.sentence_list_right:
            if sentence.located == 1:
                sentence_list_right_located.append(sentence)    
        self.paragraph.sentence_list_left = sentence_list_left_located
        self.paragraph.sentence_list_right = sentence_list_right_located
        
        if self.paragraph_type == 1:
            self.paragraph.sentence_conclusion_left = self.paragraph.sentence_list_left[0]
            self.paragraph.sentence_conclusion_right = self.paragraph.sentence_list_right[0]          
        elif self.paragraph_type == 0:
            flg_occur_benign_or_malignant = 0
            for sentence in self.paragraph.sentence_list_left:
                if sentence.located == 0:
                    continue
                if sentence.pathological_property_list[0] in word_prob_malignant:
                    self.paragraph.sentence_conclusion_left = sentence
                    break
                elif sentence.pathological_property_list[0] in word_prob_benign_or_malignant or sentence.pathological_property_list[0] in word_prob_junction_major :
                    self.paragraph.sentence_conclusion_left = sentence
                    flg_occur_benign_or_malignant = 1
                elif flg_occur_benign_or_malignant == 0:
                    self.paragraph.sentence_conclusion_left = sentence
        
