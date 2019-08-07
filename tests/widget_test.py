#! /usr/bin/python
# -*- coding: utf-8 -*-

# import logging
# logger = logging.getLogger(__name__)
from loguru import logger
import pytest
import os.path

path_to_script = os.path.dirname(os.path.abspath(__file__))

from __future__ import print_function

# import funkcí z jiného adresáře
import sys
import unittest
import scipy
import numpy as np
path_to_script = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path_to_script, "../src/"))
# from nose.plugins.attrib import attr

# from pysegbase import pycut
import seededitorqt
import seededitorqt.plugin
import numpy as np
from PyQt5.QtWidgets import QApplication

import pytest


class SeedEditorPluginTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     if sys.version_info.major < 3:
    #         cls.assertCountEqual = cls.assertItemsEqual
    def test_addplugin(self):
        """
        just run editor to see what is new
        Returns:
        """
        app = QApplication(sys.argv)
        data = (np.random.rand(30, 31, 32) * 100).astype(np.int)
        data[15:40, 13:20, 10:18] += 50
        se = seededitorqt.QTSeedEditor(data)
        wg0 = seededitorqt.plugin.SampleThresholdPlugin()
        se.addPlugin(wg0)
        # se.exec_()
        # self.assertTrue(False)

    # @attr("interactive")
    @pytest.mark.interactive
    # @pytest.mark.slow
    def test_show_editor(self):
        """
        just run editor to see what is new
        Returns:
        """
        app = QApplication(sys.argv)
        data = (np.random.rand(30, 31, 32) * 100).astype(np.int)
        data[15:40, 13:20, 10:18] += 50
        se = seededitorqt.QTSeedEditor(data)
        wg0 = seededitorqt.plugin.SampleThresholdPlugin()
        wg1 = seededitorqt.plugin.SampleThresholdPlugin()
        se.addPlugin(wg0)
        se.addPlugin(wg1)
        se.exec_()
        # self.assertTrue(False)

    # def test_show_draw_and_pickup_seed(self):
    #     """
    #     just run editor to see what is new
    #     Returns:
    #
    #     """
    #     app = QApplication(sys.argv)
    #     data = (np.random.rand(30,31,32) * 100).astype(np.int)
    #     data[15:40, 13:20, 10:18] += 50
    #     se = seededitorqt.QTSeedEditor(data)
    #     se.slice_box.seed_mark = 3 # seed 3
    #     se.slice_box.last_position = [1, 3]
    #     se.slice_box.drawSeeds([10, 5])
    #     se.slice_box.seed_mark = 2 #left mouse button
    #     se.slice_box.last_position = [8, 1]
    #     se.slice_box.drawSeeds([7, 5])
    #     # try to pick up seed from slice
    #     se.slice_box._pick_up_seed_label([1, 3])
    #     self.assertEqual(se.textFocusedSeedLabel, "3", "Pickuped value")
    #
    #     se.change_focus_seed_label(2)
    #     self.assertEqual(se.textFocusedSeedLabel, "2", "Changed value")
    #     # se.exec_()
    # def test_show_draw_and_pickup_segmentation_label(self):
    #     """
    #     just run editor to see what is new
    #     Returns:
    #
    #     """
    #     app = QApplication(sys.argv)
    #     data = (np.random.rand(30,31,32) * 100).astype(np.int)
    #     data[15:40, 13:20, 10:18] += 50
    #     segmentation = np.zeros_like(data)
    #     segmentation[15:40, 13:20, 10:18] = 1
    #     se = seededitorqt.QTSeedEditor(data, contours=segmentation)
    #     se.selectSlice(20)
    #     se.slice_box.seed_mark = 3 # seed 3
    #     se.slice_box.last_position = [1, 3]
    #     se.slice_box.drawSeeds([10, 5])
    #     se.slice_box.seed_mark = 2 #left mouse button
    #     se.slice_box.last_position = [8, 1]
    #     se.slice_box.drawSeeds([7, 5])
    #     # try to pick up seed from slice
    #     se.slice_box._pick_up_segmentation_label([16, 16])
    #     # self.assertEqual(se.textFocusedSeedLabel, "3", "Pickuped value")
    #     idx = se.combo_segmentation_label.currentIndex()
    #     logger.debug("idx {}".format(idx))
    #     self.assertEqual(idx, 1, "Picked up value")
    #
    #     se.change_focus_segmentation_label(0)
    #
    #     idx = se.combo_segmentation_label.currentIndex()
    #     logger.debug("idx {}".format(idx))
    #     self.assertEqual(idx, 0, "Changed value")
    #     # se.exec_()
    #
    # @attr('interactive')
    # def test_show_editor_with_too_much_wide_data(self):
    #     """
    #     just run editor to see what is new
    #     Returns:
    #
    #     """
    #     app = QApplication(sys.argv)
    #     data = (np.random.rand(30, 31, 150) * 100).astype(np.int)
    #     data[15:40, 13:20, 10:18] += 50
    #     se = seededitorqt.QTSeedEditor(data)
    #     se.exec_()
    # # @attr('interactive')
    #
    # def test_draw_seed_function(self):
    #     """
    #     just run editor to see what is new
    #     Returns:
    #
    #     """
    #     app = QApplication(sys.argv)
    #     data = (np.random.rand(30,31,32) * 100).astype(np.int)
    #     data[15:40, 13:20, 10:18] += 50
    #     se = seededitorqt.QTSeedEditor(data)
    #     se.slice_box.seed_mark = 1 #left mouse button
    #     se.slice_box.last_position = [1, 3]
    #     se.slice_box.drawSeeds([10, 5])
    #     se.slice_box.seed_mark = 2 #left mouse button
    #     se.slice_box.last_position = [8, 1]
    #     se.slice_box.drawSeeds([7, 5])
    #     # se.exec_()
    #
    # # @TODO znovu zprovoznit test
    #
    # # @unittest.skip("Cekame, az to Tomas opravi")
    # def make_data(self, sz=32, offset=0, sigma=80):
    #     seeds = np.zeros([sz, sz, sz], dtype=np.int8)
    #     seeds[offset + 12, offset + 9:offset + 14, offset + 10] = 1
    #     seeds[offset + 20, offset + 18:offset + 21, offset + 12] = 1
    #     img = np.ones([sz, sz, sz])
    #     img = img - seeds
    #
    #     seeds[
    #         offset + 3:offset + 15,
    #         offset + 2:offset + 6,
    #         offset + 27:offset + 29] = 2
    #     img = scipy.ndimage.morphology.distance_transform_edt(img)
    #     segm = img < 7
    #     img = (100 * segm + sigma * np.random.random(img.shape)).astype(np.uint8)
    #     return img, segm, seeds


if __name__ == "__main__":
    unittest.main()
