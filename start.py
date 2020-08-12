from overlay import FancyFrame
import wx, requests,json
from PyQt5 import QtCore, QtGui, QtWidgets
import time, os, json, indyTracks,sys
class MyApp(wx.App):
    def OnInit(self):
        mainWindow = MainWindow(None, -1, "iRacing Helper")
        mainWindow.Show(True)
        self.SetTopWindow(mainWindow)
        return True

class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(300,325))


from PyQt5 import QtCore, QtGui, QtWidgets


class UpdaterConfirm(object):
    def setupUi(self, Dialog, dl_url):
        Dialog.setObjectName("Dialog")
        Dialog.resize(172, 60)
        self.url = dl_url
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 30, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.download)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def download(self):
        print(self.url)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>A New Version Is Available</p></body></html>"))
def getLatest():
    current_tag = "v0.21beta"
    response = requests.get("https://api.github.com/repos/unquenchedservant/iracing-helper/releases/latest")
    data = json.loads(response.content)
    latest_tag = data['tag_name']
    if not current_tag == latest_tag:
        app = QtWidgets.QApplication(sys.argv)
        mainDialog = QtWidgets.QDialog()
        main = UpdaterConfirm()
        updater_url = data['assets'][1]['browser_download_url']
        main.setupUi(mainDialog, updater_url)
        sys.exit(mainDialog.exec_())
    else:
        return True
if __name__ == "__main__":
    '''
    import sys
    app = QtGui.QDialog(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    '''
    if getLatest():
        app = wx.App(0)
        f = FancyFrame()
        app.MainLoop()
