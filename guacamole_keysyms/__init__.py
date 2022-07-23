#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guacamole protocol key mappings for python
Source: https://guacamole.apache.org/doc/0.9.0/guacamole-common-js/symbols/src/src_main_webapp_modules_Keyboard.js.html"""


__version__: str = "0.0.5"
__author__: str = "Ari Archer"
__author_email__: str = "ari.web.xyz@gmail.com"


class UnshiftedKeyCodes:
    """Map of known JavaScript keycodes which do not map to typable characters
    to their unshifted X11 keysym equivalents."""

    BACKSPACE: int = 0xFF08
    TAB: int = 0xFF09
    ENTER: int = 0xFF0D
    SHIFT: int = 0xFFE1
    CTRL: int = 0xFFE3
    ALT: int = 0xFFE9
    PAUSE: int = 0xFF13
    CAPS_LOCK: int = 0xFFE5
    ESCAPE: int = 0xFF1B
    SPACE: int = 0x0020
    PAGE_UP: int = 0xFF55
    PAGE_DOWN: int = 0xFF56
    END: int = 0xFF57
    HOME: int = 0xFF50
    LEFT_ARROW: int = 0xFF51
    UP_ARROW: int = 0xFF52
    RIGHT_ARROW: int = 0xFF53
    DOWN_ARROW: int = 0xFF54
    INSERT: int = 0xFF63
    DELETE: int = 0xFFFF
    LEFT_WINDOW_KEY: int = 0xFFEB
    RIGHT_WINDOW_KEY: int = 0xFF67
    SELECT_KEY: int = 0x0
    F1: int = 0xFFBE
    F2: int = 0xFFBF
    F3: int = 0xFFC0
    F4: int = 0xFFC1
    F5: int = 0xFFC2
    F6: int = 0xFFC3
    F7: int = 0xFFC4
    F8: int = 0xFFC5
    F9: int = 0xFFC6
    F10: int = 0xFFC7
    F11: int = 0xFFC8
    F12: int = 0xFFC9
    NUM_LOCK: int = 0xFF7F
    SCROLL_LOCK: int = 0xFF14


