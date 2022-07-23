#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guacamole protocol key mappings for python
Source: https://guacamole.apache.org/doc/0.9.0/guacamole-common-js/symbols/src/src_main_webapp_modules_Keyboard.js.html"""


from enum import IntEnum

__version__: str = "0.0.4"
__author__: str = "Ari Archer <ari.web.xyz@gmail.com>"


class UnshiftedKeyCodes(IntEnum):
    """Map of known JavaScript keycodes which do not map to typable characters
    to their unshifted X11 keysym equivalents.
    """

    BACKSPACE = 0xFF08
    TAB = 0xFF09
    ENTER = 0xFF0D
    SHIFT = 0xFFE1
    CTRL = 0xFFE3
    ALT = 0xFFE9
    PAUSE = 0xFF13
    CAPS_LOCK = 0xFFE5
    ESCAPE = 0xFF1B
    SPACE = 0x0020
    PAGE_UP = 0xFF55
    PAGE_DOWN = 0xFF56
    END = 0xFF57
    HOME = 0xFF50
    LEFT_ARROW = 0xFF51
    UP_ARROW = 0xFF52
    RIGHT_ARROW = 0xFF53
    DOWN_ARROW = 0xFF54
    INSERT = 0xFF63
    DELETE = 0xFFFF
    LEFT_WINDOW_KEY = 0xFFEB
    RIGHT_WINDOW_KEY = 0xFF67
    SELECT_KEY = 0x0
    F1 = 0xFFBE
    F2 = 0xFFBF
    F3 = 0xFFC0
    F4 = 0xFFC1
    F5 = 0xFFC2
    F6 = 0xFFC3
    F7 = 0xFFC4
    F8 = 0xFFC5
    F9 = 0xFFC6
    F10 = 0xFFC7
    F11 = 0xFFC8
    F12 = 0xFFC9
    NUM_LOCK = 0xFF7F
    SCROLL_LOCK = 0xFF14


class KeyIdentifiers(IntEnum):
    """Map of known Python keyidentifiers which do not map to typable
    characters to their unshifted X11 keysym equivalents."""

    AGAIN = 0xFF66
    ALL_CANDIDATES = 0xFF3D
    ALPHANUMERIC = 0xFF30
    ALT = 0xFFE9
    ATTN = 0xFD0E
    ALT_GRAPH = 0xFFEA
    ARROW_DOWN = 0xFF54
    ARROW_LEFT = 0xFF51
    ARROW_RIGHT = 0xFF53
    ARROW_UP = 0xFF52
    BACKSPACE = 0xFF08
    CAPS_LOCK = 0xFFE5
    CANCEL = 0xFF69
    CLEAR = 0xFF0B
    CONVERT = 0xFF21
    COPY = 0xFD15
    CRSEL = 0xFD1C
    CR_SEL = 0xFD1C
    CODE_INPUT = 0xFF37
    COMPOSE = 0xFF20
    CONTROL = 0xFFE3
    CONTEXT_MENU = 0xFF67
    DELETE = 0xFFFF
    DOWN = 0xFF54
    END = 0xFF57
    ENTER = 0xFF0D
    ERASE_EOF = 0xFD06
    ESCAPE = 0xFF1B
    EXECUTE = 0xFF62
    EXSEL = 0xFD1D
    EX_SEL = 0xFD1D
    F1 = 0xFFBE
    F2 = 0xFFBF
    F3 = 0xFFC0
    F4 = 0xFFC1
    F5 = 0xFFC2
    F6 = 0xFFC3
    F7 = 0xFFC4
    F8 = 0xFFC5
    F9 = 0xFFC6
    F10 = 0xFFC7
    F11 = 0xFFC8
    F12 = 0xFFC9
    F13 = 0xFFCA
    F14 = 0xFFCB
    F15 = 0xFFCC
    F16 = 0xFFCD
    F17 = 0xFFCE
    F18 = 0xFFCF
    F19 = 0xFFD0
    F20 = 0xFFD1
    F21 = 0xFFD2
    F22 = 0xFFD3
    F23 = 0xFFD4
    F24 = 0xFFD5
    FIND = 0xFF68
    GROUP_FIRST = 0xFE0C
    GROUP_LAST = 0xFE0E
    GROUP_NEXT = 0xFE08
    GROUP_PREVIOUS = 0xFE0A
    FULL_WIDTH = 0x0
    HALF_WIDTH = 0x0
    HANGUL_MODE = 0xFF31
    HANKAKU = 0xFF29
    HANJA_MODE = 0xFF34
    HELP = 0xFF6A
    HIRAGANA = 0xFF25
    HIRAGANA_KATAKANA = 0xFF27
    HOME = 0xFF50
    HYPER = 0xFFED
    INSERT = 0xFF63
    JAPANESE_HIRAGANA = 0xFF25
    JAPANESE_KATAKANA = 0xFF26
    JAPANESE_ROMAJI = 0xFF24
    JUNJA_MODE = 0xFF38
    KANA_MODE = 0xFF2D
    KANJI_MODE = 0xFF21
    KATAKANA = 0xFF26
    LEFT = 0xFF51
    META = 0xFFE7
    MODE_CHANGE = 0xFF7E
    NUM_LOCK = 0xFF7F
    PAGE_DOWN = 0xFF55
    PAGE_UP = 0xFF56
    PAUSE = 0xFF13
    PLAY = 0xFD16
    PREVIOUS_CANDIDATE = 0xFF3E
    PRINT_SCREEN = 0xFD1D
    REDO = 0xFF66
    RIGHT = 0xFF53
    ROMAN_CHARACTERS = 0x0
    SCROLL = 0xFF14
    SELECT = 0xFF60
    SEPARATOR = 0xFFAC
    SHIFT = 0xFFE1
    SINGLE_CANDIDATE = 0xFF3C
    SUPER = 0xFFEB
    TAB = 0xFF09
    UP = 0xFF52
    UNDO = 0xFF65
    WIN = 0xFFEB
    ZENKAKU = 0xFF28
    ZENKAKU_HANKAKU = 0xFF2A


