import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Web_b(QMainWindow):
    def __init__(self):
        super(Web_b, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
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
        

    def navigation(self, url):
         
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
        
        
        
        
app = QApplication(sys.argv)
QApplication.setApplicationName('Jehan Kandy web VER 2')
window = Web_b()
app.exec_()