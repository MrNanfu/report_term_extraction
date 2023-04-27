from entity.paragraph import Paragraph
from model.extraction import Extracion
from model.target_locate import TargetSentenceLocate
from model.match import Match
from entity.result import Result

def run():
    print('病理报告:')
    input0 = "1.“左乳肿物”微创旋切标本，考虑为纤维腺瘤，伴普通型增生，部分区域间质细胞增生较活跃，注意随诊观察，监测有无复发/演进。"
    print(input0)
    paragraph_0 = Paragraph(input0, 0)
    paragraph_0.convert_input_to_paragraph()
    extraction0 = Extracion(paragraph_0)
    extraction0.extracion_all_property()
    locate0 = TargetSentenceLocate(paragraph_0)
    locate0.locate_target_sentence()
    print()
    
    # ------------------------------------------------------------------------------------------------------------------
    print('超声报告:')
    input1 = "双侧乳腺内实质性结节（M1），BI-RADS 4a类。"
    print(input1)
    paragraph_1 = Paragraph(input1, 1)
    paragraph_1.convert_input_to_paragraph()
    extraction1 = Extracion(paragraph_1)
    extraction1.extracion_all_property()
    locate1 = TargetSentenceLocate(paragraph_1)
    locate1.locate_target_sentence()
    print()
    
     # ------------------------------------------------------------------------------------------------------------------
    print('匹配结果：')
    match = Match()
    result = match.match(paragraph_0, paragraph_1)
    print(result)
    
if __name__ == '__main__':
    run()

    
    

    