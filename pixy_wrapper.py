import pixy 
from ctypes import *
from pixy import *
# from __future__ import print_function

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]


class PixyWrapper:
    def __init__(self, block_len):
        pixy.init()
        pixy.change_prog("color_connected_components")
        self.block_len = block_len
        self.blocks = BlockArray(self.block_len)
        self.frame = 0

    def get_blocks(self):
        count = pixy.ccc_get_blocks(self.block_len, self.blocks)

        if count > 0:
            # print('frame %3d:' % (self.frame))
            self.frame = self.frame + 1
            # for index in range (0, count):
                # print('[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (self.blocks[index].m_signature, self.blocks[index].m_x, self.blocks[index].m_y, self.blocks[index].m_width, self.blocks[index].m_height))
            return self.blocks[0].m_x, self.blocks[0].m_y
        return None

    def get_cam_frame(self):
        return pixy.get_frame_width(), pixy.get_frame_height()

    def get_dist_from_cam_center(self):
        block_x, block_y = self.get_blocks()
        frame_width, frame_height = self.get_cam_frame()

        x_displacement = block_x - (frame_width/2)
        y_displacement = block_y - (frame_height/2)

        return x_displacement, y_displacement
