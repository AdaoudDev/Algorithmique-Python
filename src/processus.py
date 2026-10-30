class Processus:
    def __init__(self, nom, voisins):
        self.name = nom
        self.voisins = voisins
        self.statut = 1 # 1 = actif, 0 = en panne

    def envoyer(self, destinataire, contenu):
        # todo
        pass
    def decider(self, valeur):
        # todo
        pass
    def armer_minuterie(self, delai, etiquette):
        # todo
        pass


    def recevoir(self, expediteur, contenu):
        # todo réactions
        pass
    def a_la_reception(self, source, contenu):
        # todo réactions
        pass
    def a_la_minuterie(self, etiquette):
        # todo réactions
        pass




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

    