import win32con
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from qfluentwidgets import FluentIcon
from qfluentwidgets import TextEdit, RadioButton, PrimaryPushButton, LineEdit, MessageBox, HyperlinkButton, ScrollBar
from win32clipboard import OpenClipboard, EmptyClipboard, SetClipboardData, CloseClipboard
from calculate import p_sss, p_sas, p_aas


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Triangles')

        self.h = QHBoxLayout(self)
        self.vb = QVBoxLayout(self)
        self.vbo = QVBoxLayout(self)
        self.r1h = QHBoxLayout(self)

        self.h_ea = QHBoxLayout(self)
        self.h_eb = QHBoxLayout(self)
        self.h_ec = QHBoxLayout(self)
        self.h_aa = QHBoxLayout(self)
        self.h_ab = QHBoxLayout(self)
        self.h_ac = QHBoxLayout(self)

        self.r_sss = RadioButton('SSS', self)
        self.r_sss.setChecked(True)
        self.r_sas = RadioButton('SAS', self)
        self.r_aas = RadioButton('AAS', self)

        self.l_ea = QLabel('Edge a =', self)
        self.l_ea.setFont(QFont("Microsoft YaHei UI", 10))
        self.l_eb = QLabel('Edge b =', self)
        self.l_eb.setFont(QFont("Microsoft YaHei UI", 10))
        self.l_ec = QLabel('Edge c =', self)
        self.l_ec.setFont(QFont("Microsoft YaHei UI", 10))
        self.l_aa = QLabel('∠A (°) =', self)
        self.l_aa.setFont(QFont("Microsoft YaHei UI", 10))
        self.l_ab = QLabel('∠B (°) =', self)
        self.l_ab.setFont(QFont("Microsoft YaHei UI", 10))
        self.l_ac = QLabel('∠C (°) =', self)
        self.l_ac.setFont(QFont("Microsoft YaHei UI", 10))

        self.l_r = TextEdit(self)
        self.l_r.setFont(QFont("Microsoft YaHei UI", 13))
        self.l_r.setText('There is nothing to show.\nPlease input something.')
        self.scb = ScrollBar(Qt.Vertical, self.l_r)

        self.e_ea = LineEdit(self)
        self.e_eb = LineEdit(self)
        self.e_ec = LineEdit(self)
        self.e_aa = LineEdit(self)
        self.e_ab = LineEdit(self)
        self.e_ac = LineEdit(self)

        self.pb = PrimaryPushButton('Process', self)
        self.lb = HyperlinkButton(url='https://github.com/Unqualified-Developers/Triangles', text='Source Code Repository', icon=FluentIcon.GITHUB)

        self.r_sss.clicked.connect(self.sss_c)
        self.r_sas.clicked.connect(self.sas_c)
        self.r_aas.clicked.connect(self.aas_c)
        self.pb.clicked.connect(self.process)

        self.r1h.addWidget(self.r_sss)
        self.r1h.addWidget(self.r_sas)
        self.r1h.addWidget(self.r_aas)
        self.h_ea.addWidget(self.l_ea)
        self.h_ea.addWidget(self.e_ea)
        self.h_eb.addWidget(self.l_eb)
        self.h_eb.addWidget(self.e_eb)
        self.h_ec.addWidget(self.l_ec)
        self.h_ec.addWidget(self.e_ec)
        self.h_aa.addWidget(self.l_aa)
        self.h_aa.addWidget(self.e_aa)
        self.h_ab.addWidget(self.l_ab)
        self.h_ab.addWidget(self.e_ab)
        self.h_ac.addWidget(self.l_ac)
        self.h_ac.addWidget(self.e_ac)

        self.vb.addLayout(self.r1h)
        self.vb.addLayout(self.h_ea)
        self.vb.addLayout(self.h_eb)
        self.vb.addLayout(self.h_ec)
        self.vb.addLayout(self.h_aa)
        self.vb.addLayout(self.h_ab)
        self.vb.addLayout(self.h_ac)

        self.vbo.addWidget(self.l_r)
        self.vb.addWidget(self.pb)
        self.vb.addWidget(self.lb)
        self.h.addLayout(self.vb)
        self.h.addWidget(QLabel(" "))
        self.h.addLayout(self.vbo)

        self.e_aa.setEnabled(False)
        self.e_ab.setEnabled(False)
        self.e_ac.setEnabled(False)

    def sss_c(self):
        self.e_aa.setEnabled(False)
        self.e_ab.setEnabled(False)
        self.e_ac.setEnabled(False)
        self.e_ea.setEnabled(True)
        self.e_eb.setEnabled(True)
        self.e_ec.setEnabled(True)

    def sas_c(self):
        self.e_aa.setEnabled(False)
        self.e_ab.setEnabled(False)
        self.e_ac.setEnabled(True)
        self.e_ea.setEnabled(True)
        self.e_eb.setEnabled(True)
        self.e_ec.setEnabled(False)

    def aas_c(self):
        self.e_aa.setEnabled(True)
        self.e_ab.setEnabled(True)
        self.e_ac.setEnabled(False)
        self.e_ea.setEnabled(True)
        self.e_eb.setEnabled(False)
        self.e_ec.setEnabled(False)

    def process(self):
        try:
            if self.r_sss.isChecked():
                self.l_r.setText(p_sss(float(self.e_ea.text()), float(self.e_eb.text()), float(self.e_ec.text())))
            elif self.r_sas.isChecked():
                self.l_r.setText(p_sas(float(self.e_ea.text()), float(self.e_ac.text()), float(self.e_eb.text())))
            elif self.r_aas.isChecked():
                self.l_r.setText(p_aas(float(self.e_aa.text()), float(self.e_ab.text()), float(self.e_ea.text())))
        except ValueError:
            m = MessageBox("Process", "This is not a triangle.", self)
            m.exec_()
