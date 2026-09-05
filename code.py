import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

class Stenokeyboard(KMKKeyboard):

    def __init__(self):
        super().__init__()

        self.col_pins = (
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
    )
        self.row_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
    )

        self.keymap = [ 
        [  #LAYER 0 - STENO
            KC.NO, KC.S, KC.T, KC.P, KC.H, KC.NO, KC.NO, KC.F, KC.P, KC.L, KC.T, KC.D,

            KC.NO, KC.S, KC.K, KC.W, KC.R, KC.NO, KC.NO, KC.R, KC.B, KC.G, KC.S, KC.Z,

            KC.TG(1), KC.LSHIFT, KC.LCTRL, KC.LALT, KC.LGUI, KC.SPACE, KC.VOL_DOWN, KC.LEFT, KC.UP, KC.DOWN, KC.RIGHT, KC.VOL_UP,

            KC.NO, KC.NO, KC.NO, KC.NO, KC.A, KC.O, KC.E, KC.NO, KC.NO, KC.NO, KC.NO,
            ],

        [   #LAYER 1 - QWERTY
            KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,

            KC.LCTRL, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.COMMA,

            KC.TG(0), KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLSH, KC.ENT,

            KC.NO, KC.NO, KC.NO, KC.LGUI, KC.MO(2), KC.LSHIFT, KC.SPACE, KC.MO(3), KC.LALT, KC.NO, KC.NO, KC.NO,
            ],

        [   #LAYER 2 - NUMBERS
            KC.NO, KC.1, KC.2, KC.3, KC.4, KC.5, KC.6, KC.7, KC.8, KC.9, KC.0, KC.NO,

            KC.TAB, KC.NO, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

            KC.NO, KC.NO, KC.DEL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

            KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
            ],

        [   #LAYER 3 - SYMBOLS
            KC.NO, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC, KC.CARET, KC.AMPERSAND,KC.ASTR, KC.LPRN, KC.RPRN, KC.NO,

            KC.NO, KC.NO, KC.MUTE, KC.VOL_DOWN, KC.VOL_UP, KC.NO, KC.MINUS, KC.EQUAL, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.BTICK,

            KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE, KC.TILD,

            KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
            ],

        ]

#OLED?
        self.enable_oleds = True
        self.oled_sda = [board.GP16]
        self.oled_scl = [board.GP17]
        self.oled_width = [128]
        self.oled_height = [32]
        self.oled_count = 1
        self.make_oleds()

keyboard = Stenokeyboard()
keyboard.go()

