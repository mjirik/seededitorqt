#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sample widget for pyqt editor
"""
from loguru import logger
# import logging
#
# logger = logging.getLogger(__name__)
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class QtSEdPlugin(QtWidgets.QWidget):
    def __init__(self):
        super(QtSEdPlugin, self).__init__()
        self.data3d = None
        self.segmentation = None
        self.seeds = None
        self.voxelsize_mm = None
        self.run_callback = None
        self.get_callback = None
        self.get_data_from_parent_callback = None
        self.show_status_callback = None
        self.general_initUI()

    def updateDataFromParent(self):
        if self.get_data_from_parent_callback is not None:
            data3d, segmentation, seeds, voxelsize_mm = (
                self.get_data_from_parent_callback()
            )
            self.setData(data3d, segmentation, seeds, voxelsize_mm)

    def setData(self, data3d, segmentation, seeds, voxelsize_mm):
        self.data3d = data3d
        self.segmentation = segmentation
        self.seeds = seeds
        self.voxelsize_mm = voxelsize_mm

    def setShowStatusCallback(self, show_status_callback):
        self.show_status_callback = show_status_callback

    def showStatus(self, msg):
        if self.show_status_callback is not None:
            self.show_status_callback(msg)
        else:
            logger.info(msg)

    def setGetDataFromParentCallback(self, get_data_from_parent_callback):
        """
        Define callback function called on run funcion.
        This function cam be used to update parent editor.
        :param input_data_callback: Function signature: io3d, segmentation, seeds, voxelsize_mm = fcn()
        :return:
        """
        self.get_data_from_parent_callback = get_data_from_parent_callback

    def setRunCallback(self, run_callback):
        """
        Define callback function called on run funcion.
        This function cam be used to update parent editor.
        :param run_callback: Function signature: fcn(widget, io3d, segmentation, seeds, voxelsize_mm)
        :return:
        """
        self.run_callback = run_callback

    def runInit(self):
        self.updateDataFromParent()

    def runFinish(self):
        if self.run_callback is not None:
            self.run_callback(
                self, self.data3d, self.segmentation, self.seeds, self.voxelsize_mm
            )

    def run(self):
        self.runInit()
        # self.segmentation = self.data3d > self.slider.value()
        self.runFinish()

    def general_initUI(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)


class SampleThresholdPlugin(QtSEdPlugin):
    def __init__(self):
        super(SampleThresholdPlugin, self).__init__()
        self.initUI()
        self.updateUI()

    def initUI(self):
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.runbutton = QtWidgets.QPushButton("Set")
        self.runbutton.clicked.connect(self.run)
        self.vbox.addWidget(self.slider)
        self.vbox.addWidget(self.runbutton)

    def updateUI(self):
        if self.data3d is not None:
            self.slider.setRange(np.min(self.data3d), np.max(self.data3d))

    def run(self):
        self.runInit()
        self.segmentation = self.data3d > self.slider.value()
        self.showStatus("Value {}".format(self.slider.value()))
        self.runFinish()
