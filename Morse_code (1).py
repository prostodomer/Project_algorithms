# PROJECT 11
# Amangeldy Damir, Yersitov Aidyn


class Node:
    def __init__(self, value=None):
        self.value = value
        self.dot = None
        self.dash = None

class MorseCodeTree:
    def __init__(self):
        self.root = Node()
        self.codes = {
            'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
            'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
            'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
            'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
            'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
            'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
            'Y': '-.--',  'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----'
        }
        self._build_tree()

    def _build_tree(self):
        for char, code in self.codes.items():
            self._insert_code(char, code)

    def _insert_code(self, char, code):
        node = self.root
        for symbol in code:
            if symbol == '.':
                if not node.dot:
                    node.dot = Node()
                node = node.dot
            elif symbol == '-':
                if not node.dash:
                    node.dash = Node()
                node = node.dash
        node.value = char

    def getCodeSeq(self, symbol):
        for char, code in self.codes.items():
            if char == symbol.upper():
                return code
        return None

    def decode(self, code):
        node = self.root
        for symbol in code:
            if symbol == '.':
                node = node.dot
            elif symbol == '-':
                node = node.dash
            if node is None:
                return None
        return node.value if node and node.value else None

tree = MorseCodeTree()
print(tree.getCodeSeq('A'))  
print(tree.decode('.-'))     
print(tree.decode('---'))    
print(tree.decode('----'))   



def main():
    print("Enter Morse code sequences separated by spaces:")
    input_stream = input().strip().split()
    tree = MorseCodeTree()

    for code in input_stream:
        result = tree.decode(code)
        if result is None:
            print(f"Invalid Morse Code Sequence: {code}")
        else:
            print(f"Decoded: {result}")

if __name__ == "__main__":
    main()
