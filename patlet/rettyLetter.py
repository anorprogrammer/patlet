from patlet.fontstyle import charters


class PrettyLetter:

    def __init__(self, text: str):
        self.text = text

    def style(self, number: int):
        result = ""
        for let in self.text:
            try:
                result += charters['style_' + str(number)]['let_' + let]
            except KeyError:
                result += f"{let}"
        return result
