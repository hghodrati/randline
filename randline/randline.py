"""

"""
import mmap


class randline():
    def __init__(self, file):
        self._file = file
        self._line_breaks = self._index_line_breaks(file)

    @staticmethod
    def _index_line_breaks(file):
        line_breaks = []
        with open(file, 'rb') as f:
            line_start = 0
            mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
            file_size = mm.size()
            while True:
                line_end = mm.find(b'\n', line_start)
                if line_end == -1:
                    break
                line_breaks.append(line_end)
                line_start = line_end + 1
        if file_size > line_breaks[-1]:
            line_breaks.append(file_size)
        print(line_breaks)
        return line_breaks

    def __getitem__(self, item):
        with open(self._file, 'rb') as f:
            mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
            line_pos = 0
            if item > 0:
                line_pos = self._line_breaks[item-1] + 1
            line_len = self._line_breaks[item] - line_pos
            mm.seek(line_pos)
            return mm.read(line_len).decode('utf-8')

    def __len__(self):
        return len(self._line_breaks)
