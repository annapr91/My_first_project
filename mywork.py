import psutil
import json


def info_decor_(level):
    def decor_func(func):
        def filename():
            with open(level, 'a') as outfile:
                res = func()
                json.dump(res, outfile, sort_keys=True, indent=2)
            return res

        return filename

    return decor_func


@info_decor_("data1.json")
def virt_mem():
    mem = {}
    data = psutil.virtual_memory()
    mem.update(Total_MEM=round(data.total / 1000000000, 2), Available_MEM=round(data.available / 1000000000, 2),
               Used_MEM=round(data.used / 1000000000, 2), MEM_usage=round(data.percent))
    return mem


@info_decor_('data1.json')
def cpu_info():
    cpu = {}
    info = psutil.cpu_times()
    cpu.update(user=round(info.user, 2), system=round(info.system, 2), idle=round(info.idle, 2))
    return cpu


@info_decor_('data1.json')
def disk_info():
    disk = {}
    data = psutil.disk_usage('/')
    disk.update(Total=round(data.total / 1000000000, 2), Used=round(data.used / 1000000000, 2),
                Free=round(data.free / 1000000000, 2), Percent=data.percent)
    return disk


def show(_VIRT_mem, _CPU, _DISK):
    header_for_CPU = '|{:*^60}'.format('CPU') + '\n'
    header_for_CPU += '|' + '_' * 60 + '|' + '\n'
    for i in _CPU:
        header_for_CPU += '|{:^30}'.format(i) + '|{:^29}|'.format(_CPU[i]) + '\n'
        header_for_CPU += '|' + '_' * 60 + '|' + '\n'

    header_for_Memory = '|{:*^60}|'.format('MEMORY') + '\n'
    header_for_Memory += '|' + '_' * 60 + '|' + '\n'
    for j in _VIRT_mem:
        if j == 'MEM_usage':
            header_for_Memory += '|{:^30}'.format(j) + '|{:^29}|'.format(str(_VIRT_mem[j]) + '%') + '\n'
        else:
            header_for_Memory += '|{:^30}'.format(j) + '|{:^29}|'.format(_VIRT_mem[j]) + '\n'
            header_for_Memory += '|' + '_' * 60 + '|' + '\n'

    header_for_Disk = '|{:*^60}|'.format('DISK') + '\n'
    header_for_Disk += '|' + '_' * 60 + '|' + '\n'
    for r in _DISK:
        header_for_Disk += '|{:^30}'.format(r) + '|{:^29}|'.format(_DISK[r]) + '\n'
        header_for_Disk += '|' + '_' * 60 + '|' + '\n'

    print(header_for_CPU, header_for_Memory, header_for_Disk)


def main():
    _CPU = cpu_info()
    _VIRT_mem = virt_mem()
    _DISK = disk_info()
    show(_CPU, _VIRT_mem, _DISK)


if __name__ == '__main__':
    main()
