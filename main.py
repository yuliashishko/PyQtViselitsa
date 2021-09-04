import sys

from PyQt5 import uic, QtGui  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup, QDialog, QMessageBox
import Utils
from Logic import Logic
from Login import Ui_Login
from game import Ui_Game
from lost import Ui_Lost
from rules import Ui_Rules
from profile import Ui_Profile
from levelchooser import Ui_LevelChooser
from won import Ui_Won

user = 'guest'


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class RegistrWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Registr.ui', self)
        self.OKButton.clicked.connect(self.createProfile)
        self.NoButton.clicked.connect(self.cansel)
        self.show()

    def createProfile(self):
        if Utils.check_login(self.login.text()):
            self.warning_label.setText("This login already in use")
            return
        if len(self.login.text()) == 0:
            self.warning_label.setText("Login field cant be empty")
            return
        if self.password.text() != self.confirmation.text():
            self.warning_label.setText("Passwords don't match")
            return
        Utils.create_account(self.name.text(), self.login.text(), self.password.text())
        self.warning_label.setText("Account is created")
        global user
        user = self.login.text()
        self.close()

    def cansel(self):
        self.close()


class RulesWindow(QMainWindow, Ui_Rules):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ProfileWindow(QMainWindow, Ui_Profile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateProfile()
        self.createButton.clicked.connect(self.createButtonClicked)
        self.deleteButton.clicked.connect(self.deleteButtonClicked)
        self.loginButton.clicked.connect(self.loginButtonClicked)
        self.logoutButton.clicked.connect(self.logoutButtonClicked)
        if user == "guest":
            self.deleteButton.setEnabled(False)
            self.logoutButton.setEnabled(False)
        else:
            self.createButton.setEnabled(False)
            self.loginButton.setEnabled(False)
        self.show()

    def loginButtonClicked(self):
        self.login = LogInWidget()
        self.setVisible(False)

    def logoutButtonClicked(self):
        global user
        user = 'guest'
        self.close()

    def deleteButtonClicked(self):
        msgBox = QMessageBox()
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setText("Are you sure?")
        result = msgBox.exec_()
        if QMessageBox.Yes == result:
            global user
            Utils.delete_user(user)
            user = 'guest'
            self.close()
        elif QMessageBox.No == result:
            self.close()

    def createButtonClicked(self):
        self.register = RegistrWidget()
        self.setVisible(False)

    def updateProfile(self):
        result = Utils.get_profile(user)
        self.name.setText(result['name'])
        self.username.setText(result['username'])
        self.level.setText(result['level'])
        self.totalExp.setText(result['totalExp'])
        self.gamesLost.setText(result['gamesLost'])
        self.gamesWon.setText(result['gamesWon'])
        self.currentExp.setText(result['currentExp'])
        self.maxExp.setText(result['maxExp'])
        self.levelProgress.setValue(result['levelProgress'])


class LogInWidget(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OKButton.clicked.connect(self.log_in)
        self.NoButton.clicked.connect(self.cansel)
        self.show()

    def log_in(self):
        if Utils.check_login(self.login.text()):
            self.warning_label.setText("Login successful")
            global user
            user = self.login.text()
        else:
            self.warning_label.setText("Account does not exist")
            return
        self.close()

    def cansel(self):
        self.close()


class LevelChooser(QMainWindow, Ui_LevelChooser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.levels = QButtonGroup()
        self.levels.addButton(self.easyButton)
        self.levels.addButton(self.hardButton)
        self.levels.addButton(self.normalButton)
        self.levels.buttonClicked.connect(self.levelClicked)
        self.show()

    def levelClicked(self, level):
        self.game = GameWindow(level.text())
        self.setVisible(False)


class WonWindow(QMainWindow, Ui_Won):
    def __init__(self, word):
        super().__init__()
        self.setupUi(self)
        path = 'resources/win.gif'
        gif = QtGui.QMovie(path)  # !!!
        self.gifLabel.setMovie(gif)
        gif.start()
        self.menuButton.clicked.connect(self.menuClicked)
        word_state = Utils.get_word_state(word)
        self.players.setText(word_state['players'])
        self.won.setText(word_state['won'])
        self.persent.setText(word_state['persent'])
        self.show()

    def menuClicked(self):
        self.menu = MenuWidget()
        self.setVisible(False)


class LostWindow(QMainWindow, Ui_Lost):
    def __init__(self, word):
        super().__init__()
        self.setupUi(self)
        path = 'resources/lost.gif'
        gif = QtGui.QMovie(path)  # !!!
        self.gifLabel.setMovie(gif)
        gif.start()
        self.menuButton.clicked.connect(self.menuClicked)
        word_state = Utils.get_word_state(word)
        self.players.setText(word_state['players'])
        self.won.setText(word_state['won'])
        self.persent.setText(word_state['persent'])
        self.show()

    def menuClicked(self):
        self.menu = MenuWidget()
        self.close()


class GameWindow(QMainWindow, Ui_Game):
    def __init__(self, level):
        super().__init__()
        self.setupUi(self)
        self.logic = Logic(level, user)
        self.letterButtonGroup = QButtonGroup()
        for i in range(32):
            button = QPushButton(chr(ord('А') + i))
            self.gridLayout.addWidget(button, i // 8, i % 8)
            self.letterButtonGroup.addButton(button)
        self.letterButtonGroup.buttonClicked.connect(self.letterClicked)
        self.hintButton.clicked.connect(self.hintButtonClicked)
        self.hintButton.setToolTip('This is a <b>Hint</b>. You can use it only once. Shows the first closed letter')
        self.updateWord()
        self.updatePicture()
        self.show()

    def hintButtonClicked(self):
        self.logic.get_hint()
        self.updateWord()
        self.hintButton.setEnabled(False)

    def updateWord(self):
        self.wordLabel.setText(self.logic.get_curr_state())

    def letterClicked(self, letter):
        if self.logic.new_letter(letter.text()):
            letter.setStyleSheet('background: rgb(0,200,0);')
            self.updateWord()
        else:
            letter.setStyleSheet('background: rgb(200,0,0);')
            self.updatePicture()
        if self.logic.has_won():
            self.setVisible(False)
            word = self.logic.get_word().lower()
            Utils.update_user_win(user, word)
            self.won = WonWindow(word)
        if self.logic.has_lost():
            self.setVisible(False)
            word = self.logic.get_word().lower()
            Utils.update_user_loose(user, word)
            self.lost = LostWindow(word)

    def updatePicture(self):
        mistakes = self.logic.get_curr_mistakes()
        self.pixmap = QPixmap(f'resources/{str(mistakes).rjust(2, "0")}.png')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.picture.resize(130, 130)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.picture.setPixmap(self.pixmap)


class MenuWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)  # Загружаем дизайн
        self.beginGameButton.clicked.connect(self.chooseLevel)
        self.profileButton.clicked.connect(self.openProfile)
        self.rulesButton.clicked.connect(self.openRules)
        # self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.show()

    def chooseLevel(self):
        self.levelChooser = LevelChooser()
        self.setVisible(False)

    def openProfile(self):
        self.profile = ProfileWindow()
        self.profile.show()

    def openRules(self):
        self.rules = RulesWindow()
        self.rules.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
