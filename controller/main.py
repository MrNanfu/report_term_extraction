from ..entity.paragrph import Paragraph
from ..model.extraction import Extracion
from ..model.target_locate import TargetSentenceLocate
if __name__ == '__main__':
    
    input0 = "“左乳肿物”①良性囊肿；②乳腺腺病，部分导管上皮增生，倾向为普通型增生，建议行免疫组化协诊排除不典型增生。※如同意做免疫组化请于工作日至外科楼二楼病理科办理相关手续。"
    print(input)
    
    paragraph_0 = Paragraph(input, 0)
    paragraph_0.convert_input_to_paragraph()
    print(paragraph_0)
    extraction0 = Extracion(paragraph_0)
    extraction0.extracion_all_property
    
    # ------------------------------------------------------------------------------------------------------------------
    input1 = "双侧乳腺内实质性结节（M1），BI-RADS 4a类。"
    print(input)
    
    paragraph_1 = Paragraph(input, 1)
    paragraph_1.convert_input_to_paragraph()
    print(paragraph_1)
    
    extraction1 = Extracion(paragraph_1)
    extraction1.extracion_all_property
    
    

    