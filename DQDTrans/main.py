import sys
# sys.path.append('..')
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
import win32api,win32con
import UIFile.UI110 as UI110
import TransAPI.baiduTransAPI as baiduTransAPI
import QQInfo.sendQQInfo as sendQQInfo

class UDTrans(QMainWindow,UI110.Ui_MainWindow,sendQQInfo.CtrlQQ):
    def __init__(self):
        # name = '小太阳'
        super(UDTrans,self).__init__()
        # 自定义的初始化函数用于初始化界面之类的！
        self.setupUi(self)
        self.pushButton.clicked.connect(self.underTrans)
        self.pushButton_23.clicked.connect(self.newsTrans)
        self.pushButton_22.clicked.connect(self.changeQQnew)
        self.pushButton_2.clicked.connect(self.invertTrans)
        self.pushButton_4.clicked.connect(self.siglezh2spa1)
        self.pushButton_5.clicked.connect(self.sigleen2spa1)
        self.pushButton_7.clicked.connect(self.siglezh2spa2)
        self.pushButton_9.clicked.connect(self.sigleen2spa2)
        self.pushButton_10.clicked.connect(self.siglezh2spa3)
        self.pushButton_12.clicked.connect(self.sigleen2spa3)
        self.pushButton_13.clicked.connect(self.siglezh2spa4)
        self.pushButton_15.clicked.connect(self.sigleen2spa4)
        self.pushButton_17.clicked.connect(self.copyText1)
        self.pushButton_18.clicked.connect(self.copyText2)
        self.pushButton_19.clicked.connect(self.copyText3)
        self.pushButton_20.clicked.connect(self.copyText4)

    def underTrans(self):
        if (self.textEdit.toPlainText()=='')and(self.textEdit_2.toPlainText()==''):
            pass
        elif (self.textEdit.toPlainText()!='')and(self.textEdit_2.toPlainText()==''):
            str = baiduTransAPI.trans(self.textEdit.toPlainText(),fromLang='spa',toLang='zh')
            self.textEdit_3.append(str)
        elif (self.textEdit.toPlainText()=='')and(self.textEdit_2.toPlainText()!=''):
            str = baiduTransAPI.trans(self.textEdit_2.toPlainText(), fromLang='spa', toLang='zh')
            self.textEdit_16.append(str)
        else:
            str1 = baiduTransAPI.trans(self.textEdit.toPlainText(), fromLang='spa', toLang='zh')
            str2 = baiduTransAPI.trans(self.textEdit_2.toPlainText(), fromLang='spa', toLang='zh')
            self.textEdit_3.append(str1)
            self.textEdit_16.append(str2)

    def newsTrans(self):
        if self.textEdit.toPlainText()=='':
            win32api.MessageBox(0, "新闻标题为空！", "警告", win32con.MB_OK)
        if self.textEdit_2.toPlainText()!='':
            self.sendQQ('小太阳', self.textEdit.toPlainText())
            str = baiduTransAPI.trans(self.textEdit_2.toPlainText(), fromLang='spa', toLang='zh')
            self.textEdit_16.append(str)

    def changeQQnew(self):
        self.sendQQ('小太阳','新闻重了！我换一个！')

    def invertTrans(self):
        if self.textEdit_6.toPlainText()!='':
            istr11 = baiduTransAPI.trans(self.textEdit_6.toPlainText(), fromLang='zh', toLang='en')
            istr12 = baiduTransAPI.trans(istr11, fromLang='en', toLang='spa')
            self.textEdit_5.append(istr11)
            self.textEdit_4.append(istr12)
        if self.textEdit_9.toPlainText()!='':
            istr21 = baiduTransAPI.trans(self.textEdit_9.toPlainText(), fromLang='zh', toLang='en')
            istr22 = baiduTransAPI.trans(istr21, fromLang='en', toLang='spa')
            self.textEdit_8.append(istr21)
            self.textEdit_7.append(istr22)
        if self.textEdit_12.toPlainText()!='':
            istr31 = baiduTransAPI.trans(self.textEdit_12.toPlainText(), fromLang='zh', toLang='en')
            istr32 = baiduTransAPI.trans(istr31, fromLang='en', toLang='spa')
            self.textEdit_11.append(istr31)
            self.textEdit_10.append(istr32)
        if self.textEdit_14.toPlainText()!='':
            istr41 = baiduTransAPI.trans(self.textEdit_14.toPlainText(), fromLang='zh', toLang='en')
            istr42 = baiduTransAPI.trans(istr41, fromLang='en', toLang='spa')
            self.textEdit_13.append(istr41)
            self.textEdit_15.append(istr42)

    def siglezh2spa1(self):
        if self.textEdit_6.toPlainText()!='':
            istr11 = baiduTransAPI.trans(self.textEdit_6.toPlainText(), fromLang='zh', toLang='en')
            istr12 = baiduTransAPI.trans(istr11, fromLang='en', toLang='spa')
            self.textEdit_5.append(istr11)
            self.textEdit_4.append(istr12)

    def sigleen2spa1(self):
        if self.textEdit_5.toPlainText() != '':
            istr12 = baiduTransAPI.trans(self.textEdit_5.toPlainText(), fromLang='en', toLang='spa')
            self.textEdit_4.append(istr12)

    def siglezh2spa2(self):
        if self.textEdit_9.toPlainText()!='':
            istr21 = baiduTransAPI.trans(self.textEdit_9.toPlainText(), fromLang='zh', toLang='en')
            istr22 = baiduTransAPI.trans(istr21, fromLang='en', toLang='spa')
            self.textEdit_8.append(istr21)
            self.textEdit_7.append(istr22)

    def sigleen2spa2(self):
        if self.textEdit_8.toPlainText() != '':
            istr22 = baiduTransAPI.trans(self.textEdit_8.toPlainText(), fromLang='en', toLang='spa')
            self.textEdit_7.append(istr22)

    def siglezh2spa3(self):
        if self.textEdit_12.toPlainText()!='':
            istr31 = baiduTransAPI.trans(self.textEdit_12.toPlainText(), fromLang='zh', toLang='en')
            istr32 = baiduTransAPI.trans(istr31, fromLang='en', toLang='spa')
            self.textEdit_11.append(istr31)
            self.textEdit_10.append(istr32)

    def sigleen2spa3(self):
        if self.textEdit_11.toPlainText() != '':
            istr32 = baiduTransAPI.trans(self.textEdit_11.toPlainText(), fromLang='en', toLang='spa')
            self.textEdit_10.append(istr32)

    def siglezh2spa4(self):
        if self.textEdit_14.toPlainText()!='':
            istr41 = baiduTransAPI.trans(self.textEdit_14.toPlainText(), fromLang='zh', toLang='en')
            istr42 = baiduTransAPI.trans(istr41, fromLang='en', toLang='spa')
            self.textEdit_13.append(istr41)
            self.textEdit_15.append(istr42)

    def sigleen2spa4(self):
        if self.textEdit_13.toPlainText() != '':
            istr42 = baiduTransAPI.trans(self.textEdit_13.toPlainText(), fromLang='en', toLang='spa')
            self.textEdit_15.append(istr42)
    # 发送QQ消息的代码放在这里会发送两次！？
    def copyText1(self):
        if self.textEdit_4.toPlainText()!='':
            clipboard = QApplication.clipboard()
            clipboard.setText(self.textEdit_4.toPlainText())
            print(self.textEdit_4.toPlainText())

    def copyText2(self):
        if self.textEdit_7.toPlainText()!='':
            clipboard = QApplication.clipboard()
            clipboard.setText(self.textEdit_7.toPlainText())
            print(self.textEdit_7.toPlainText())

    def copyText3(self):
        if self.textEdit_10.toPlainText()!='':
            clipboard = QApplication.clipboard()
            clipboard.setText(self.textEdit_10.toPlainText())
            print(self.textEdit_10.toPlainText())

    def copyText4(self):
        if self.textEdit_15.toPlainText()!='':
            clipboard = QApplication.clipboard()
            clipboard.setText(self.textEdit_15.toPlainText())
            print(self.textEdit_15.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ###################################
    # MainWindow = QMainWindow()
    # ui = textui.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    ###################################
    print('亲爱的主人您好，祝您工作顺利。')
    myui=UDTrans()
    myui.show()
    ###################################

    sys.exit(app.exec_())