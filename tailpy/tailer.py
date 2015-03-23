import pyuv, sys, os, signal

class Tailer(object):
    """Log tailer."""
    def __init__(self, filename):
        self.filename = filename
        self.loop = pyuv.Loop.default_loop()
        self.end_of_file = os.stat(filename).st_size
        self.filehandle = open(filename, "r")
        
        self.signal_h = pyuv.Signal(self.loop)
        self.signal_h.start(self.signal_cb, signal.SIGINT)
        
        self.event_handle = pyuv.fs.FSEvent(self.loop)
        self.event_handle.start(filename, 0, self.read_handle)
    
    def read_handle(self, handle, filename, events, error):
        """Callback every time data is appended to the file."""
        self.filehandle.seek(self.end_of_file)
        tailportion = self.filehandle.read()
        sys.stdout.write(tailportion)
        self.end_of_file = os.stat(self.filename).st_size
        
    def signal_cb(self, handle, signum):
        """Handle ctrl-C"""
        self.filehandle.close()
        self.signal_h.close()
        sys.exit()
    
    def run(self):
        self.loop.run()

def tail():
    Tailer(sys.argv[1]).run()

if __name__ == "__main__":
    tail()