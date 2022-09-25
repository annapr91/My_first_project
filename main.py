import psutil


class CpuInfo:
    cpu = {}

    def get_data(self, ):
        self.cpu.update(user=round(psutil.cpu_times().user, 2),
                        system=round(psutil.cpu_times().system, 2),
                        idle=round(psutil.cpu_times().idle, 2))

    def __str__(self):
        def _table():
            lis = self.cpu.items()
            header_for_CPU = '|{:*^60}'.format('CPU') + '\n'
            header_for_CPU += '|' + '_' * 60 + '|' + '\n'
            for i in lis:
                header_for_CPU += '|{:^30}'.format(i[0]) + '|{:^29}|'.format(i[1]) + '\n'
                header_for_CPU += '|' + '_' * 60 + '|' + '\n'

            return header_for_CPU

        return _table()


class VirtMem:
    mem = {}

    def get_data(self):
        self.mem.update(Total_MEM=round(psutil.virtual_memory().total / 10 ** 9, 2),
                        Available_MEM=round(psutil.virtual_memory().available / 10 ** 9, 2),
                        Used_MEM=round(psutil.virtual_memory().used / 10 ** 9, 2),
                        MEM_usage=round(psutil.virtual_memory().percent))

    def __str__(self):
        def _table():
            lis = self.mem.items()
            header_for_Memory = '|{:*^60}|'.format('MEMORY') + '\n'
            header_for_Memory += '|' + '_' * 60 + '|' + '\n'
            for j in lis:
                if j == 'MEM_usage':
                    header_for_Memory += '|{:^30}'.format(j[0]) + '|{:^29}|'.format(str(j[1]) + '%') + '\n'
                else:
                    header_for_Memory += '|{:^30}'.format(j[0]) + '|{:^29}|'.format(j[1]) + '\n'
                    header_for_Memory += '|' + '_' * 60 + '|' + '\n'

            return header_for_Memory

        return _table()


class DiskInfo:
    disk = {}

    def get_data(self):
        self.disk.update(Total=round(psutil.disk_usage('/').total / 10 ** 9, 2),
                         Used=round(psutil.disk_usage('/').used / 10 ** 9, 2),
                         Free=round(psutil.disk_usage('/').free / 10 ** 9, 2),
                         Percent=psutil.disk_usage('/').percent)

    def __str__(self):
        def _table():
            lis = self.disk.items()
            header_for_Disk = '|{:*^60}|'.format('DISK') + '\n'
            header_for_Disk += '|' + '_' * 60 + '|' + '\n'
            for r in lis:
                header_for_Disk += '|{:^30}'.format(r[0]) + '|{:^29}|'.format(r[1]) + '\n'
                header_for_Disk += '|' + '_' * 60 + '|' + '\n'

            return header_for_Disk

        return _table()


def main():
    _CPU = CpuInfo()
    _CPU.get_data()
    print(_CPU)

    _VIRT_mem = VirtMem()
    _VIRT_mem.get_data()
    print(_VIRT_mem)

    _DISK = DiskInfo()
    _DISK.get_data()
    print(_DISK)


if __name__ == '__main__':
    main()
