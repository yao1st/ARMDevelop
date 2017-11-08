import sys
import serial
from PyQt5.QtWidgets import (QMainWindow, QRadioButton, QAction, QMenu, QWidget, QMessageBox, QLineEdit,
	QDesktopWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLabel, QButtonGroup)
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont

class Window(QWidget):
	"""docstring for Window"""
	def __init__(self):
		super().__init__()
		self.ser = None
		self.com = 'com3'
		self.section = 5
		self.initUI()

	def initUI(self):
		self.resize(600, 600)
		self.center()


		buttonOpenUsart = self.createPushButton('Open USART',tip='open Usart Port, default is COM3', slot=self.USARTOpen)
		buttonCloseUsart = self.createPushButton('Close USART',tip='close existing Usart Port', slot=self.USARTClose)
		rbtnChangetoCOM1 = self.createRadioButton('COM1', tip='set USART port to COM1', slot=self.changeUsartCom)
		rbtnChangetoCOM2 = self.createRadioButton('COM2', tip='set USART port to COM2', slot=self.changeUsartCom)
		rbtnChangetoCOM3 = self.createRadioButton('COM3', tip='set USART port to COM3', slot=self.changeUsartCom)
		bg1 = QButtonGroup(self)
		bg1.addButton(rbtnChangetoCOM1, 11)
		bg1.addButton(rbtnChangetoCOM2, 12)
		bg1.addButton(rbtnChangetoCOM3, 13)

		usartLayout = QHBoxLayout()
		usartLayout.addWidget(buttonOpenUsart)
		usartLayout.addStretch(1)
		usartLayout.addWidget(buttonCloseUsart)
		usartLayout.addStretch(1)
		usartLayout.addWidget(rbtnChangetoCOM1)
		usartLayout.addWidget(rbtnChangetoCOM2)
		usartLayout.addWidget(rbtnChangetoCOM3)

		motorModeLayout = QHBoxLayout()
		djtsLabel = QLabel('Motor Test')
		djtsLabel.setFont(QFont("Roman times",10,QFont.Bold))
		rbtnTimeSync = self.createRadioButton('Time Sync', tip='all motors startup and shutdown together')
		rbtnUserVelo = self.createRadioButton('Customized Velocity', tip='User defined velocity')
		bg2 = QButtonGroup(self)
		bg2.addButton(rbtnTimeSync, 21)
		bg2.addButton(rbtnUserVelo, 22)

		motorModeLayout.addStretch(2)
		motorModeLayout.addWidget(djtsLabel)
		motorModeLayout.addStretch(1)
		motorModeLayout.addWidget(rbtnTimeSync)
		motorModeLayout.addStretch(1)
		motorModeLayout.addWidget(rbtnUserVelo)
		motorModeLayout.addStretch(2)


		motorNoLayout = QVBoxLayout()
		motorNoLayout.addWidget(QLabel('No.'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('A1'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('A2'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('A3'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('B1'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('B2'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('B3'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('C1'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('C2'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('C3'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('D1'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('D2'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('D3'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('E1'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('E2'))
		motorNoLayout.addSpacing(1)
		motorNoLayout.addStretch(1)
		motorNoLayout.addWidget(QLabel('E3'))

		motorAngleLayout = QVBoxLayout()

		angleSubmit = self.createPushButton('angle', tip='submit angle changes', slot=self.angleChanged)
		A1Angle = QLineEdit()
		A2Angle = QLineEdit()
		A3Angle = QLineEdit()
		B1Angle = QLineEdit()
		B2Angle = QLineEdit()
		B3Angle = QLineEdit()
		C1Angle = QLineEdit()
		C2Angle = QLineEdit()
		C3Angle = QLineEdit()
		D1Angle = QLineEdit()
		D2Angle = QLineEdit()
		D3Angle = QLineEdit()
		E1Angle = QLineEdit()
		E2Angle = QLineEdit()
		E3Angle = QLineEdit()
		motorAngleLayout.addWidget(angleSubmit)
		motorAngleLayout = self.addwt(motorAngleLayout, [A1Angle, A2Angle, A3Angle, B1Angle, B2Angle, B3Angle, C1Angle, C2Angle, C3Angle, D1Angle, D2Angle, D3Angle, E1Angle, E2Angle, E3Angle])

		motorSpeedLayout = QVBoxLayout()
		speedSubmit = self.createPushButton('Speed', tip='submit speed changes', slot=self.speedChanged)
		A1Speed = QLineEdit()
		A2Speed = QLineEdit()
		A3Speed = QLineEdit()
		B1Speed = QLineEdit()
		B2Speed = QLineEdit()
		B3Speed = QLineEdit()
		C1Speed = QLineEdit()
		C2Speed = QLineEdit()
		C3Speed = QLineEdit()
		D1Speed = QLineEdit()
		D2Speed = QLineEdit()
		D3Speed = QLineEdit()
		E1Speed = QLineEdit()
		E2Speed = QLineEdit()
		E3Speed = QLineEdit()
		motorSpeedLayout.addWidget(speedSubmit)
		motorSpeedLayout = self.addwt(motorSpeedLayout, [A1Speed, A2Speed, A3Speed, B1Speed, B2Speed, B3Speed, C1Speed, C2Speed, C3Speed, D1Speed, D2Speed, D3Speed, E1Speed, E2Speed, E3Speed])

		singStepZLayout = QVBoxLayout()
		stepNumZ = self.createLineEdit(placeholder='steps(+)')
		A1SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		A2SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		A3SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		B1SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		B2SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		B3SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		C1SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		C2SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		C3SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		D1SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		D2SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		D3SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		E1SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		E2SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		E3SingleStepZ = self.createPushButton(text='+', tip='move fixed steps clockwise', slot=self.singleStepZ)
		singStepZLayout.addWidget(stepNumZ)
		singStepZLayout = self.addwt(singStepZLayout, [A1SingleStepZ, A2SingleStepZ, A3SingleStepZ, 
			B1SingleStepZ, B2SingleStepZ, B3SingleStepZ, 
			C1SingleStepZ, C2SingleStepZ, C3SingleStepZ, 
			D1SingleStepZ, D2SingleStepZ, D3SingleStepZ, 
			E1SingleStepZ, E2SingleStepZ, E3SingleStepZ])

		singStepFLayout = QVBoxLayout()
		stepNumF = self.createLineEdit(placeholder='steps(-)')
		A1SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		A2SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		A3SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		B1SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		B2SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		B3SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		C1SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		C2SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		C3SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		D1SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		D2SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		D3SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		E1SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		E2SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		E3SingleStepF = self.createPushButton(text='-', tip='move fixed steps anticlockwise', slot=self.singleStepF)
		singStepFLayout.addWidget(stepNumF)
		singStepFLayout = self.addwt(singStepFLayout, [A1SingleStepF, A2SingleStepF, A3SingleStepF, 
			B1SingleStepF, B2SingleStepF, B3SingleStepF, 
			C1SingleStepF, C2SingleStepF, C3SingleStepF, 
			D1SingleStepF, D2SingleStepF, D3SingleStepF, 
			E1SingleStepF, E2SingleStepF, E3SingleStepF])


		motorLayout = QHBoxLayout()
		motorLayout.addStretch(1)
		motorLayout.addLayout(motorNoLayout)
		motorLayout.addStretch(1)
		motorLayout.addLayout(motorAngleLayout)
		motorLayout.addStretch(1)
		motorLayout.addLayout(motorSpeedLayout)
		motorLayout.addStretch(1)
		motorLayout.addLayout(singStepZLayout)
		motorLayout.addStretch(1)
		motorLayout.addLayout(singStepFLayout)
		motorLayout.addStretch(1)


		mainLayout = QVBoxLayout()
		mainLayout.addLayout(usartLayout)
		mainLayout.addLayout(motorModeLayout)
		mainLayout.addLayout(motorLayout)
		mainLayout.addStretch(1)

		self.setLayout(mainLayout)

		self.setWindowTitle('Motor Control')
		self.show()

		newLineEdit = QLineEdit()
	def createLineEdit(self, slot=None, placeholder=None):
		newLineEdit = QLineEdit()
		if slot is not None:
			newLineEdit.editingFinished.connect(slot)
		if placeholder is not None:
			newLineEdit.setPlaceholderText(placeholder)
		return newLineEdit

	def addwt(self, Layout, Wts):
		for wt in Wts:
			Layout.addStretch(1)
			Layout.addWidget(wt)
		return Layout

	def speedChanged(self):
		pass

	def angleChanged(self):
		pass

	def singleStepZ(self):
		pass

	def singleStepF(self):
		pass

	def createPushButton(self,text='Button',tip=None, slot=None):
		btn = QPushButton(text,self)
		if tip is not None:
			btn.setToolTip(tip)
		if slot is not None:
			btn.clicked.connect(slot)
		return btn

	def createRadioButton(self,text='Button',tip=None, slot=None):
		btn = QRadioButton(text, self)
		btn.setFocusPolicy(Qt.NoFocus)
		if tip is not None:
			btn.setToolTip(tip)
		if slot is not None:
			btn.toggled.connect(slot)
		return btn

	def createAction(self, text, slot=None, shortcut=None, tip=None, checkable=False):
		action = QAction(text, self)
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
		if slot is not None:
			action.triggered.connect(slot)
		if checkable:
			action.setCheckable(True)
			action.setChecked(False)
		return action

	def addActions(self, target, actions):
		for action in actions:
			if action is None:
				target.addSeperator()
			else:
				target.addAction(action)

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Warning', 
			'Are you sure to quit?',
			 QMessageBox.Yes | QMessageBox.No, 
			 QMessageBox.No)

		if reply == QMessageBox.Yes:
			if self.ser is not None:
				self.ser.close()
			event.accept()
		else:
			event.ignore()

	def USARTOpen(self):
		try:
			self.ser = serial.Serial(self.com, 115200)
			QMessageBox.information(self,'USART', 'open USART successfully')
		except Exception:
			QMessageBox.information(self,'USART', 'cannot open the USART COM')

	def USARTClose(self):
		try:
			if self.ser is not None:
				self.ser.close();
				QMessageBox.information(self,'USART', 'close USART successfully')
			QMessageBox.information(self,'USART', 'USART does not exit')
		except Exception:
			QMessageBox.information(self,'USART', 'cannot close the USART COM')

	def changeUsartCom(self):
		sender = self.sender()
		self.com = sender.text();
		if sender.isChecked():
			QMessageBox.information(self, 'USART', 'change USART Port ' + self.com)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())