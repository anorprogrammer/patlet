from .letters import charters


class PatLet:
    "PatLet nomli klass yaratamiz"""

    def __init__(self, text: str):
        """PatLet ning xususiyatlari"""
        self.text = text

    def printer(self, char: str):
        if len(char) != 1:
            for let in self.text:
                print(charters[f"let_{let.lower()}"])
        else:
            for let in self.text:
                print(charters[f"let_{let.lower()}"].replace("*", f"{char}"))

    def writer(self, char: str):
        if len(char) != 1:
            with open("patlet.txt", "a") as f:
                for let in self.text:
                    f.write(charters[f"let_{let.lower()}"])
        else:
            with open("patlet.txt", "a") as f:
                for let in self.text:
                    f.write(charters[f"let_{let.lower()}"].replace(
                        "*", f"{char}"))


###############################################################
# Coming Soon ### Coming Soon ### Coming Soon ### Coming Soon #
###############################################################

    # def liner(self):
    #     result = """"""
    #     text = self.text
    #     print(text)

        # for let in self.text:
        # letter = charters[f"let_{self.text[0].lower()}"].splitlines()
        # letter2 = charters[f"let_{self.text[1].lower()}"].splitlines()
        # letter3 = charters[f"let_{self.text[2].lower()}"].splitlines()
        # print(letter)
        # print(letter2)
        # print(letter3)
        # print(list(zip(letter, letter2, letter3)))
        # for res in list(zip(letter, letter2, letter3)):
        #     for r in res:
        #         if len(r)<15:
        #             r+=" "*(15-len(r))
        #         print(r, sep="")
        #     print(res)


# pattern = PatLet(text="Kitob")
# pattern.printer(char='3')
# pattern.liner()
