#  Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import os
import shutil
import webbrowser
import locale

from PyQt6.QtCore import Qt, QSysInfo, QSize, QProcess, QT_VERSION_STR, PYQT_VERSION_STR
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout,
                             QLabel, QSpacerItem, QSizePolicy, QCheckBox)


class welcomeui(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setFixedSize(700, 475)

        self.setWindowTitle(self.tr("Welcome Pisi Linux"))
        self.setWindowIcon(QIcon("/usr/share/pisilinux-welcome/images/pisilinux-welcome.svg"))
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("QPushButton {border: none; text-align: left; color:black;} QLabel {color:black;}")


        # The header code:

        self.headerWidget = QWidget()
        self.headerWidget.setFixedHeight(80)
        self.headerWidget.setLayout(QHBoxLayout())
        self.headerWidget.setStyleSheet("background-image: url(/usr/share/pisilinux-welcome/images/background.png);")
        self.layout().addWidget(self.headerWidget)

        self.pisiWhiteLogo = QLabel()
        self.pisiWhiteLogo.setFixedSize(64, 64)
        self.pisiWhiteLogo.setScaledContents(True)
        self.pisiWhiteLogo.setPixmap(
            QIcon("/usr/share/pisilinux-welcome/images/pisi-white.svg").pixmap(self.pisiWhiteLogo.size()))
        self.headerWidget.layout().addWidget(self.pisiWhiteLogo)

        self.pisiTextLabel = QLabel()
        self.pisiTextLabel.setFixedSize(157, 48)
        self.pisiTextLabel.setScaledContents(True)
        self.pisiTextLabel.setPixmap(QPixmap("/usr/share/pisilinux-welcome/images/pisi-text.png"))
        self.headerWidget.layout().addWidget(self.pisiTextLabel)

        self.headerWidget.layout().addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self.versionLabel = QLabel()
        font = self.versionLabel.font()
        font.setPointSize(12)
        self.versionLabel.setFont(font)
        self.versionLabel.setText(
            "KERNEL : {} - QT : {} - PYQT : {}".format(
                QSysInfo.kernelVersion(),
                QT_VERSION_STR,
                PYQT_VERSION_STR
                # QSysInfo.productVersion(),
                # QSysInfo.currentCpuArchitecture()
                ))
        self.versionLabel.setStyleSheet("color: white; font-weight: bold;")
        self.headerWidget.layout().addWidget(self.versionLabel)


        # The middle area code:

        self.contentWidget = QWidget()
        self.contentWidget.setLayout(QGridLayout())
        self.contentWidget.setContentsMargins(50, 0, 50, 50)
        self.contentWidget.setStyleSheet("background-color: white;")
        self.layout().addWidget(self.contentWidget)

        self.meetingLabel = QLabel()
        self.meetingLabel.setText(
            self.tr("Welcome to Pisi Linux!"
                    " Thank you for joining our community!\n\n"
                    "As Pisi GNU/Linux developers,"
                    " we hope you enjoy using Pisi Linux."
                    " The following links will guide you while"
                    " using Pisi Linux. Please do not"
                    " hesitate to inform about your experiences,"
                    " suggestions and errors you have encountered."))
        self.meetingLabel.setFixedHeight(150)
        self.meetingLabel.setWordWrap(True)
        font = self.meetingLabel.font()
        font.setPointSize(10)
        self.meetingLabel.setFont(font)
        self.meetingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.meetingLabel.setStyleSheet("color: black;")
        self.contentWidget.layout().addWidget(self.meetingLabel, 0, 0, 1, 3)

        self.docsHeader = QLabel()
        font = self.docsHeader.font()
        font.setPointSize(14)
        font.setBold(True)
        self.docsHeader.setFont(font)
        self.docsHeader.setAlignment(Qt.AlignmentFlag.AlignLeading)
        self.docsHeader.setText(self.tr("Documents"))
        self.contentWidget.layout().addWidget(self.docsHeader, 1, 0)
        
        self.installationDocButton = QPushButton()
        self.installationDocButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.installationDocButton.setText(self.tr("Installation Guide"))
        self.installationDocButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/guide.svg'))
        self.installationDocButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.installationDocButton, 2, 0)

        self.releaseNotesButton = QPushButton()
        self.releaseNotesButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.releaseNotesButton.setText(self.tr("Release Notes"))
        self.releaseNotesButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/info.svg'))
        self.releaseNotesButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.releaseNotesButton, 3, 0)

        self.wikiButton = QPushButton()
        self.wikiButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.wikiButton.setText(self.tr("Pisi Linux Wiki"))
        self.wikiButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/wikipedia-logo.svg'))
        self.wikiButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.wikiButton, 4, 0)

        self.supportHeader = QLabel()
        font = self.supportHeader.font()
        font.setPointSize(14)
        font.setBold(True)
        self.supportHeader.setFont(font)
        self.supportHeader.setAlignment(Qt.AlignmentFlag.AlignLeading)
        self.supportHeader.setText(self.tr("Support"))
        self.contentWidget.layout().addWidget(self.supportHeader, 1, 1)

        self.forumButton = QPushButton()
        self.forumButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.forumButton.setText(self.tr("Forum"))
        self.forumButton.setIconSize(QSize(32, 32))
        self.forumButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/forum.svg'))
        self.contentWidget.layout().addWidget(self.forumButton, 2, 1)

        self.chatButton = QPushButton()
        self.chatButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.chatButton.setText(self.tr("PisiLinux Telegram"))
        self.chatButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/chat.svg'))
        self.chatButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.chatButton, 3, 1)

        self.bugsButton = QPushButton()
        self.bugsButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.bugsButton.setText(self.tr("Pisi Linux Bugs"))
        self.bugsButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/bug.svg'))
        self.bugsButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.bugsButton, 4, 1)

        self.installationHeader = QLabel()
        font = self.installationHeader.font()
        font.setPointSize(14)
        font.setBold(True)
        self.installationHeader.setFont(font)
        self.installationHeader.setAlignment(Qt.AlignmentFlag.AlignLeading)
        self.installationHeader.setText(self.tr("Installation"))
        self.contentWidget.layout().addWidget(self.installationHeader, 1, 2)

        # TODO: Also for YALI
        self.calamaresButton = QPushButton()
        self.calamaresButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.calamaresButton.setText(self.tr("Start Installation"))
        self.calamaresButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/calamares.svg'))
        self.calamaresButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.calamaresButton, 2, 2)

        self.joinUsButton = QPushButton()
        self.joinUsButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.joinUsButton.setText(self.tr("Join Us"))
        self.joinUsButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/join_us.svg'))
        self.joinUsButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.joinUsButton, 3, 2)

        self.donateButton = QPushButton()
        self.donateButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.donateButton.setText(self.tr("Home"))
        self.donateButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/home.svg'))
        self.donateButton.setIconSize(QSize(32, 32))
        self.contentWidget.layout().addWidget(self.donateButton, 4, 2)

        self.noteLabel = QLabel()
        font = self.noteLabel.font()
        font.setPointSize(12)
        font.setBold(True)
        self.noteLabel.setFont(font)
        self.noteLabel.setText(self.tr("Note: The password is \"live\"."))
        self.noteLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # self.noteLabel.setMinimumSize(250, 50)
        # self.noteLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.contentWidget.layout().addWidget(self.noteLabel, 5, 0, 1, 3)


        # The footer code:

        self.footerWidget = QWidget()
        self.footerWidget.setFixedHeight(50)
        self.footerWidget.setLayout(QHBoxLayout())
        self.footerWidget.setStyleSheet(
            "background-image: url(/usr/share/pisilinux-welcome/images//background.png);")
        self.layout().addWidget(self.footerWidget)

        self.facebookButton = QPushButton()
        self.facebookButton.setFixedSize(36, 36)
        self.facebookButton.setIconSize(QSize(36, 36))
        self.facebookButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/facebook.svg'))
        self.facebookButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.facebookButton.setToolTip(self.tr("Facebook Page"))
        self.footerWidget.layout().addWidget(self.facebookButton)

        self.twitterButton = QPushButton()
        self.twitterButton.setFixedSize(36, 36)
        self.twitterButton.setIconSize(QSize(36, 36))
        self.twitterButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/twitter.svg'))
        self.twitterButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.twitterButton.setToolTip(self.tr("Twitter Page"))
        self.footerWidget.layout().addWidget(self.twitterButton)

        self.instagramButton = QPushButton()
        self.instagramButton.setFixedSize(36, 36)
        self.instagramButton.setIconSize(QSize(36, 36))
        self.instagramButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/instagram.svg'))
        self.instagramButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.instagramButton.setToolTip(self.tr("Instagram Page"))
        self.footerWidget.layout().addWidget(self.instagramButton)

        self.youtubeButton = QPushButton()
        self.youtubeButton.setFixedSize(36, 36)
        self.youtubeButton.setIconSize(QSize(36, 36))
        self.youtubeButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/youtube.svg'))
        self.youtubeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.youtubeButton.setToolTip(self.tr("YouTube Page"))
        self.footerWidget.layout().addWidget(self.youtubeButton)

        self.githubButton = QPushButton()
        self.githubButton.setFixedSize(36, 36)
        self.githubButton.setIconSize(QSize(36, 36))
        self.githubButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/github-logo.svg'))
        self.githubButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.githubButton.setToolTip(self.tr("Pisi Linux Repositories GitHub Page"))
        self.footerWidget.layout().addWidget(self.githubButton)

        self.footerWidget.layout().addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self.startupCheckBox = QCheckBox()
        self.startupCheckBox.setChecked(
            os.path.exists(os.path.join(os.environ["HOME"],
                                        ".config",
                                        "autostart",
                                        "pisilinux-welcome.desktop")))
        font = self.startupCheckBox.font()
        font.setBold(True)
        self.startupCheckBox.setFont(font)
        self.startupCheckBox.setText(self.tr("Show on startup"))
        self.startupCheckBox.setStyleSheet("color: white;")
        self.footerWidget.layout().addWidget(self.startupCheckBox)

        self.facebookButton.clicked.connect(self.facebookPage)
        self.twitterButton.clicked.connect(self.twitterPage)
        self.instagramButton.clicked.connect(self.instagramPage)
        self.youtubeButton.clicked.connect(self.youtubePage)
        self.githubButton.clicked.connect(self.githubPage)

        self.releaseNotesButton.clicked.connect(self.releaseNotes)
        self.wikiButton.clicked.connect(self.wikiPage)
        self.forumButton.clicked.connect(self.forumPage)
        self.chatButton.clicked.connect(self.chatPages)
        self.joinUsButton.clicked.connect(self.joinUsPage)
        self.donateButton.clicked.connect(self.homePage)
        self.startupCheckBox.clicked.connect(self.startupState)
        self.bugsButton.clicked.connect(self.issuesPage)

    def setSystem(self, type):
        if type == "live":
            self.installationDocButton.clicked.connect(self.installationDocument)

            # TODO: Also for YALI
            self.calamaresButton.clicked.connect(self.calamaresExec)

        else:
            self.installationDocButton.setText(self.tr("Pisi Guide"))
            self.installationDocButton.clicked.connect(self.installationDocument)

            self.installationHeader.setText(self.tr("Project"))

            # TODO: Also for YALI
            self.calamaresButton.setText(self.tr("Start Kaptan"))
            self.calamaresButton.setIcon(QIcon('/usr/share/pisilinux-welcome/images/kaptan.svg'))
            self.calamaresButton.clicked.connect(self.kaptanExec)

            self.noteLabel.hide()
            # self.contentWidget.layout().addItem(
            #     QSpacerItem(20, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

    def open_url(self, url):
        webbrowser.get('firefox').open(url)

    def facebookPage(self):
        self.open_url("https://www.facebook.com/Pisilinux/")

    def twitterPage(self):
        self.open_url("https://twitter.com/pisi_linux")

    def instagramPage(self):
        self.open_url("https://www.instagram.com/pisilinux_official/")

    def youtubePage(self):
        self.open_url("https://www.youtube.com/channel/UCLGSGLpxVE-vxzBuebBj3tA")

    def githubPage(self):
        self.open_url("https://github.com/pisilinux")

    def installationDocument(self):
        self.open_url("https://pisilinux.org/en/pisilinux-kurulumu/")

    def releaseNotes(self):
        if locale.getlocale()[0][:2] == "en":
            self.open_url("/usr/share/pisilinux-welcome/data/release-notes/release-notes-en.html")
        elif locale.getlocale()[0][:2] == "tr":
            self.open_url("/usr/share/pisilinux-welcome/data/release-notes/release-notes-tr.html")
        else:
            self.open_url("/usr/share/pisilinux-welcome/data/release-notes/release-notes-en.html")

    def wikiPage(self):
        self.open_url("https://pisilinux.org/wiki")

    def forumPage(self):
        self.open_url("https://pisilinux.org/forum")

    def chatPages(self):
        self.open_url("https://t.me/joinchat/MAcpp0o6E4dAAoz090cDjA")

    def joinUsPage(self):
        self.open_url("https://pisilinux.org/contact/")

    def homePage(self):
        self.open_url("https://pisilinux.org")

    # TODO: Also for YALI
    def calamaresExec(self):
        QProcess.startDetached("sudo LC_ALL=en_US calamares")

    def kaptanExec(self):
        QProcess.startDetached("kaptan")

    def issuesPage(self):
        self.open_url("https://github.com/pisilinux/main/issues/new")

    def startupState(self):
        if self.startupCheckBox.isChecked():
            try:
                shutil.copy("/usr/share/applications/pisilinux-welcome.desktop",
                            os.path.join(os.environ["HOME"],
                                         ".config", "autostart"))

            except OSError as err:
                print(err)

        else:
            try:
                os.remove(
                    os.path.join(
                        os.environ["HOME"], ".config", "autostart",
                        "pisilinux-welcome.desktop"))

            except OSError as err:
                print(err)
