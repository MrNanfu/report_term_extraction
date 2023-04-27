from entity.paragraph import *
from model.normalize import Normalize



class Extracion:
    def __init__(self, paragraph : Paragraph) -> None:
        self.paragraph = paragraph
        self.paragraph_type = paragraph.report_type
        self.sentence_list = paragraph.sentence_list
    
    def part_extraction(self):
        normalize = Normalize()
        for sentence in self.sentence_list:
            if sentence.valid == 0:
                continue
            normalize.normalize_part(sentence)
    
    def pathological_property_extraction(self):
        """
        For ultrasound report:
            extract the first pathological_property as the target_pathological_property
        For pathological report:
            1. if '免疫组化' keyword exists and then extract the first pathological_property following '免疫组化' keywords
            2. elif there is only one pathological_property,  do nothing 
            3. elif there are more than one pathological_property, extract the target_pathological_property according to benign_malignant, major_minor and senmatics
            4. elif there is no pathological_property, extract '细胞', '腺体', '导管'
        """
        if self.paragraph_type == 1:    # extract pathological_property of ultrasound report
            for sentence in self.sentence_list:
                if sentence.valid == 0:
                    continue
                if len(sentence.pathological_property_list) != 0:
                    pathological_property_term = sentence.pathological_property_list[0]
                    self.sentence.pathological_property_list = []
                    self.sentence.pathological_property_list.append(pathological_property_term)
        elif self.paragraph_type == 0:  # extract pathological_property of pathological report
            for sentence in self.sentence_list:
                if sentence.valid == 0:
                    continue
                # if '免疫组化' keyword exists and then extract the first pathological_property following '免疫组化' keywords
                flg_mianyizuhua = 0
                for semantics_term in sentence.semantics_list:
                    if '免疫组化' in semantics_term.word:
                        position_mianyizuhua = semantics_term.position_paragraph
                        pathological_property_list_new = []
                        for pathological_property_term in sentence.pathological_property_list:
                            if pathological_property_term.position_paragraph > position_mianyizuhua and abs(pathological_property_term.position_paragraph - position_mianyizuhua) < 10:
                                pathological_property_list_new.append(pathological_property_term)
                                sentence.pathological_property_list = pathological_property_list_new
                                flg_mianyizuhua = 1
                                break
                if flg_mianyizuhua == 1:
                    break

                # elif there is only zero or one pathological_property, do nothing 
                
                # elif there are more than one pathological_property, extract the target_pathological_property according to benign_malignant, major_minor and senmatics
                elif len(sentence.pathological_property_list) > 1:
                    cnt_list = [0, 0, 0, 0, 0]    # 0:  major_malignant, 1: major_benign_or_malignant, 2: major_benign,3:  major_junction, 4: minor_benign
                    for term in sentence.pathological_property_list:
                        if term.word in word_prob_malignant_major:
                            cnt_list[0] += 1
                        elif term.word in word_prob_benign_or_malignant_major:
                            cnt_list[1] += 1
                        elif term.word in word_prob_benign_major:
                            cnt_list[2] += 1
                        elif term.word in word_prob_junction_major:
                            cnt_list[3] += 1
                        elif term.word in word_prob_benign_minor:
                            cnt_list[4] += 1                   
                    cnt_major = cnt_list[0] + cnt_list[1] + cnt_list[2] + cnt_list[3]
                    cnt_minor = cnt_list[4]
                    cnt_all = cnt_major + cnt_minor
                    pathological_property_list_new = []
                    if cnt_major > 0:
                        # if cnt_major == 1, do nothing to sentence.pathological_property_list
                        
                        # if cnt_major > 1, extract pathological_property according to benign_malignant and semantics
                        if cnt_list[0] > 0:     # cnt_malignant > 0
                            for term in sentence.pathological_property_list:
                                if term.word in word_prob_malignant:
                                    pathological_property_list_new.append(term)
                            sentence.pathological_property_list = pathological_property_list_new
                        elif cnt_list[1] > 0 or cnt_list[3] > 0:    # cnt_malignant = 0 , cnt_malignant_or_benign > 0 or cnt_junction > 0
                            for term in sentence.pathological_property_list:
                                if term.word in word_prob_benign_or_malignant_major or term.word in word_prob_junction_major:
                                    pathological_property_list_new.append(term)
                            sentence.pathological_property_list = pathological_property_list_new
                        else:   # except below condition, cnt_major_benign > 0 or cnt_minor_benign > 0, so extract pathological_property according to senmatics
                            benign_property_list = []
                            weight_pathological_property_list = []
                            for term in sentence.pathological_property_list: 
                                if term.word in word_prob_benign:
                                    benign_property_list.append(term)
                                    weight_pathological_property_list.append(0)
                            flg = 0
                            for term in sentence.semantics_list:  
                                # if it occur to that "pathological_property1, '伴' pathological_property2", and then weight_pathological_property2 -= 1
                                if term.word in {'伴':0.01, '个别':0.01, '部分':0.01}:
                                    for idx, benign_property_term in enumerate(benign_property_list):
                                        if benign_property_term.position_paragraph > term.position_paragraph:
                                            weight_pathological_property_list[idx] -= 1
                                            flg = 1
                                            break
                                # if it occur to that " '主体' pathological_property1", and then weight_pathological_property1 += 1
                                elif term.word in {'主体':0.01}:
                                    for idx, benign_property_term in enumerate(benign_property_list):
                                        if benign_property_term.position_paragraph > term.position_paragraph:
                                            weight_pathological_property_list[idx] += 1
                                            flg = 1
                                            break
                                # if it occur to that "pathological_property1 '的' pathological_property2 ", weight_pathological_property2 = -1
                                elif term.word in {'的':0.01}:
                                    for idx, benign_property_term in enumerate(benign_property_list):
                                        if benign_property_term.position_paragraph > term.position_paragraph and (benign_property_term.position_paragraph - term.position_paragraph) < 3:
                                            weight_pathological_property_list[idx - 1] = -1
                                            flg = 1
                                            break 
                            # calculate all weight_value
                            weight_all = 0
                            for weight in weight_pathological_property_list:
                                weight_all += weight         
                            # if there is no semantical information, and then select last pathological_property as target_pathological_property                
                            if weight_all == 0:
                                pathological_property_list_new.append(sentence.pathological_property_list[-1]) 
                                sentence.pathological_property_list = pathological_property_list_new
                            else:
                                max_value = max(weight_pathological_property_list)
                                max_idx = weight_pathological_property_list.index(max_value)
                                pathological_property_list_new.append(benign_property_list[max_idx]) 
                                sentence.pathological_property_list = pathological_property_list_new
                    else:
                        for pathological_property_term in sentence.pathological_property_list:
                            if pathological_property_term.word in word_prob_minor:
                                pathological_property_list_new.append(pathological_property_term)
                                break
                        sentence.pathological_property_list = pathological_property_list_new              

    def benign_malignant_property_extracion(self):
        """
        For pathological report:
            generate benign_malignant property according to extracted pathological property
        For ultrasound report:
            nothing to do

        """
        if self.paragraph_type == 0:
            for sentence in self.sentence_list:
                if sentence.valid == 0:
                    continue
                if len(sentence.pathological_property_list) == 0:
                    continue
                pathological_property_term = sentence.pathological_property_list[0]
                if pathological_property_term.word in word_prob_malignant:
                    sentence.benign_malignant_property_list.append(Term('恶性', pathological_property_term.position_paragraph, 4))
                elif pathological_property_term.word in word_prob_benign_or_malignant:
                    sentence.benign_malignant_property_list.append(Term('良性或恶性待定', pathological_property_term.position_paragraph, 4))
                elif pathological_property_term.word in word_prob_benign:
                    sentence.benign_malignant_property_list.append(Term('良性', pathological_property_term.position_paragraph, 4))
                elif pathological_property_term.word in word_prob_junction_major:
                    sentence.benign_malignant_property_list.append(Term('交界性', pathological_property_term.position_paragraph, 4))
                  
    
    def physical_property_extracion(self):
        """
        For pathological report:
            generate physical property according to extracted pathological property
        For ultrasound report:
            nothing to do
        """
        normalize =  Normalize()
        if self.paragraph_type == 0:
            for sentence in self.sentence_list:
                if sentence.valid == 0:
                    continue
                if len(sentence.pathological_property_list) == 0:
                    continue
                pathological_property_term = sentence.pathological_property_list[0]
                physical_property_list_new = []
                if pathological_property_term.word in word_prob_physical_benign:
                    physical_property_list_new.append(Term('囊性', pathological_property_term.position_paragraph, 5))
                    
                else:
                    physical_property_list_new.append(Term('实性', pathological_property_term.position_paragraph, 5))
                sentence.physical_property_list = physical_property_list_new  
                normalize.normalize_physical_property(sentence)
        elif self.paragraph_type == 1:
            for sentence in self.sentence_list:
                if sentence.valid == 0:
                    continue
                if len(sentence.pathological_property_list) == 0:
                    continue 
                normalize.normalize_physical_property(sentence)
        
    
    def extracion_all_property(self):
        self.part_extraction()
        self.pathological_property_extraction()
        self.benign_malignant_property_extracion()
        self.physical_property_extracion()