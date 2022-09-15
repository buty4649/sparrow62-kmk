from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import kmk.extensions.keymap_extras.keymap_jp

layer1 = 0
layer2 = 1

____ = KC.TRANSPARENT

mo_layer2 = KC.MO(layer2)
kc_paste = KC.LSFT(KC.INS)
KC.BSLS = KC.INT3

def layer1_keymap(keyboard: KMKKeyboard):
    left = [
        [KC.ESC,    KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,     kc_paste],
        [           KC.LCTL,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,     KC.CIRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,     KC.LBRC],
        [                                               KC.CAPS,    mo_layer2,  KC.LGUI,  KC.ENT],
    ]
    right = [
        [           KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS],
        [KC.PSCR,   KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.AT],
        [KC.BSLS,   KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.COLN],
        [KC.RBRC,   KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.UNDS],
        [KC.SPC,    KC.BSPC,    KC.RCTL,    mo_layer2],
    ]

    return [[left, right]]

def layer2_keymap(keyboard: KMKKeyboard):
    left = [
        [____,      ____,       KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5],
        [           ____,       ____,       ____,       ____,       ____,       ____,       KC.F6],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           KC.LSHIFT,  ____,       ____,       ____,       ____,       ____,       ____],
        [                                               ____,       ____,       KC.LGUI,    ____],
    ]
    right = [
        [           KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12],
        [____,      ____,       KC.PGDN,    KC.PGUP,    ____,       ____,       ____],
        [____,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   ____,       ____],
        [____,      KC.HOME,    ____,       ____,       KC.END,     ____,       ____],
        [____,      KC.DEL,     ____,       ____],
    ]

    return [[left, right]]

def get_keymap(keyboard: KMKKeyboard):
    layer1 = layer1_keymap(keyboard)
    layer2 = layer2_keymap(keyboard)
    return [layer1[0], layer2[0]]

def on_before_start(keyboard: KMKKeyboard):
    keyboard.pixels.set_rgb_fill((2, 2, 2))
