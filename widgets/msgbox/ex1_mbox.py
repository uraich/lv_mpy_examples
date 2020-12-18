#!/opt/bin/lv_micropython
import lvgl as lv
import time
import display_driver

def event_handler(obj, event):
    if event == lv.EVENT.VALUE_CHANGED:
        print("Button: %s" % obj.get_active_btn_text())

btns = ["Apply", "Close", ""]

mbox1 = lv.msgbox(lv.scr_act())
mbox1.set_text("A message box with two buttons.");
mbox1.add_btns(btns)
mbox1.set_width(200)
mbox1.set_event_cb(event_handler)
mbox1.align(None, lv.ALIGN.CENTER, 0, 0)  # Align to the corner

while True:
    lv.task_handler()
    time.sleep_ms(5)
