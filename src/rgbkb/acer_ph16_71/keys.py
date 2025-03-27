from enum import Enum


class KeyNames(Enum):
    A_KEY = 'a_key'
    ALT_L = 'alt_l'
    ALT_R = 'alt_r'
    APOSTROPHE = 'apostrophe'
    B_KEY = 'b_key'
    BACKSLASH = 'backslash'
    BACKSPACE = 'backspace'
    BACKTICK = 'backtick'
    C_KEY = 'c_key'
    CAPS_LOCK = 'capslock'
    COMMA = 'comma'
    CTRL_L = 'ctrl_l'
    CTRL_R = 'ctrl_r'
    D_KEY = 'd_key'
    DASH = 'dash'
    DELETE = 'delete'
    DOT = 'dot'
    DOWN_ARROW = 'down_arrow'
    E_KEY = 'e_key'
    ENTER = 'enter'
    EQUAL = 'equal'
    ESCAPE = 'escape'
    F1 = 'f1'
    F2 = 'f2'
    F3 = 'f3'
    F4 = 'f4'
    F5 = 'f5'
    F6 = 'f6'
    F7 = 'f7'
    F8 = 'f8'
    F9 = 'f9'
    F10 = 'f10'
    F11 = 'f11'
    F12 = 'f12'
    F_KEY = 'f_key'
    FAST_FORWARD = 'fast_forward'
    FN = 'fn'
    G_KEY = 'g_key'
    H_KEY = 'h_key'
    I_KEY = 'i_key'
    INSERT = 'insert'
    J_KEY = 'j_key'
    K_KEY = 'k_key'
    KP_0 = 'kp_0'
    KP_1 = 'kp_1'
    KP_2 = 'kp_2'
    KP_3 = 'kp_3'
    KP_4 = 'kp_4'
    KP_5 = 'kp_5'
    KP_6 = 'kp_6'
    KP_7 = 'kp_7'
    KP_8 = 'kp_8'
    KP_9 = 'kp_9'
    KP_ASTERISK = 'kp_asterisk'
    KP_DOT = 'kp_dot'
    KP_ENTER = 'kp_enter'
    KP_FORWARD_SLASH = 'kp_forward_slash'
    KP_MINUS = 'kp_minus'
    KP_PLUS = 'kp_plus'
    L_KEY = 'l_key'
    LEFT_ARROW = 'left_arrow'
    LEFT_BRACKET = 'left_bracket'
    M_KEY = 'm_key'
    MENU = 'menu'
    N_KEY = 'n_key'
    NUM_LOCK = 'num_lock'
    NUMBER_ROW_0 = 'number_row_0'
    NUMBER_ROW_1 = 'number_row_1'
    NUMBER_ROW_2 = 'number_row_2'
    NUMBER_ROW_3 = 'number_row_3'
    NUMBER_ROW_4 = 'number_row_4'
    NUMBER_ROW_5 = 'number_row_5'
    NUMBER_ROW_6 = 'number_row_6'
    NUMBER_ROW_7 = 'number_row_7'
    NUMBER_ROW_8 = 'number_row_8'
    NUMBER_ROW_9 = 'number_row_9'
    O_KEY = 'o_key'
    P_KEY = 'p_key'
    PLAY_PAUSE = 'play_pause'
    POWER = 'power'
    PREDATOR = 'predator'
    PRINT_SCREEN = 'print_screen'
    Q_KEY = 'q_key'
    R_KEY = 'r_key'
    REWIND = 'rewind'
    RIGHT_ARROW = 'right_arrow'
    RIGHT_BRACKET = 'right_bracket'
    S_KEY = 's_key'
    SEMICOLON = 'semicolon'
    SHIFT_L = 'shift_l'
    SHIFT_R = 'shift_r'
    SLASH = 'slash'
    SPACE = 'space'
    T_KEY = 't_key'
    TAB = 'tab'
    U_KEY = 'u_key'
    UP_ARROW = 'up_arrow'
    V_KEY = 'v_key'
    W_KEY = 'w_key'
    WIN = 'win'
    X_KEY = 'x_key'
    Y_KEY = 'y_key'
    Z_KEY = 'z_key'


class GroupNames(Enum):
    ALL = "all"
    LETTERS = "letters"
    F_KEYS = "f_keys"
    NUMBER_ROW = "number_row"
    WASD_KEYS = "wasd_keys"
    ARROW_KEYS = "arrow_keys"
    NUMPAD_NUMBERS = "numpad_numbers"
    MEDIA_KEYS = "media_keys"
    MODIFIER_KEYS = "modifier_keys"


