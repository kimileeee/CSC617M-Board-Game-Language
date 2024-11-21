from enum import Enum

class Colors(Enum):
    BLACK = ("#000000", "Black")
    WHITE = ("#FFFFFF", "White")
    RED = ("#FF0000", "Red")
    GREEN = ("#00FF00", "Green")
    BLUE = ("#0000FF", "Blue")
    YELLOW = ("#FFFF00", "Yellow")
    CYAN = ("#00FFFF", "Cyan")
    MAGENTA = ("#FF00FF", "Magenta")
    ORANGE = ("#FFA500", "Orange")
    PURPLE = ("#800080", "Purple")
    BROWN = ("#A52A2A", "Brown")
    GRAY = ("#808080", "Gray")
    
    def hex_code(self):
        return self.value[0]
    
    def normal_name(self):
        return self.value[1]

    def get_hex_code_by_name(normal_name):
        for color in Colors:
            if color.normal_name().lower() == normal_name.lower():
                return color.hex_code()
        return None  # Return None if no match is found