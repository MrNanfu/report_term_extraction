from ..entity.paragrph import Paragraph
class Extracion:
    def __init__(self, paragraph : Paragraph) -> None:
        self.paragraph = paragraph
        self.paragraph_type = paragraph.report_type
    
    def part_extraction(self):
        return
    
    def pathological_property_extraction(self):
        return
    
    def benign_malignant_property_extracion(self):
        return
    
    def physical_property_extracion(self):
        return
    
    def extracion_all_property(self):
        self.part_extraction()
        self.pathological_property_extraction()
        self.benign_malignant_property_extracion()
        self.physical_property_extracion()