from typing import Optional, Any
import json

class DecisionNode:
    def __init__(self, pregunta: Any, si: Optional['DecisionNode'] = None, no: Optional['DecisionNode'] = None):
        self.pregunta: Any = pregunta
        self.si: Optional[DecisionNode] = si
        self.no: Optional[DecisionNode] = no

    def is_leaf(self):
        return self.si is None and self.no is None

class DecisionTree:
    def __init__(self, root: Optional[DecisionNode] = None):
        self.root = root
        
    def diagnose(self):
        node = self.root
        while node and not node.is_leaf():
            answer = input(f"{node.pregunta} (sí/no): ").strip().lower()
            if answer == "sí":
                node = node.si
            else:
                node = node.no
        if node:
            print(f"Diagnóstico: {node.pregunta}")
        else:
            print("No se pudo determinar un diagnóstico.")

    def postorder_traversal(self, node: Optional[DecisionNode] = None):
        if node is None:
            node = self.root
        if node is None:
            return
        
        self.postorder_traversal(node.si)
        self.postorder_traversal(node.no)
        print(node.pregunta)

