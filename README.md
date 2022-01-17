# Web-Browser-VER-2
Web Browser VER 2
<br>
1. you have to install pyinstaller module <br>
2. then install PyQt5 module
3. and install PyQtwebEngine


<br>
you can download code from here (From My GitHub)
<br> and you can Download .exe file 
<br> this link 
https://www.mediafire.com/file/c46yg54l97ras31/JK_web2.exe/file
<br><br><br>
About the Code 
<br><br>
import sys<br>
from PyQt5.QtCore import *<br>
from PyQt5.QtWidgets import *<br>
from PyQt5.QtWebEngineWidgets import *<br>


#Create a Class for Web Browser for creat the web  browser<br><br>
class Web_b(QMainWindow):<br>
    def __init__(self):<br>
        super(Web_b, self).__init__()<br>
        self.browser = QWebEngineView()<br>
        self.browser.setUrl(QUrl('http://www.google.com'))<br>
        self.setCentralWidget(self.browser)<br>
        self.showMaximized()<br>
        
        #navigetion bar
        jk_nav = QToolBar()
        self.addToolBar(jk_nav)
        
        #back button
        jk_back = QAction('Back', self)
        jk_back.triggered.connect(self.browser.back)
        jk_nav.addAction(jk_back)
        
        #forward button
        jk_forward = QAction('Forword', self)
        jk_forward.triggered.connect(self.browser.forward)
        jk_nav.addAction(jk_forward)
        
        #reload button
        jk_reload = QAction('Reload', self)
        jk_reload.triggered.connect(self.browser.reload)
        jk_nav.addAction(jk_reload)
        
        #home button
        jk_home = QAction('Home', self)
        jk_home.triggered.connect(self.jk_go_home)
        jk_nav.addAction(jk_home)
    
        #url
        self.jk_url = QLineEdit()
        self.jk_url.returnPressed.connect(self.jk_nevigate_to)
        jk_nav.addWidget(self.jk_url)
    
        #update url
        self.browser.urlChanged.connect(self.jk_update_url)
        
    def jk_go_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def jk_nevigate_to(self):
        jk_get_url = self.jk_url.text()
        self.browser.setUrl(QUrl(jk_get_url))
        
    def jk_update_url(self,j):
        self.jk_url.setText(j.toString())
        
       
        
#____________For RUN the Application_______________     
app = QApplication(sys.argv)
#application Name
QApplication.setApplicationName('Jehan Kandy web VER 2')
window = Web_b()
#run the application
app.exec_()