KEY_GROUPS: dict[GroupNames, tuple[KeyNames, ...]] = {
    GroupNames.ALL: tuple(KeyNames),
    GroupNames.LETTERS: (
        KeyNames.A_KEY,
        KeyNames.B_KEY,
        KeyNames.C_KEY,
        KeyNames.D_KEY,
        KeyNames.E_KEY,
        KeyNames.F_KEY,
        KeyNames.G_KEY,
        KeyNames.H_KEY,
        KeyNames.I_KEY,
        KeyNames.J_KEY,
        KeyNames.K_KEY,
        KeyNames.L_KEY,
        KeyNames.M_KEY,
        KeyNames.N_KEY,
        KeyNames.O_KEY,
        KeyNames.P_KEY,
        KeyNames.Q_KEY,
        KeyNames.R_KEY,
        KeyNames.S_KEY,
        KeyNames.T_KEY,
        KeyNames.U_KEY,
        KeyNames.V_KEY,
        KeyNames.W_KEY,
        KeyNames.X_KEY,
        KeyNames.Y_KEY,
        KeyNames.Z_KEY
    ),
    GroupNames.F_KEYS: (
        KeyNames.F1,
        KeyNames.F2,
        KeyNames.F3,
        KeyNames.F4,
        KeyNames.F5,
        KeyNames.F6,
        KeyNames.F7,
        KeyNames.F8,
        KeyNames.F9,
        KeyNames.F10,
        KeyNames.F11,
        KeyNames.F12
    ),
    GroupNames.NUMBER_ROW: (
        KeyNames.NUMBER_ROW_1,
        KeyNames.NUMBER_ROW_2,
        KeyNames.NUMBER_ROW_3,
        KeyNames.NUMBER_ROW_4,
        KeyNames.NUMBER_ROW_5,
        KeyNames.NUMBER_ROW_6,
        KeyNames.NUMBER_ROW_7,
        KeyNames.NUMBER_ROW_8,
        KeyNames.NUMBER_ROW_9,
        KeyNames.NUMBER_ROW_0
    )
    ,
    GroupNames.WASD_KEYS: (
        KeyNames.W_KEY,
        KeyNames.A_KEY,
        KeyNames.S_KEY,
        KeyNames.D_KEY
    ),
    GroupNames.ARROW_KEYS: (
        KeyNames.LEFT_ARROW,
        KeyNames.UP_ARROW,
        KeyNames.RIGHT_ARROW,
        KeyNames.DOWN_ARROW
    ),
    GroupNames.NUMPAD_NUMBERS: (
        KeyNames.KP_0,
        KeyNames.KP_1,
        KeyNames.KP_2,
        KeyNames.KP_3,
        KeyNames.KP_4,
        KeyNames.KP_5,
        KeyNames.KP_6,
        KeyNames.KP_7,
        KeyNames.KP_8,
        KeyNames.KP_9
    ),
    GroupNames.MEDIA_KEYS: (
        KeyNames.PLAY_PAUSE,
        KeyNames.REWIND,
        KeyNames.FAST_FORWARD
    ),
    GroupNames.MODIFIER_KEYS: (
        KeyNames.CTRL_L,
        KeyNames.ALT_L,
        KeyNames.SHIFT_L,
        KeyNames.CTRL_R,
        KeyNames.ALT_R,
        KeyNames.SHIFT_R
    )
}

