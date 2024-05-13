class Node:
    def __init__(self, value, code):
        self.left = None
        self.right = None
        self.value = value
        self.code = code


class BinarySearchTree:
    def __init__(self):
        self.root = Node('', '')

    def insert(self, letter, code):
        if self.root is None:
            self.root = Node(letter, code)
        else:
            current_node = self.root
            for symbol in code:
                if symbol == ".":
                    if current_node.left is None:
                        current_node.left = Node(letter, code)
                    current_node = current_node.left
                elif symbol == "-":
                    if current_node.right is None:
                        current_node.right = Node(letter, code)
                    current_node = current_node.right

    #        codigo para traducir de morse a alfabeto

    def translateMorse(self, code):
        current = self.root
        for character in code:
            if character == '.':
                current = current.left
            else:
                current = current.right
        return current.value

    def translateToAlphabet(self, frase):
        ans = ''

        frases = frase.split('/')
        for word in frases:
            word = word.split(' ')
            for i in word:
                if self.translateMorse(i).isnumeric():
                    ans += ' '
                    ans += (self.translateMorse(i))
                    ans += ' '
                else:
                    ans += (self.translateMorse(i))

            ans += ' '
        return ans


    # codigo para traducir de alfabeto a morse

    def lookup(self, node, value):
        current_node = node
        while current_node:
            if current_node.value == value:
                return current_node.code
            else:
                return self.lookup(current_node.left, value), self.lookup(current_node.right, value)

    def flatten_tuple(self, nested_tuple):
        flattened_list = []
        for item in nested_tuple:
            if isinstance(item, tuple):
                flattened_list.extend(self.flatten_tuple(item))
            elif item is not None:
                flattened_list.append(item)
        return flattened_list
    def morseOfLetter(self,letter):
        return self.flatten_tuple(self.lookup(self.root,letter))

    def translateToMorse(self, message):
        ans = ''
        for i in message:
            if i == ' ':
                ans += '/'
            else:
                ans += f'{self.morseOfLetter(i)[0]} '
        return ans






codigo_morse = {
    # primer nivel
    "e": ".", "t": "-",
    # segundo nivel
    "m": "--", "n": "-.", "i": "..", "a": ".-",
    # tercer nivel
    "s": "...", "u": "..-", "r": ".-.", "w": ".--", "d": "-..", "k": "-.-", "g": "--.", "o": "---",
    # cuarto nivel
    "b": "-...", "c": "-.-.", "f": "..-.", "h": "....",
    "j": ".---", "l": ".-..", "p": ".--.", "q": "--.-",
    "v": "...-", "x": "-..-", "y": "-.--", "z": "--..", " ": "---.", "  ": "----", "": "..--", "     ": ".-.-",
    #     quinto nivel
    "5": ".....", "4": "....-", "2": "..---", "1": ".----", "6": "-....", "7": "--...",
    '0': "-----", '9': "----.", "8": "---..", "3": "...--", "+": ".-.-.", "=": "-...-", "/": "-..-."
}

tree = BinarySearchTree()
for key, item in codigo_morse.items():
    tree.insert(key, item)


# ------------------ la creacion del arbol va hasta aqui ----------------------

#    este metodo filtra la informacion que adquirimos del metodo loopup que tiene el arbol, ya que este retornaba una lista con otras muchas listas

















print(tree.translateToMorse('hola a todos'))
print(tree.translateToAlphabet('.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- '))