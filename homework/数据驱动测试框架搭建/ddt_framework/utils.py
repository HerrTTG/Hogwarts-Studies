import logging

log = logging.getLogger("DDT")
log.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
log.addHandler(sh)
