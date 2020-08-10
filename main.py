from overlay import FancyFrame
import wx

class MyApp(wx.App):
    def OnInit(self):
        mainWindow = MainWindow(None, -1, "iRacing Helper")
        mainWindow.Show(True)
        self.SetTopWindow(mainWindow)
        return True

class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(300,325))

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
    app = wx.App(0)
    f = FancyFrame()
    app.MainLoop()
