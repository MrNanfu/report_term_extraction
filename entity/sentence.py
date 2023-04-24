from term import Term
class Sentence:
    """
    The structure of a sentence is ('part', 'pathological_propert1', ... 'pathological_propertN')
    """
    def __init__(self) -> None:
        self.term_list = []
        self.position_start = -1
        self.position_end = -1
        self.valid = 1   # 1 -> valid, 0 -> invalid
        self.sizeway = None # type = 1
        self.part = None    # type = 2
        self.pathological_property_list = []    # type = 3
        self.benign_malignant_property_list = []   # type = 4
        self.physical_property_list = []    # type = 5
        self.semantics_list = []    #type = 6
        self.sep_list = []      # type = 7
        self.other_list = []    # type = 8
    
    def add_term(self, term : Term = None, position_sentence : int = -1):# assume preprocess has been done to part
        if len(self.term_list) == 0:
            self.part = term.word
            self.position_start = term.position_paragraph
            if '左' in term.word:
                self.sizeway = '左' 
            if '右' in term.word:
                self.sizeway = '右' 
        term.position_sentence = position_sentence
        self.term_list.append(term)
        
    def classify_term_into_property_list(self): # assume preprocess has been done to pathological, malignant, physical
        assert len(self.term_list) >= 2
        for term in self.term_list:
            if term.type == 3:
                self.pathological_property_list.append(term)
            if term.type == 4:
                self.benign_malignant_property_list.append(term)
            if term.type == 5:
                self.physical_property_list.append(term)
            if term.type == 6:
                self.semantics_list.append(term)  
            if term.type == 7:
                  self.sep_list.append(term)      
            if term.type == 8:
                self.other_list.append(term)           
        
    def locate_position_start_end(self):
        assert len(self.term_list) >= 2
        self.position_start = self.term_list[0].position_paragraph
        position_end = -1
        for term in self.term_list:
            if term.position_paragraph > position_end:
                position_end = term.position_paragraph
        self.position_end = position_end
        
        