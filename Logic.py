import Utils


class Logic:
    def __init__(self, level, user):
        self.game_level = level
        self.user = user
        self.curr_mistakes = 0
        self.word = ''
        self.curr_state = ''
        self.generate_word()

    def get_word(self):
        return self.word

    def generate_word(self):
        self.word = Utils.get_random_word(self.game_level, self.user)[0].upper()
        self.curr_state = '_' * len(self.word)

    def has_won(self):
        return self.word == self.curr_state

    def has_lost(self):
        return self.curr_mistakes >= 11

    def get_curr_state(self):
        return ' '.join(list(self.curr_state))

    def get_curr_mistakes(self):
        return self.curr_mistakes

    def new_letter(self, letter):
        if letter in self.word:
            temp = list(self.curr_state)
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    temp[i] = letter
            self.curr_state = ''.join(temp)
            return True
        else:
            self.curr_mistakes += 1
            return False

    def get_hint(self):
        temp = list(self.curr_state)
        for i in range(len(self.word)):
            if temp[i] == '_':
                temp[i] = self.word[i]
                break
        self.curr_state = ''.join(temp)
