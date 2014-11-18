# -*- coding: utf-8 -*-

DM_COMMAND_NAMES = {0: "DIAG_CMD_VERSION_INFO",
                    1: "DIAG_CMD_ESN",
                    2: "DIAG_CMD_PEEKB",
                    3: "DIAG_CMD_PEEKW",
                    4: "DIAG_CMD_PEEKD",
                    5: "DIAG_CMD_POKEB",
                    6: "DIAG_CMD_POKEW",
                    7: "DIAG_CMD_POKED",
                    8: "DIAG_CMD_OUTP",
                    9: "DIAG_CMD_OUTPW",
                    10: "DIAG_CMD_INP",
                    11: "DIAG_CMD_INPW",
                    12: "DIAG_CMD_STATUS",
                    15: "DIAG_CMD_LOGMASK",
                    16: "DIAG_CMD_LOG",
                    17: "DIAG_CMD_NV_PEEK",
                    18: "DIAG_CMD_NV_POKE",
                    19: "DIAG_CMD_BAD_CMD",
                    20: "DIAG_CMD_BAD_PARM",
                    21: "DIAG_CMD_BAD_LEN",
                    22: "DIAG_CMD_BAD_DEV",
                    24: "DIAG_CMD_BAD_MODE",
                    25: "DIAG_CMD_TAGRAPH",
                    26: "DIAG_CMD_MARKOV",
                    27: "DIAG_CMD_MARKOV_RESET",
                    28: "DIAG_CMD_DIAG_VER",
                    29: "DIAG_CMD_TIMESTAMP",
                    30: "DIAG_CMD_TA_PARM",
                    31: "DIAG_CMD_MESSAGE",
                    32: "DIAG_CMD_HS_KEY",
                    33: "DIAG_CMD_HS_LOCK",
                    34: "DIAG_CMD_HS_SCREEN",
                    36: "DIAG_CMD_PARM_SET",
                    38: "DIAG_CMD_NV_READ",
                    39: "DIAG_CMD_NV_WRITE",
                    41: "DIAG_CMD_CONTROL",
                    42: "DIAG_CMD_ERR_READ",
                    43: "DIAG_CMD_ERR_CLEAR",
                    44: "DIAG_CMD_SER_RESET",
                    45: "DIAG_CMD_SER_REPORT",
                    46: "DIAG_CMD_TEST",
                    47: "DIAG_CMD_GET_DIPSW",
                    48: "DIAG_CMD_SET_DIPSW",
                    49: "DIAG_CMD_VOC_PCM_LB",
                    50: "DIAG_CMD_VOC_PKT_LB",
                    53: "DIAG_CMD_ORIG",
                    54: "DIAG_CMD_END",
                    56: "DIAG_CMD_SW_VERSION",
                    58: "DIAG_CMD_DLOAD",
                    59: "DIAG_CMD_TMOB",
                    63: "DIAG_CMD_STATE",
                    64: "DIAG_CMD_PILOT_SETS",
                    65: "DIAG_CMD_SPC",
                    66: "DIAG_CMD_BAD_SPC_MODE",
                    67: "DIAG_CMD_PARM_GET2",
                    68: "DIAG_CMD_SERIAL_CHG",
                    70: "DIAG_CMD_PASSWORD",
                    71: "DIAG_CMD_BAD_SEC_MODE",
                    72: "DIAG_CMD_PRL_WRITE",
                    73: "DIAG_CMD_PRL_READ",
                    75: "DIAG_CMD_SUBSYS",
                    81: "DIAG_CMD_FEATURE_QUERY",
                    83: "DIAG_CMD_SMS_READ",
                    84: "DIAG_CMD_SMS_WRITE",
                    85: "DIAG_CMD_SUP_FER",
                    86: "DIAG_CMD_SUP_WALSH_CODES",
                    87: "DIAG_CMD_SET_MAX_SUP_CH",
                    88: "DIAG_CMD_PARM_GET_IS95B",
                    89: "DIAG_CMD_FS_OP",
                    90: "DIAG_CMD_AKEY_VERIFY",
                    91: "DIAG_CMD_HS_BMP_SCREEN",
                    92: "DIAG_CMD_CONFIG_COMM",
                    93: "DIAG_CMD_EXT_LOGMASK",
                    96: "DIAG_CMD_EVENT_REPORT",
                    97: "DIAG_CMD_STREAMING_CONFIG",
                    98: "DIAG_CMD_PARM_RETRIEVE",
                    99: "DIAG_CMD_STATUS_SNAPSHOT",
                    100: "DIAG_CMD_RPC",
                    101: "DIAG_CMD_GET_PROPERTY",
                    102: "DIAG_CMD_PUT_PROPERTY",
                    103: "DIAG_CMD_GET_GUID",
                    104: "DIAG_CMD_USER_CMD",
                    105: "DIAG_CMD_GET_PERM_PROPERTY",
                    106: "DIAG_CMD_PUT_PERM_PROPERTY",
                    107: "DIAG_CMD_PERM_USER_CMD",
                    108: "DIAG_CMD_GPS_SESS_CTRL",
                    109: "DIAG_CMD_GPS_GRID",
                    110: "DIAG_CMD_GPS_STATISTICS",
                    111: "DIAG_CMD_TUNNEL",
                    112: "DIAG_CMD_RAM_RW",
                    113: "DIAG_CMD_CPU_RW",
                    114: "DIAG_CMD_SET_FTM_TEST_MODE",
                    115: "DIAG_CMD_LOG_CONFIG",
                    124: "DIAG_CMD_EXT_BUILD_ID",
                    125: "DIAG_CMD_EXT_MESSAGE_CONFIG",
                    129: "DIAG_CMD_EVENT_GET_MASK",
                    130: "DIAG_CMD_EVENT_SET_MASK",
                    }

DM_SUBSYS_NAMES = { 4 : "DIAG_SUBSYS_WCDMA",
                    5 : "DIAG_SUBSYS_HDR",
                    8 : "DIAG_SUBSYS_GSM",
                    9 : "DIAG_SUBSYS_UMTS",
                    12 : "DIAG_SUBSYS_OS",
                    13 : "DIAG_SUBSYS_GPS",
                    14 : "DIAG_SUBSYS_SMS",
                    15 : "DIAG_SUBSYS_CM",
                    19 : "DIAG_SUBSYS_FS",
                    50 : "DIAG_SUBSYS_NW_CONTROL_6500",
                    101 : "DIAG_SUBSYS_ZTE",
                    250 : "DIAG_SUBSYS_NW_CONTROL_6800",
                    }
