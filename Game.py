from Map import Map

class Game:

    def __init__(self):

        self.position = {"x": 0, "y": 0}
        self.finish = False

    def move(self, start_level):
        direction = input()
        direction = direction.lower()
        if direction == "d":
            self.position["y"] += 1
            if start_level[self.position["x"]][self.position["y"]] == "#":
                print(self.position["y"])
                print("Impossible d'aller ici")
                self.position["y"] -=1
            else:
                if start_level[self.position["x"]][self.position["y"]] == '=' : self.finish = True
                start_level[self.position["x"]][self.position["y"] - 1] = " "
                start_level[self.position["x"]][self.position["y"]] = "X"
        elif direction == "q":
            self.position["y"] -= 1
            if start_level[self.position["x"]][self.position["y"]] == "#":
                print(self.position["y"])
                print("Impossible d'aller ici")
                self.position["y"] +=1
            else:
                if start_level[self.position["x"]][self.position["y"]] == '=' : self.finish = True
                start_level[self.position["x"]][self.position["y"] + 1] = " "
                start_level[self.position["x"]][self.position["y"]] = "X"
        elif direction == "z":
            self.position["x"] -= 1
            if start_level[self.position["x"]][self.position["y"]] == "#":
                print(self.position["y"])
                print("Impossible d'aller ici")
                self.position["x"] +=1
            else:
                if start_level[self.position["x"]][self.position["y"]] == '=' : self.finish = True
                start_level[self.position["x"] + 1][self.position["y"]] = " "
                start_level[self.position["x"]][self.position["y"]] = "X"
        elif direction == "s":
            self.position["x"] += 1
            if start_level[self.position["x"]][self.position["y"]] == "#":
                print(self.position["y"])
                print("Impossible d'aller ici")
                self.position["x"] -=1
            else:
                if start_level[self.position["x"]][self.position["y"]] == '=' : self.finish = True
                start_level[self.position["x"] - 1][self.position["y"]] = " "
                start_level[self.position["x"]][self.position["y"]] = "X"
        else:
            print("Utilise Z Q S ou D")

    def finished(self):
        print("Felicitation vous avez finit le labyrinthe")