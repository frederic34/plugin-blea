import time

KNOWN_DEVICES = {}
LEARN_MODE = False
LEARN_MODE_ALL = 0
LEARN_BEGIN = int(time.time())
LAST_CLEAR = int(time.time())
COMPATIBILITY = []
LAST_STATE={}
KEEPED_CONNECTION={}
LAST_STORAGE={}
LAST_TIME_READ = {}
IFACE_DEVICE = 0
SCAN_ERRORS = 0
SCANNER = ''
PENDING_ACTION = False
log_level = "error"
pidfile = '/tmp/blead.pid'
apikey = ''
callback = ''
cycle = 0.3
daemonname=''
socketport=''
sockethost=''
