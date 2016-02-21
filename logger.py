import logging
import socket
from logging.handlers import SysLogHandler


class ContextFilter(logging.Filter):
	hostname = socket.gethostname()

	def filter(self, record):
		record.hostname = ContextFilter.hostname
		return True


logger = logging.getLogger()
logger.setLevel(logging.INFO)

f = ContextFilter()
logger.addFilter(f)

syslog = SysLogHandler(address=('logs3.papertrailapp.com', 33501))
formatter = logging.Formatter('%(asctime)s  Sense: %(message)s', datefmt='%b %d %H:%M:%S')

syslog.setFormatter(formatter)
logger.addHandler(syslog)

# logger.info("This is a message")

log = logger