class KeyIdentifiers:
    """Map of known Python keyidentifiers which do not map to typable
    characters to their unshifted X11 keysym equivalents."""

    AGAIN: int = 0xFF66
    ALL_CANDIDATES: int = 0xFF3D
    ALPHANUMERIC: int = 0xFF30
    ALT: int = 0xFFE9
    ATTN: int = 0xFD0E
    ALT_GRAPH: int = 0xFFEA
    ARROW_DOWN: int = 0xFF54
    ARROW_LEFT: int = 0xFF51
    ARROW_RIGHT: int = 0xFF53
    ARROW_UP: int = 0xFF52
    BACKSPACE: int = 0xFF08
    CAPS_LOCK: int = 0xFFE5
    CANCEL: int = 0xFF69
    CLEAR: int = 0xFF0B
    CONVERT: int = 0xFF21
    COPY: int = 0xFD15
    CRSEL: int = 0xFD1C
    CR_SEL: int = 0xFD1C
    CODE_INPUT: int = 0xFF37
    COMPOSE: int = 0xFF20
    CONTROL: int = 0xFFE3
    CONTEXT_MENU: int = 0xFF67
    DELETE: int = 0xFFFF
    DOWN: int = 0xFF54
    END: int = 0xFF57
    ENTER: int = 0xFF0D
    ERASE_EOF: int = 0xFD06
    ESCAPE: int = 0xFF1B
    EXECUTE: int = 0xFF62
    EXSEL: int = 0xFD1D
    EX_SEL: int = 0xFD1D
    F1: int = 0xFFBE
    F2: int = 0xFFBF
    F3: int = 0xFFC0
    F4: int = 0xFFC1
    F5: int = 0xFFC2
    F6: int = 0xFFC3
    F7: int = 0xFFC4
    F8: int = 0xFFC5
    F9: int = 0xFFC6
    F10: int = 0xFFC7
    F11: int = 0xFFC8
    F12: int = 0xFFC9
    F13: int = 0xFFCA
    F14: int = 0xFFCB
    F15: int = 0xFFCC
    F16: int = 0xFFCD
    F17: int = 0xFFCE
    F18: int = 0xFFCF
    F19: int = 0xFFD0
    F20: int = 0xFFD1
    F21: int = 0xFFD2
    F22: int = 0xFFD3
    F23: int = 0xFFD4
    F24: int = 0xFFD5
    FIND: int = 0xFF68
    GROUP_FIRST: int = 0xFE0C
    GROUP_LAST: int = 0xFE0E
    GROUP_NEXT: int = 0xFE08
    GROUP_PREVIOUS: int = 0xFE0A
    FULL_WIDTH: int = 0x0
    HALF_WIDTH: int = 0x0
    HANGUL_MODE: int = 0xFF31
    HANKAKU: int = 0xFF29
    HANJA_MODE: int = 0xFF34
    HELP: int = 0xFF6A
    HIRAGANA: int = 0xFF25
    HIRAGANA_KATAKANA: int = 0xFF27
    HOME: int = 0xFF50
    HYPER: int = 0xFFED
    INSERT: int = 0xFF63
    JAPANESE_HIRAGANA: int = 0xFF25
    JAPANESE_KATAKANA: int = 0xFF26
    JAPANESE_ROMAJI: int = 0xFF24
    JUNJA_MODE: int = 0xFF38
    KANA_MODE: int = 0xFF2D
    KANJI_MODE: int = 0xFF21
    KATAKANA: int = 0xFF26
    LEFT: int = 0xFF51
    META: int = 0xFFE7
    MODE_CHANGE: int = 0xFF7E
    NUM_LOCK: int = 0xFF7F
    PAGE_DOWN: int = 0xFF55
    PAGE_UP: int = 0xFF56
    PAUSE: int = 0xFF13
    PLAY: int = 0xFD16
    PREVIOUS_CANDIDATE: int = 0xFF3E
    PRINT_SCREEN: int = 0xFD1D
    REDO: int = 0xFF66
    RIGHT: int = 0xFF53
    ROMAN_CHARACTERS: int = 0x0
    SCROLL: int = 0xFF14
    SELECT: int = 0xFF60
    SEPARATOR: int = 0xFFAC
    SHIFT: int = 0xFFE1
    SINGLE_CANDIDATE: int = 0xFF3C
    SUPER: int = 0xFFEB
    TAB: int = 0xFF09
    UP: int = 0xFF52
    UNDO: int = 0xFF65
    WIN: int = 0xFFEB
    ZENKAKU: int = 0xFF28
    ZENKAKU_HANKAKU: int = 0xFF2A


class ShiftedKeywords:
    """Map of known Python keycodes which do not map to typable characters
    to their shifted X11 keysym equivalents. Keycodes must only be listed
    here if their shifted X11 keysym equivalents differ from their unshifted
    equivalents."""

    ALT: int = 0xFFE7


class NoRepeat:
    """All keysyms which should not repeat when held down."""

    LEFT_SHIFT: int = 0xFFE1
    RIGHT_SHIFT: int = 0xFFE2
    LEFT_CTRL: int = 0xFFE3
    RIGHT_CTRL: int = 0xFFE4
    LEFT_META: int = 0xFFE7
    RIGHT_META: int = 0xFFE8
    LEFT_ALT: int = 0xFFE9
    RIGHT_ALT: int = 0xFFEA
    LEFT_HYPER: int = 0xFFEB
    RIGHT_HYPER: int = 0xFFEC


