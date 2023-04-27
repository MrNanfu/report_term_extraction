from entity.paragraph import Paragraph
from entity.sentence import Sentence
from entity.result import Result

# bi-rads良恶性
word_prob_birads_to_benign_malignant = {"BI-RADS 0": '良性或恶性待定', "BI-RADS 1": '没有发现病灶', "BI-RADS 2": '良性', "BI-RADS 3": '良性', 'BI-RADSⅢ':'良性', "BI-RADS 4a": '良性',
                  "BI-RADS 4b": '良性', "BI-RADS 4c": '恶性', "BI-RADS 5": '恶性', "BI-RADS 6": '已有病理结果'}

class Match:
    def __init__(self) -> None:
        self.result = Result()
        pass
    
    def match(self, paragrph0 : Paragraph, paragrph1 : Paragraph) -> Result:   
        """
        1. get target str from term_list and then put str of pathological and ultrasound into result
        2. judge 
        """     
        self.put_target_str_into_result(paragrph0.sentence_conclusion_left, paragrph1.sentence_conclusion_left, 0)
        self.put_target_str_into_result(paragrph0.sentence_conclusion_right, paragrph1.sentence_conclusion_right, 1)
        self.judge(0)
        self.judge(1)
        return self.result
    
    def get_str_from_term_list(self, term_list : list, type = 0):
        if len(term_list) == 0:
            return 'None'
        else:
            term = term_list[0]
            if type == 0:
                return term.word
            elif type == 1:
                return word_prob_birads_to_benign_malignant[term.word]
            
    
    def put_target_str_into_result(self, pathological_sentence_conclusion : Sentence, ultrasound_sentence_conclusion : Sentence, side : int = 0):
        #  get target str from term_list
        result = self.result
        sentence_p = pathological_sentence_conclusion
        sentence_u = ultrasound_sentence_conclusion
            
        if sentence_p is not None:
            sideway_str_p = sentence_p.sideway
            part_str_p = sentence_p.part.word
            pathological_property_str_p = self.get_str_from_term_list(sentence_p.pathological_property_list)
            benign_malignant_property_p = self.get_str_from_term_list(sentence_p.benign_malignant_property_list)
            physical_property_p = self.get_str_from_term_list(sentence_p.physical_property_list)
        if sentence_u is not None:
            sideway_str_u = sentence_u.sideway
            part_str_u = sentence_u.part.word
            pathological_property_str_u = self.get_str_from_term_list(sentence_u.pathological_property_list)
            benign_malignant_property_u = self.get_str_from_term_list(sentence_u.benign_malignant_property_list)
            physical_property_u = self.get_str_from_term_list(sentence_u.physical_property_list)
        
        
        # put str of pathological and ultrasound into result
        if side == 0: # 左侧
            if sentence_p is None:
                result.sideway_result_left.append('None')
                result.part_result_left.append('None')
                result.pathological_property_result_left.append('None')
                result.benign_malignant_property_result_left.append('None')
                result.physical_property_result_left.append('None')
            else:
                result.sideway_result_left.append(sideway_str_p)
                result.part_result_left.append(part_str_p)
                result.pathological_property_result_left.append(pathological_property_str_p)
                result.benign_malignant_property_result_left.append(benign_malignant_property_p)
                result.physical_property_result_left.append(physical_property_p)
            if sentence_u is None:
                result.sideway_result_left.append('None')
                result.part_result_left.append('None')
                result.pathological_property_result_left.append('None')
                result.benign_malignant_property_result_left.append('None')
                result.physical_property_result_left.append('None')
            else:    
                result.sideway_result_left.append(sideway_str_u)
                result.part_result_left.append(part_str_u)
                result.pathological_property_result_left.append(pathological_property_str_u)
                result.benign_malignant_property_result_left.append(benign_malignant_property_u)
                result.physical_property_result_left.append(physical_property_u)
        elif side == 1: #右侧
            if sentence_p is None:
                result.sideway_result_right.append('None')
                result.part_result_right.append('None')
                result.pathological_property_result_right.append('None')
                result.benign_malignant_property_result_right.append('None')
                result.physical_property_result_right.append('None')
            else:
                result.sideway_result_right.append(sideway_str_p)
                result.part_result_right.append(part_str_p)
                result.pathological_property_result_right.append(pathological_property_str_p)
                result.benign_malignant_property_result_right.append(benign_malignant_property_p)
                result.physical_property_result_right.append(physical_property_p)
            if sentence_u is None:
                result.sideway_result_right.append('None')
                result.part_result_right.append('None')
                result.pathological_property_result_right.append('None')
                result.benign_malignant_property_result_right.append('None')
                result.physical_property_result_right.append('None')
            else:    
                result.sideway_result_right.append(sideway_str_u)
                result.part_result_right.append(part_str_u)
                result.pathological_property_result_right.append(pathological_property_str_u)
                result.benign_malignant_property_result_right.append(benign_malignant_property_u)
                result.physical_property_result_right.append(physical_property_u)     
      
    
    def judge(self, type : int = 0):
        result = self.result
        if type == 0: # 左侧
            for particular_property_result in result.left_result:
                property_result_p = particular_property_result[0]
                property_result_u = particular_property_result[1]
                match_result = self.rule(property_result_p, property_result_u)
                particular_property_result.append(match_result) 
        elif  type == 1: # 右侧
            for particular_property_result in result.right_result:
                property_result_p = particular_property_result[0]
                property_result_u = particular_property_result[1]
                match_result = self.rule(property_result_p, property_result_u)
                particular_property_result.append(match_result)
    
    def rule(self, str1 : str, str2 : str) -> int:
        if str1 == 'None':
            return 7
        if str1 == str2:
            return 0
        if str1 != str2:
            return 1
            
            