from .linux import sysinfo,load,cpu_mac,cpu,memory,network,host_alive

def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()

def WindowsSysInfo():
    from windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()

def GetLinuxCpuStatus():
    return cpu.monitor()

def host_alive_check():
    return host_alive.monitor()

def GetLinuxMemStatus():
    return memory.monitor()

def GetMacCPU():
    #return cpu.monitor()
    return cpu_mac.monitor()

def GetLinuxNetworkStatus():
    return network.monitor()

def get_linux_load():
    return load.monitor()