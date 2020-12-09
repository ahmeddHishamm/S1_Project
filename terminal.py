class terminal:
    def __init__(self, disp):
        self.txt = input(disp + ">")

    @property
    def get_txt(self):
        return self.txt
