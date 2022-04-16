from patlet.fontstyle import charters


class PrettyLetter:

    def __init__(self, text: str):
        self.text = text

    def printer(self, number: int):
        result = ""
        for let in self.text:
            try:
                result += charters['style_' + str(number)]['let_' + let]
            except KeyError:
                result += f"{let}"
        print(result)

    def writer(self, number: int, filename: str = "patlet"):
        with open(f"{filename}.txt", "a") as f:
            for let in self.text:
                try:
                    f.write(charters['style_' + str(number)]['let_' + let])
                except KeyError:
                    f.write(f"{let}")
            print(f"{filename}.txt - file created")