# indexes with seemingly no keys:
# 7,8,9,14,30,36,42,48,54,66,79,
# 87,88,91.92.93,94,97,98,113,119,
# 121,125,126,127
KEYS: tuple[tuple[KeyNames, int, int, int], ...] = (
    # KeyName,Row, Col, PayloadIndex
    (KeyNames.CTRL_L, 0, 0, 0),
    (KeyNames.FN, 0, 1, 6),
    (KeyNames.WIN, 0, 2, 12),
    (KeyNames.ALT_L, 0, 3, 18),
    (KeyNames.SPACE, 0, 4, 24),
    (KeyNames.ALT_R, 0, 5, 60),
    (KeyNames.MENU, 0, 6, 72),
    (KeyNames.CTRL_R, 0, 7, 78),
    (KeyNames.LEFT_ARROW, 0, 8, 84),
    (KeyNames.DOWN_ARROW, 0, 9, 96),
    (KeyNames.RIGHT_ARROW, 0, 10, 102),
    (KeyNames.KP_0, 0, 11, 108),
    (KeyNames.KP_DOT, 0, 12, 114),
    (KeyNames.KP_ENTER, 0, 13, 120),
    (KeyNames.SHIFT_L, 1, 0, 1),
    (KeyNames.Z_KEY, 1, 1, 19),
    (KeyNames.X_KEY, 1, 2, 25),
    (KeyNames.C_KEY, 1, 3, 31),
    (KeyNames.V_KEY, 1, 4, 37),
    (KeyNames.B_KEY, 1, 5, 43),
    (KeyNames.N_KEY, 1, 6, 49),
    (KeyNames.M_KEY, 1, 7, 55),
    (KeyNames.COMMA, 1, 8, 61),
    (KeyNames.DOT, 1, 9, 67),
    (KeyNames.SLASH, 1, 10, 73),
    (KeyNames.SHIFT_R, 1, 11, 85),
    (KeyNames.UP_ARROW, 1, 12, 90),
    (KeyNames.KP_1, 1, 13, 100),
    (KeyNames.KP_2, 1, 14, 109),
    (KeyNames.KP_3, 1, 15, 115),
    (KeyNames.CAPS_LOCK, 2, 0, 2),
    (KeyNames.A_KEY, 2, 1, 20),
    (KeyNames.S_KEY, 2, 2, 26),
    (KeyNames.D_KEY, 2, 3, 32),
    (KeyNames.F_KEY, 2, 4, 38),
    (KeyNames.G_KEY, 2, 5, 44),
    (KeyNames.H_KEY, 2, 6, 50),
    (KeyNames.J_KEY, 2, 7, 56),
    (KeyNames.K_KEY, 2, 8, 62),
    (KeyNames.L_KEY, 2, 9, 68),
    (KeyNames.SEMICOLON, 2, 10, 74),
    (KeyNames.APOSTROPHE, 2, 11, 80),
    (KeyNames.ENTER, 2, 12, 86),
    (KeyNames.KP_4, 2, 13, 101),
    (KeyNames.KP_5, 2, 14, 110),
    (KeyNames.KP_6, 2, 15, 116),
    (KeyNames.KP_PLUS, 2, 16, 122),
    (KeyNames.TAB, 3, 0, 3),
    (KeyNames.Q_KEY, 3, 1, 15),
    (KeyNames.W_KEY, 3, 2, 21),
    (KeyNames.E_KEY, 3, 3, 27),
    (KeyNames.R_KEY, 3, 4, 33),
    (KeyNames.T_KEY, 3, 5, 39),
    (KeyNames.Y_KEY, 3, 6, 45),
    (KeyNames.U_KEY, 3, 7, 51),
    (KeyNames.I_KEY, 3, 8, 57),
    (KeyNames.O_KEY, 3, 9, 63),
    (KeyNames.P_KEY, 3, 10, 69),
    (KeyNames.LEFT_BRACKET, 3, 11, 75),
    (KeyNames.RIGHT_BRACKET, 3, 12, 81),
    (KeyNames.BACKSLASH, 3, 13, 13),
    (KeyNames.KP_7, 3, 14, 99),
    (KeyNames.KP_8, 3, 15, 111),
    (KeyNames.KP_9, 3, 16, 117),
    (KeyNames.KP_MINUS, 3, 17, 123),
    (KeyNames.BACKTICK, 4, 0, 4),
    (KeyNames.NUMBER_ROW_1, 4, 1, 10),
    (KeyNames.NUMBER_ROW_2, 4, 2, 16),
    (KeyNames.NUMBER_ROW_3, 4, 3, 22),
    (KeyNames.NUMBER_ROW_4, 4, 4, 28),
    (KeyNames.NUMBER_ROW_5, 4, 5, 34),
    (KeyNames.NUMBER_ROW_6, 4, 6, 40),
    (KeyNames.NUMBER_ROW_7, 4, 7, 46),
    (KeyNames.NUMBER_ROW_8, 4, 8, 52),
    (KeyNames.NUMBER_ROW_9, 4, 9, 58),
    (KeyNames.NUMBER_ROW_0, 4, 10, 64),
    (KeyNames.DASH, 4, 11, 70),
    (KeyNames.EQUAL, 4, 12, 76),
    (KeyNames.BACKSPACE, 4, 13, 82),
    (KeyNames.PREDATOR, 4, 14, 106),
    (KeyNames.NUM_LOCK, 4, 15, 112),
    (KeyNames.KP_FORWARD_SLASH, 4, 16, 118),
    (KeyNames.KP_ASTERISK, 4, 17, 124),
    (KeyNames.ESCAPE, 5, 0, 5),
    (KeyNames.F1, 5, 1, 11),
    (KeyNames.F2, 5, 2, 17),
    (KeyNames.F3, 5, 3, 23),
    (KeyNames.F4, 5, 4, 29),
    (KeyNames.F5, 5, 5, 35),
    (KeyNames.F6, 5, 6, 41),
    (KeyNames.F7, 5, 7, 47),
    (KeyNames.F8, 5, 8, 53),
    (KeyNames.F9, 5, 9, 59),
    (KeyNames.F10, 5, 10, 65),
    (KeyNames.F11, 5, 11, 71),
    (KeyNames.F12, 5, 12, 77),
    (KeyNames.PRINT_SCREEN, 5, 13, 83),
    (KeyNames.INSERT, 5, 14, 89),
    (KeyNames.DELETE, 5, 15, 95),
    (KeyNames.REWIND, 5, 16, 104),
    (KeyNames.PLAY_PAUSE, 5, 17, 105),
    (KeyNames.FAST_FORWARD, 5, 18, 103),
    (KeyNames.POWER, 5, 19, 107),
)