class AsciiKeys:
    """Map of all X11 typable ASCII characters"""

    KEY_SPACE: int = 0x20
    KEY_LOWERCASE_A: int = 0x61
    KEY_LOWERCASE_B: int = 0x62
    KEY_LOWERCASE_C: int = 0x63
    KEY_LOWERCASE_D: int = 0x64
    KEY_LOWERCASE_E: int = 0x65
    KEY_LOWERCASE_F: int = 0x66
    KEY_LOWERCASE_G: int = 0x67
    KEY_LOWERCASE_H: int = 0x68
    KEY_LOWERCASE_I: int = 0x69
    KEY_LOWERCASE_J: int = 0x6A
    KEY_LOWERCASE_K: int = 0x6B
    KEY_LOWERCASE_L: int = 0x6C
    KEY_LOWERCASE_M: int = 0x6D
    KEY_LOWERCASE_N: int = 0x6E
    KEY_LOWERCASE_O: int = 0x6F
    KEY_LOWERCASE_P: int = 0x70
    KEY_LOWERCASE_Q: int = 0x71
    KEY_LOWERCASE_R: int = 0x72
    KEY_LOWERCASE_S: int = 0x73
    KEY_LOWERCASE_T: int = 0x74
    KEY_LOWERCASE_U: int = 0x75
    KEY_LOWERCASE_V: int = 0x76
    KEY_LOWERCASE_W: int = 0x77
    KEY_LOWERCASE_X: int = 0x78
    KEY_LOWERCASE_Y: int = 0x79
    KEY_LOWERCASE_Z: int = 0x7A
    KEY_UPPERCASE_A: int = 0x41
    KEY_UPPERCASE_B: int = 0x42
    KEY_UPPERCASE_C: int = 0x43
    KEY_UPPERCASE_D: int = 0x44
    KEY_UPPERCASE_E: int = 0x45
    KEY_UPPERCASE_F: int = 0x46
    KEY_UPPERCASE_G: int = 0x47
    KEY_UPPERCASE_H: int = 0x48
    KEY_UPPERCASE_I: int = 0x49
    KEY_UPPERCASE_J: int = 0x4A
    KEY_UPPERCASE_K: int = 0x4B
    KEY_UPPERCASE_L: int = 0x4C
    KEY_UPPERCASE_M: int = 0x4D
    KEY_UPPERCASE_N: int = 0x4E
    KEY_UPPERCASE_O: int = 0x4F
    KEY_UPPERCASE_P: int = 0x50
    KEY_UPPERCASE_Q: int = 0x51
    KEY_UPPERCASE_R: int = 0x52
    KEY_UPPERCASE_S: int = 0x53
    KEY_UPPERCASE_T: int = 0x54
    KEY_UPPERCASE_U: int = 0x55
    KEY_UPPERCASE_V: int = 0x56
    KEY_UPPERCASE_W: int = 0x57
    KEY_UPPERCASE_X: int = 0x58
    KEY_UPPERCASE_Y: int = 0x59
    KEY_UPPERCASE_Z: int = 0x5A
    SIGN_EXCLAMATION: int = 0x21
    SIGN_DOUBLE_QUOTE: int = 0x22
    SIGN_HASH: int = 0x23
    SIGN_DOLLAR: int = 0x24
    SIGN_PERCENT: int = 0x25
    SIGN_AMPERSAND: int = 0x26
    SIGN_SINGLE_QUOTE: int = 0x27
    SIGN_OPENING_BRACKET: int = 0x28
    SIGN_CLOSING_BRACKET: int = 0x29
    SIGN_STAR: int = 0x2A
    SIGN_PLUS: int = 0x2B
    SIGN_COMMA: int = 0x2C
    SIGN_MINUS: int = 0x2D
    SIGN_DOT: int = 0x2E
    SIGN_SLASH: int = 0x2F
    SIGN_COLON: int = 0x3A
    SIGN_SEMICOLON: int = 0x3B
    SIGN_LESS_THAN: int = 0x3C
    SIGN_EQUAL: int = 0x3D
    SIGN_MORE_THAN: int = 0x3E
    SIGN_QUESTION: int = 0x3F
    SIGN_AT: int = 0x40
    SIGN_OPENING_SQUARE_BRACKET: int = 0x5B
    SIGN_BACKSLASH: int = 0x5C
    SIGN_CLOSING_SQUARE_BRACKET: int = 0x5D
    SIGN_CARET: int = 0x5E
    SIGN_UNDERSCORE: int = 0x5F
    SIGN_BACKTICK: int = 0x60
    SIGN_OPENING_CURLY_BRACKET: int = 0x7B
    SIGN_PIPE: int = 0x7C
    SIGN_CLOSING_CURLY_BRACKET: int = 0x7D
    SIGN_TILDE: int = 0x7E
