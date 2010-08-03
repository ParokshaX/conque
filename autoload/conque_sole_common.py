
import mmap

##############################################################
# shared memory creation

# XXX - assumes user will never write a nul char to input

# size of shared memory
SHM_SIZE = 4096

def create_shm (name, access):
    global SHM_SIZE
    name = "%s_%s" % ('conque_sole', name)
    smo = mmap.mmap (0, SHM_SIZE, name, access)
    if not smo:
        exit()
    else:
        return smo

def read_shm (shm):
    global SHM_SIZE
    shm.seek(0)
    nul_pos = shm.find(chr(0))
    if nul_pos == 0:
        return ''
    elif nul_pos == -1:
      shm_str = shm.read(SHM_SIZE).encode('ascii', 'ignore')
    else:
      shm_str = shm.read(nul_pos).encode('ascii', 'ignore')
    return shm_str

def clear_shm(shm):
    global SHM_SIZE
    shm.seek(0)
    shm.write(chr(0))

def write_shm(shm, text):
    global SHM_SIZE
    shm.seek(0)
    shm.write(text + chr(0))
