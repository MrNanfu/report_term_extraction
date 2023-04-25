from ..entity.paragrph import Paragraph
from ..entity.sentence import Sentence
class TargetSentenceLocate:
    def __init__(self, paragraph : Paragraph) -> None:
        self.paragraph = paragraph
        self.paragraph_type = paragraph.report_type
        
    def locate_target_sentence(self) -> Sentence:
        return