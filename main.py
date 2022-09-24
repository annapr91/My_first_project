import psutil


class CpuInfo:
    cpu = {}

    def __init__(self, info):
        self.info = info

    def get_data(self):
        self.cpu.update(user=round(self.info.user, 2), system=round(self.info.system, 2), idle=round(self.info.idle, 2))


    def table(self):
        lis=self.cpu.items()
        self.header_for_CPU = '|{:*^60}'.format('CPU') + '\n'
        self.header_for_CPU += '|' + '_' * 60 + '|' + '\n'
        for i in lis:
            self.header_for_CPU += '|{:^30}'.format(i[0]) + '|{:^29}|'.format(i[1]) + '\n'
            self.header_for_CPU += '|' + '_' * 60 + '|' + '\n'

        return self.header_for_CPU


class VirtMem:
    mem = {}


    def __init__(self, info):
        self.info = info

    def get_data(self):
        self.mem.update(Total_MEM=round(self.info.total / 10**9, 2), Available_MEM=round(self.info.available /10**9, 2),
                   Used_MEM=round(self.info.used / 10**9, 2), MEM_usage=round(self.info.percent))

    def table(self):
        lis=self.mem.items()
        header_for_Memory = '|{:*^60}|'.format('MEMORY') + '\n'
        header_for_Memory += '|' + '_' * 60 + '|' + '\n'
        for j in lis:
            if j == 'MEM_usage':
                header_for_Memory += '|{:^30}'.format(j[0]) + '|{:^29}|'.format(str(j[1]) + '%') + '\n'
            else:
                header_for_Memory += '|{:^30}'.format(j[0]) + '|{:^29}|'.format(j[1]) + '\n'
                header_for_Memory += '|' + '_' * 60 + '|' + '\n'
        return header_for_Memory


def main():
    _CPU =CpuInfo(psutil.cpu_times())
    _CPU.get_data()
    print(_CPU.table())

    _VIRT_mem = VirtMem(psutil.virtual_memory())
    _VIRT_mem.get_data()
    print(_VIRT_mem.table())


if __name__ == '__main__':
      main()





