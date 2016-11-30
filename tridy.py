class Zviratko:
    def __init__(self, nejake_jmeno):
        self.jmeno = nejake_jmeno

    def __str__(self):
        return '<Kotatko: {}>'.format(self.jmeno)

    def snez(self, jidlo):
        print("{}: Mnam, snedlo jsem {}".format(
            self.jmeno, jidlo))



class Kotatko(Zviratko):
    def zamnoukej(self):
        print("Mnau, ja jsem {}".format(self.jmeno))





class Stenatko(Zviratko):

    def zastekej(self):
        print("Haf, ja jsem {}".format(self.jmeno))
