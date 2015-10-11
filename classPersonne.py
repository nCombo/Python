class Personne:
    """ Classe dédissant une personne caractérisée par:
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence """

    def __init__(self, nom, prenom): #méthode constructeur

        self.nom = nom
        self.prenom = prenom
        self.age = 15
        self.lieu_residence = "Nancy"