class ShiftedKeywords(IntEnum):
    """Map of known Python keycodes which do not map to typable characters
    to their shifted X11 keysym equivalents. Keycodes must only be listed
    here if their shifted X11 keysym equivalents differ from their unshifted
    equivalents."""

    ALT = 0xFFE7


class NoRepeat(IntEnum):
    """All keysyms which should not repeat when held down."""

    LEFT_SHIFT = 0xFFE1
    RIGHT_SHIFT = 0xFFE2
    LEFT_CTRL = 0xFFE3
    RIGHT_CTRL = 0xFFE4
    LEFT_META = 0xFFE7
    RIGHT_META = 0xFFE8
    LEFT_ALT = 0xFFE9
    RIGHT_ALT = 0xFFEA
    LEFT_HYPER = 0xFFEB
    RIGHT_HYPER = 0xFFEC


class AsciiKeys(IntEnum):
    """Map of all X11 typable ASCII characters"""

    KEY_SPACE = 0x20
    KEY_LOWERCASE_A = 0x61
    KEY_LOWERCASE_B = 0x62
    KEY_LOWERCASE_C = 0x63
    KEY_LOWERCASE_D = 0x64
    KEY_LOWERCASE_E = 0x65
    KEY_LOWERCASE_F = 0x66
    KEY_LOWERCASE_G = 0x67
    KEY_LOWERCASE_H = 0x68
    KEY_LOWERCASE_I = 0x69
    KEY_LOWERCASE_J = 0x6A
    KEY_LOWERCASE_K = 0x6B
    KEY_LOWERCASE_L = 0x6C
    KEY_LOWERCASE_M = 0x6D
    KEY_LOWERCASE_N = 0x6E
    KEY_LOWERCASE_O = 0x6F
    KEY_LOWERCASE_P = 0x70
    KEY_LOWERCASE_Q = 0x71
    KEY_LOWERCASE_R = 0x72
    KEY_LOWERCASE_S = 0x73
    KEY_LOWERCASE_T = 0x74
    KEY_LOWERCASE_U = 0x75
    KEY_LOWERCASE_V = 0x76
    KEY_LOWERCASE_W = 0x77
    KEY_LOWERCASE_X = 0x78
    KEY_LOWERCASE_Y = 0x79
    KEY_LOWERCASE_Z = 0x7A
    KEY_UPPERCASE_A = 0x41
    KEY_UPPERCASE_B = 0x42
    KEY_UPPERCASE_C = 0x43
    KEY_UPPERCASE_D = 0x44
    KEY_UPPERCASE_E = 0x45
    KEY_UPPERCASE_F = 0x46
    KEY_UPPERCASE_G = 0x47
    KEY_UPPERCASE_H = 0x48
    KEY_UPPERCASE_I = 0x49
    KEY_UPPERCASE_J = 0x4A
    KEY_UPPERCASE_K = 0x4B
    KEY_UPPERCASE_L = 0x4C
    KEY_UPPERCASE_M = 0x4D
    KEY_UPPERCASE_N = 0x4E
    KEY_UPPERCASE_O = 0x4F
    KEY_UPPERCASE_P = 0x50
    KEY_UPPERCASE_Q = 0x51
    KEY_UPPERCASE_R = 0x52
    KEY_UPPERCASE_S = 0x53
    KEY_UPPERCASE_T = 0x54
    KEY_UPPERCASE_U = 0x55
    KEY_UPPERCASE_V = 0x56
    KEY_UPPERCASE_W = 0x57
    KEY_UPPERCASE_X = 0x58
    KEY_UPPERCASE_Y = 0x59
    KEY_UPPERCASE_Z = 0x5A
    SIGN_EXCLAMATION = 0x21
    SIGN_DOUBLE_QUOTE = 0x22
    SIGN_HASH = 0x23
    SIGN_DOLLAR = 0x24
    SIGN_PERCENT = 0x25
    SIGN_AMPERSAND = 0x26
    SIGN_SINGLE_QUOTE = 0x27
    SIGN_OPENING_BRACKET = 0x28
    SIGN_CLOSING_BRACKET = 0x29
    SIGN_STAR = 0x2A
    SIGN_PLUS = 0x2B
    SIGN_COMMA = 0x2C
    SIGN_MINUS = 0x2D
    SIGN_DOT = 0x2E
    SIGN_SLASH = 0x2F
    SIGN_COLON = 0x3A
    SIGN_SEMICOLON = 0x3B
    SIGN_LESS_THAN = 0x3C
    SIGN_EQUAL = 0x3D
    SIGN_MORE_THAN = 0x3E
    SIGN_QUESTION = 0x3F
    SIGN_AT = 0x40
    SIGN_OPENING_SQUARE_BRACKET = 0x5B
    SIGN_BACKSLASH = 0x5C
    SIGN_CLOSING_SQUARE_BRACKET = 0x5D
    SIGN_CARET = 0x5E
    SIGN_UNDERSCORE = 0x5F
    SIGN_BACKTICK = 0x60
    SIGN_OPENING_CURLY_BRACKET = 0x7B
    SIGN_PIPE = 0x7C
    SIGN_CLOSING_CURLY_BRACKET = 0x7D
    SIGN_TILDE = 0x7E
