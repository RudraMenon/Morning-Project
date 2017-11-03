# --------------------------------------------------
#   Imports
# --------------------------------------------------
from ez_touchscreen_09 import *
from ez_ui_09 import *
import time

# --------------------------------------------------
#   Global Variables
# --------------------------------------------------
panel = None


# --------------------------------------------------
#   Event Handlers
# --------------------------------------------------
def on_checkbox_clicked(btn, release_point):
    # set the panel as a global variable
    global panel
    # set the background color of the label
    s = ''
    if panel.get_control('chk_1').value == True:
        s = s + 'X '
    else:
        s = s + 'O '
    if panel.get_control('chk_2').value == True:
        s = s + 'X '
    else:
        s = s + 'O '
    if panel.get_control('chk_3').value == True:
        s = s + 'X '
    else:
        s = s + 'O '
    if panel.get_control('chk_4').value == True:
        s = s + 'X '
    else:
        s = s + 'O '
    panel.get_control('label').text = s


# --------------------------------------------------
#   Main
# --------------------------------------------------

# Create a panel and add some buttons
panel = create_panel(0, 0, get_screen_width(), get_screen_height())
panel.add_checkbox('chk_1', 100, 50, 200, 40, text='Checkbox 1', on_click_handler=on_checkbox_clicked)
panel.add_checkbox('chk_2', 100, 100, 200, 40, text='Checkbox 2', on_click_handler=on_checkbox_clicked, value=True)
panel.add_checkbox('chk_3', 100, 150, 200, 40, text='Checkbox 3', on_click_handler=on_checkbox_clicked, value=True)
panel.add_checkbox('chk_4', 100, 200, 200, 40, text='Checkbox 4', on_click_handler=on_checkbox_clicked)
panel.add_label('label', 100, 250, 200, 100, color_border='white')

# Refresh the label
on_checkbox_clicked(None, None)

# process touches
while True:
    point = touchscreen_finger_point()
    panel.process_touch(point)
    time.sleep(0.05)	