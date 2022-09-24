import psutil


class CpuInfo:
    cpu = {}

    def get_data(self,info):
        self.cpu.update(user=round(info.user, 2), system=round(info.system, 2), idle=round(info.idle, 2))


    def table(self):
        lis=self.cpu.items()
        self.header_for_CPU = '|{:*^60}'.format('CPU') + '\n'
        self.header_for_CPU += '|' + '_' * 60 + '|' + '\n'
        for i in lis:
            self.header_for_CPU += '|{:^30}'.format(i[0]) + '|{:^29}|'.format(i[1]) + '\n'
            self.header_for_CPU += '|' + '_' * 60 + '|' + '\n'


    def __str__(self):
        return self.header_for_CPU


class VirtMem:
    mem = {}

    def get_data(self,info):
        self.mem.update(Total_MEM=round(info.total / 10**9, 2), Available_MEM=round(info.available /10**9, 2),
                   Used_MEM=round(info.used / 10**9, 2), MEM_usage=round(info.percent))


    def table(self):
        lis=self.mem.items()
        self.header_for_Memory = '|{:*^60}|'.format('MEMORY') + '\n'
        self.header_for_Memory += '|' + '_' * 60 + '|' + '\n'
        for j in lis:
            if j == 'MEM_usage':
                self.header_for_Memory += '|{:^30}'.format(j[0]) + '|{:^29}|'.format(str(j[1]) + '%') + '\n'
            else:
                self.header_for_Memory += '|{:^30}'.format(j[0]) + '|{:^29}|'.format(j[1]) + '\n'
                self.header_for_Memory += '|' + '_' * 60 + '|' + '\n'

    def __str__(self):
        return self.header_for_Memory


class DiskInfo:
    disk = {}

    def get_data(self,info):
        self.disk.update(Total=round(info.total / 10**9, 2), Used=round(info.used / 10**9, 2),
                    Free=round(info.free / 10**9, 2), Percent=info.percent)

    def table(self):
        lis=self.disk.items()
        self.header_for_Disk = '|{:*^60}|'.format('DISK') + '\n'
        self.header_for_Disk += '|' + '_' * 60 + '|' + '\n'
        for r in lis:
            self.header_for_Disk += '|{:^30}'.format(r[0]) + '|{:^29}|'.format(r[1]) + '\n'
            self.header_for_Disk += '|' + '_' * 60 + '|' + '\n'

    def __str__(self):
        return self.header_for_Disk


def main():
    _CPU =CpuInfo()
    _CPU.get_data(psutil.cpu_times())
    _CPU.table()
    print(_CPU)

    _VIRT_mem = VirtMem()
    _VIRT_mem.get_data(psutil.virtual_memory())
    _VIRT_mem.table()
    print(_VIRT_mem)

    _DISK= DiskInfo()
    _DISK.get_data(psutil.disk_usage('/'))
    _DISK.table()
    print(_DISK)



if __name__ == '__main__':
       main()
