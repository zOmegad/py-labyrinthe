class Character:

    def __init__(self):

        self.position = {"x": 0, "y": 0}
        self.direction = ""
        self.body = "X"
        self.live = 1
        self.item_taken = 0

    def show_info(self):
        print("Nombre de vie : " + str(self.live))
        print("Nombre d'item(s) récupéré(s) : " + str(self.item_taken))