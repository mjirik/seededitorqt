#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sample widget for pyqt editor

"""
import logging
logger = logging.getLogger(__name__)

from PyQt4 import QtGui, QtCore
import numpy as np

class QTSeedEditorWidget(QtGui.QWidget):

    def __init__(self):
        super(QTSeedEditorWidget, self).__init__()

        self.data3d = None
        self.segmentation = None
        self.seeds = None
        self.voxelsize_mm = None
        self.run_callback = None

        self.initUI()
        self.updateUI()

    def setRunCallback(self, run_callback):
        """
        Define callback function called on run funcion.
        This function cam be used to update parent editor.

        :param run_callback: Function signature: fcn(widget, io3d, segmentation, seeds, voxelsize_mm)

        :return:
        """
        self.run_callback = run_callback

    def run(self):
        self.segmentation = self.data3d > self.slider.value()
        if self.run_callback is not None:
            self.run_callback(self, self.data3d, self.segmentation, self.seeds, self.voxelsize_mm)


    # def get_data3d(self):
    #     return self.data3d
    #
    # def get_seeds(self):
    #     return self.seeds
    #
    # def get_segmentation(self):
    #     return self.segmentation

    def updateUI(self):
        if self.data3d is not None:
            self.slider.setRange(np.min(self.data3d), np.max(self.data3d))

    def initUI(self):
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.runbutton = QtGui.QPushButton("Set")
        self.runbutton.clicked.connect(self.run)

        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.slider)
        self.vbox.addWidget(self.runbutton)

