#!/usr/bin/env python


"""Indicates CPU part of SAR file"""
PART_CPU = 0

"""Indicates RAM memory usage part of SAR file"""
PART_MEM = 1

"""Indicates swap memory usage part of SAR file"""
PART_SWP = 2

"""I/O usage part of SAR file"""
PART_IO = 3

"""NET usage part of SAR file"""
PART_NET = 4

"""CPU regexp pattern for detecting SAR section header"""
PATTERN_CPU = ".*CPU.*(usr|user).*nice.*sys.*"

"""Regexp terms for finding fields in SAR parts for CPU"""
FIELDS_CPU = [
    '\%(usr|user)', '\%nice', '\%sys', '\%iowait', '\%idle'
]

"""Pair regexp terms with field names in CPU output dictionary"""
FIELD_PAIRS_CPU = {
    'usr': FIELDS_CPU[0], 'nice': FIELDS_CPU[1], 'sys': FIELDS_CPU[2],
    'iowait': FIELDS_CPU[3], 'idle': FIELDS_CPU[4]
}

"""Mem usage regexp pattern for detecting SAR section header"""
PATTERN_MEM = ".*kbmemfree.*kbmemused.*memused.*kbbuffers.*kbcached.*"

"""Regexp terms for finding fields in SAR parts for memory usage"""
FIELDS_MEM = [
    'kbmemfree', 'kbmemused', '\%memused', 'kbbuffers', 'kbcached'
]

"""Pair regexp terms with field names in memory usage output dictionary"""
FIELD_PAIRS_MEM = {
    'memfree': FIELDS_MEM[0], 'memused': FIELDS_MEM[1],
    'memusedpercent': FIELDS_MEM[2], 'membuffer': FIELDS_MEM[3],
    'memcache': FIELDS_MEM[4]
}

"""Swap usage regexp pattern for detecting SAR section header"""
PATTERN_SWP = ".*kbswpfree.*kbswpused.*swpused.*"

"""Regexp terms for finding fields in SAR parts for swap usage"""
FIELDS_SWP = [
    'kbswpfree', 'kbswpused', '\%swpused'
]

"""Pair regexp terms with field names in swap usage output dictionary"""
FIELD_PAIRS_SWP = {
    'swapfree': FIELDS_SWP[0], 'swapused': FIELDS_SWP[1],
    'swapusedpercent': FIELDS_SWP[2]
}

"""I/O usage regexp pattern for detecting SAR section header"""
PATTERN_IO = ".*tps.*rtps.*wtps.*bread\/s.*bwrtn\/s.*"

"""NET usage regexp pattern for detecting SAR section header"""
PATTERN_NET = ".*IFACE.*rxpck\/s.*txpck\/s.*rxkB\/s.*txkB\/s.*rxcmp\/s.*txcmp\/s.*rxmcst\/s.*ifutil"

"""Regexp terms for finding fields in SAR parts for swap usage"""
FIELDS_IO = [
    '^tps', '^rtps', '^wtps', 'bread\/s', 'bwrtn\/s'
]

"""Pair regexp terms with field names in swap usage output dictionary"""
FIELD_PAIRS_IO = {
    'tps': FIELDS_IO[0], 'rtps': FIELDS_IO[1], 'wtps': FIELDS_IO[2],
    'bread': FIELDS_IO[3], 'bwrite': FIELDS_IO[4],

}

"""Regexp terms for finding fields in SAR parts for net usage"""
FIELDS_NET = [
    #'^tps', '^rtps', '^wtps', 'bread\/s', 'bwrtn\/s'
    '^IFACE','^rxpck\/s','^txpck\/s','^rxkB\/s','^txkB\/s','^rxcmp\/s','^txcmp\/s','^rxmcst\/s','^%ifutil'
]

"""Pair regexp terms with field names in net usage output dictionary"""
FIELD_PAIRS_NET = {
    'IFACE':FIELDS_NET[0],
    'rxpck':FIELDS_NET[1],
    'txpck':FIELDS_NET[2],
    'rxkB':FIELDS_NET[3],
    'txkB':FIELDS_NET[4],
    'rxcmp':FIELDS_NET[5],
    'txcmp':FIELDS_NET[6],
    'rxmcst':FIELDS_NET[7],
    'ifutil':FIELDS_NET[8],

}

"""Restart time regexp pattern for detecting SAR restart notices"""
PATTERN_RESTART = ".*LINUX\ RESTART.*"

"""Pattern for splitting multiple combined SAR file"""
PATTERN_MULTISPLIT = "Linux"

"""Split by date in multiday SAR file"""
PATTERN_DATE = "[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]"

__all__ = [
    "PART_CPU", "PART_MEM", "PART_SWP", "PART_IO",
    "PATTERN_CPU", "PATTERN_MEM", "PATTERN_SWP", "PATTERN_IO","PATTERN_NET",
    "PATTERN_RESTART", "PATTERN_MULTISPLIT", "PATTERN_DATE"
]
