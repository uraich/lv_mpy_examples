#!/opt/bin/lv_micropython
# change the above to the path of your lv_micropython unix binary
#
import time
#
# initialize lvgl
#
import lvgl as lv
import init_gui
from lv_colors import * 

#
# Using the background style properties
#

style=lv.style_t()
style.init()

style.set_radius(lv.STATE.DEFAULT, 5)

# Make a gradient
style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
style.set_bg_color(lv.STATE.DEFAULT, LV_COLOR_SILVER)
style.set_bg_grad_color(lv.STATE.DEFAULT, LV_COLOR_BLUE)
style.set_bg_grad_dir(lv.STATE.DEFAULT, lv.GRAD_DIR.VER)

# Shift the gradient to the bottom
style.set_bg_main_stop(lv.STATE.DEFAULT, 128)
style.set_bg_grad_stop(lv.STATE.DEFAULT, 192)


# Create an object with the new style
obj = lv.obj(lv.scr_act(), None)
obj.add_style(lv.obj.PART.MAIN, style)
obj.align(None, lv.ALIGN.CENTER, 0, 0)

while True:
    lv.task_handler()
    time.sleep_ms(10)
    