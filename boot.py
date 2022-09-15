import supervisor
import board
import digitalio
import storage
import usb_cdc


supervisor.set_next_stack_limit(4096 + 4096)

# disable USB storage, CDC
# see. http://kmkfw.io/docs/boot
col = digitalio.DigitalInOut(board.GP5)
row = digitalio.DigitalInOut(board.GP0)
col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
  storage.disable_usb_drive()
  usb_cdc.disable()

row.deinit()
col.deinit()
