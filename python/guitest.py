import sys
import serial
from PyQt5.QtWidgets import (QMainWindow, QRadioButton, QAction, QMenu, QWidget, QMessageBox, QLineEdit,
	QDesktopWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLabel, QButtonGroup, QComboBox)
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
import struct

class Window(QWidget):
	"""docstring for Window"""
	def __init__(self):
		super().__init__()
		self.ser = None
		self.com = 'com3'
		self.section = 5
		self.baudrate = 115200
		self.MotorNum = 4
		self.initUI()

	def initUI(self):
		self.resize(600, 600)
		self.center()


		buttonOpenUsart = self.createPushButton('Open USART',tip='open Usart Port, default is COM3', slot=self.USARTOpen)
		buttonCloseUsart = self.createPushButton('Close USART',tip='close existing Usart Port', slot=self.USARTClose)
		baudChooseBox = QComboBox(self)
		baudChooseBox.addItem('115200')
		baudChooseBox.addItem('9600')
		baudChooseBox.addItem('56000')
		baudChooseBox.activated[str].connect(self.changeBaudRate)

		rbtnChangetoCOM1 = self.createRadioButton('COM1', tip='set USART port to COM1', slot=self.changeUsartCom)
		rbtnChangetoCOM2 = self.createRadioButton('COM2', tip='set USART port to COM2', slot=self.changeUsartCom)
		rbtnChangetoCOM3 = self.createRadioButton('COM3', tip='set USART port to COM3', slot=self.changeUsartCom)
		bg1 = QButtonGroup(self)
		bg1.addButton(rbtnChangetoCOM1, 11)
		bg1.addButton(rbtnChangetoCOM2, 12)
		bg1.addButton(rbtnChangetoCOM3, 13)

		usartLayout = QHBoxLayout()
		usartLayout.addStretch(1)
		usartLayout.addWidget(buttonOpenUsart)
		usartLayout.addStretch(1)
		usartLayout.addWidget(buttonCloseUsart)
		usartLayout.addStretch(1)
		usartLayout.addWidget(QLabel('Baud'))
		usartLayout.addWidget(baudChooseBox)
		usartLayout.addStretch(1)
		usartLayout.addWidget(rbtnChangetoCOM1)
		usartLayout.addWidget(rbtnChangetoCOM2)
		usartLayout.addWidget(rbtnChangetoCOM3)
		usartLayout.addStretch(1)

		btnAllTest = self.createPushButton('All Test', tip='all motors moves slightly', slot = self.alltest)
		btnStartup = self.createPushButton('Startup', tip='startup motors(after config)', slot = self.startup)
		btnShutdown = self.createPushButton('Shutdown', tip='Shutdown motors', slot = self.shutdown)
		btnZero = self.createPushButton('Zero', tip='motor moves to initial state', slot =self.zero)
		motorMainFuncLayout = QHBoxLayout()
		motorMainFuncLayout.addStretch(1)
		motorMainFuncLayout.addWidget(btnAllTest)
		motorMainFuncLayout.addStretch(1)
		motorMainFuncLayout.addWidget(btnStartup)
		motorMainFuncLayout.addStretch(1)
		motorMainFuncLayout.addWidget(btnShutdown)
		motorMainFuncLayout.addStretch(1)
		motorMainFuncLayout.addWidget(btnZero)
		motorMainFuncLayout.addStretch(1)

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
		self.AngleLineEdit = [A1Angle, A2Angle, A3Angle, B1Angle, B2Angle, B3Angle, C1Angle, C2Angle, C3Angle, D1Angle, D2Angle, D3Angle, E1Angle, E2Angle, E3Angle]


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

		motorLayout0 = QHBoxLayout()
		motorLayout0 = self.addwtorlt(motorLayout0, [QLabel('No.'), angleSubmit, speedSubmit, stepNumZ, stepNumF])
		motorLayoutA1 = QHBoxLayout()
		motorLayoutA1 = self.addwtorlt(motorLayoutA1, [QLabel('A1'), A1Angle, A1Speed, A1SingleStepZ, A1SingleStepF])
		motorLayoutA2 = QHBoxLayout()
		motorLayoutA2 = self.addwtorlt(motorLayoutA2, [QLabel('A2'), A2Angle, A2Speed, A2SingleStepZ, A2SingleStepF])
		motorLayoutA3 = QHBoxLayout()
		motorLayoutA3 = self.addwtorlt(motorLayoutA3, [QLabel('A3'), A3Angle, A3Speed, A3SingleStepZ, A3SingleStepF])
		motorLayoutB1 = QHBoxLayout()
		motorLayoutB1 = self.addwtorlt(motorLayoutB1, [QLabel('B1'), B1Angle, B1Speed, B1SingleStepZ, B1SingleStepF])
		motorLayoutB2 = QHBoxLayout()
		motorLayoutB2 = self.addwtorlt(motorLayoutB2, [QLabel('B2'), B2Angle, B2Speed, B2SingleStepZ, B2SingleStepF])
		motorLayoutB3 = QHBoxLayout()
		motorLayoutB3 = self.addwtorlt(motorLayoutB3, [QLabel('B3'), B3Angle, B3Speed, B3SingleStepZ, B3SingleStepF])
		motorLayoutC1 = QHBoxLayout()
		motorLayoutC1 = self.addwtorlt(motorLayoutC1, [QLabel('C1'), C1Angle, C1Speed, C1SingleStepZ, C1SingleStepF])
		motorLayoutC2 = QHBoxLayout()
		motorLayoutC2 = self.addwtorlt(motorLayoutC2, [QLabel('C2'), C2Angle, C2Speed, C2SingleStepZ, C2SingleStepF])
		motorLayoutC3 = QHBoxLayout()
		motorLayoutC3 = self.addwtorlt(motorLayoutC3, [QLabel('C3'), C3Angle, C3Speed, C3SingleStepZ, C3SingleStepF])
		motorLayoutD1 = QHBoxLayout()
		motorLayoutD1 = self.addwtorlt(motorLayoutD1, [QLabel('D1'), D1Angle, D1Speed, D1SingleStepZ, D1SingleStepF])
		motorLayoutD2 = QHBoxLayout()
		motorLayoutD2 = self.addwtorlt(motorLayoutD2, [QLabel('D2'), D2Angle, D2Speed, D2SingleStepZ, D2SingleStepF])
		motorLayoutD3 = QHBoxLayout()
		motorLayoutD3 = self.addwtorlt(motorLayoutD3, [QLabel('D3'), D3Angle, D3Speed, D3SingleStepZ, D3SingleStepF])
		motorLayoutE1 = QHBoxLayout()
		motorLayoutE1 = self.addwtorlt(motorLayoutE1, [QLabel('E1'), E1Angle, E1Speed, E1SingleStepZ, E1SingleStepF])
		motorLayoutE2 = QHBoxLayout()
		motorLayoutE2 = self.addwtorlt(motorLayoutE2, [QLabel('E2'), E2Angle, E2Speed, E2SingleStepZ, E2SingleStepF])
		motorLayoutE3 = QHBoxLayout()
		motorLayoutE3 = self.addwtorlt(motorLayoutE3, [QLabel('E3'), E3Angle, E3Speed, E3SingleStepZ, E3SingleStepF])

		motorLayout = QVBoxLayout()
		motorLayout = self.addwtorlt(motorLayout, [motorLayout0, motorLayoutA1, motorLayoutA2, motorLayoutA3, 
			motorLayoutB1, motorLayoutB2, motorLayoutB3, 
			motorLayoutC1, motorLayoutC2, motorLayoutC3,
			motorLayoutD1, motorLayoutD2, motorLayoutD3,
			motorLayoutE1, motorLayoutE2, motorLayoutE3], lt=True)


		mainLayout = QVBoxLayout()
		mainLayout.addLayout(usartLayout)
		mainLayout.addLayout(motorMainFuncLayout)
		mainLayout.addLayout(motorModeLayout)
		mainLayout.addLayout(motorLayout)



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

	def addwtorlt(self, Layout, Wts, lt=False):
		for i in range(0, len(Wts)):
			Layout.addStretch(1)
			if lt is False:
				Layout.addWidget(Wts[i])
			if lt is True:
				Layout.addLayout(Wts[i])
		return Layout

	def speedChanged(self):
		pass

	def angleChanged(self):
		# angleSet = []
		# for i in range(0, self.MotorNum):
		# 	# angelSet.append(float(self.AngleLineEdit[i].text()))
		# 	pass

		QMessageBox.information(self, 'Debug', 'the fist element of Angle Set is '+self.AngleLineEdit[0].text())
		print(type(self.AngleLineEdit[0].text()))
		print(float(self.AngleLineEdit[0].text()))

	def singleStepZ(self):
		pass

	def singleStepF(self):
		pass

	def alltest(self):
		pass

	def startup(self):
		command = struct.pack('>ccc', b'a', b'\r', b'\n')
		self.ser.write(command)
		print(command)

	def shutdown(self):
		pass

	def zero(self):
		pass

	def changeBaudRate(self, text):
		self.baudrate = int(text)
		QMessageBox.information(self, 'USART', 'You have changed Baud Rate to '+text)

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
			self.ser = serial.Serial(self.com, self.baudrate)
			QMessageBox.information(self,'USART', 'open USART successfully')
		except Exception:
			QMessageBox.information(self,'USART', 'cannot open the USART COM')

	def USARTClose(self):
		try:
			if self.ser is not None:
				self.ser.close();
				QMessageBox.information(self,'USART', 'close USART successfully')
			else:
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