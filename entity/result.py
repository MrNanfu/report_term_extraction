class Result:
    def __init__(self) -> None:
        # -------------------------left--------------------------------------------------
        self.sideway_result_left = []
        self.part_result_left = []
        self.pathological_property_result_left = []
        self.benign_malignant_property_result_left = []
        self.physical_property_result_left = []
        
        self.left_result = []
        self.left_result.append(self.sideway_result_left)
        self.left_result.append(self.part_result_left)
        self.left_result.append(self.pathological_property_result_left)
        self.left_result.append(self.benign_malignant_property_result_left)
        self.left_result.append(self.physical_property_result_left)
        # ---------------------------right------------------------------------------------
        self.sideway_result_right = []
        self.part_result_right = []
        self.pathological_property_result_right = []
        self.benign_malignant_property_result_right = []
        self.physical_property_result_right = []
        
        self.right_result = []
        self.right_result.append(self.sideway_result_right)
        self.right_result.append(self.part_result_right)
        self.right_result.append(self.pathological_property_result_right)
        self.right_result.append(self.benign_malignant_property_result_right)
        self.right_result.append(self.physical_property_result_right)