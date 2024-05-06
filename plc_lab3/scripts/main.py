import time
from pyModbusTCP import utils
from pyModbusTCP.client import ModbusClient


def read_int16(addr):
    regs = c.read_holding_registers(reg_addr=addr, reg_nb=1)
    hex_uint = utils.get_list_2comp(regs, 16)
    return hex_uint[0]


c = ModbusClient(host='192.168.1.150', port=502, auto_open=True)

while True:
    if c.is_open:
        temp = read_int16(60200) / 10
        hum = read_int16(60201)
        val = int(input('type int:'))
        val = min(24000, max(0, val))
        if c.write_single_register(62200, val):
            print("ok")
        print(temp, hum)
    else:
        c.open()
    time.sleep(1)
