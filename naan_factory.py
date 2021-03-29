
class NaanFactory:

    def make(self, water, flour):
        if water == "water":
            if flour == "flour":
                return "dough"

    def bake(self, dough):
        if dough == "dough":
            return "naan"

    def run_fact(self, water, flour):
        if water == "water":
            if flour == "flour":
                return "naan"
