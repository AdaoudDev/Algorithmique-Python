class Reseau:
    def __init__(self, processus, graine, delai_max):
        self.processus = processus
        self.graine = graine
        self.delai_max = delai_max
        self.file_evenements = []
        self.messages = 0
        self.pannes = []
        

    def executer(self, initiateurs):
        # todo
        pass