class Term:
    def __init__(self, word : str = '', position_paragraph : int = -1,  type : int = -1) -> None:
        """
        Args:
            type: 1->sideway, 2->part, 3->pathological_property, 4->benign_malignant_property, 5->physical_property, 6->semantics, 7->sep, 8->others
        """
        self.word = word
        self.position_paragraph = position_paragraph
        self.type = type
        self.position_sentence = -1
    
    
    