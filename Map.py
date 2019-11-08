class Map:

    def __init__(self):

        self.start_level = []

        with open('level.txt', 'r') as level:
            lines = level.readlines()
            print("Bienvenue dans mon labyrinthe, c'est partit : \n")
            enum = 0
            for line in lines:
                x = list(line)
                x.pop()
                self.start_level.insert(enum, x)
                enum += 1

    def place_character(self, my_character):
        self.start_level[0][0] = my_character.body

    def show_level(self):
        print("\n")
        for line in self.start_level:
            print(''.join(map(str, line)))