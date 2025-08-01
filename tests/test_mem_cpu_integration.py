import pytest
from generated.memory import Memory
from generated.cpu import CPU

def test_direct_memory_write_read():
    mem = Memory()
    mem.write(0xC000, 0x42)
    assert mem.read(0xC000) == 0x42

def test_cpu_memory_write_read():
    mem = Memory()
    cpu = CPU(memory=mem)
    cpu.A = 0x77
    cpu.step({"op": "LD_n8_A_ptr", "n8": 0xC080})
    cpu.A = 0x00
    cpu.step({"op": "LD_A_n8_ptr", "n8": 0xC080})
    assert cpu.A == 0x77

def test_write_rom_raises_error():
    mem = Memory()
    with pytest.raises(ValueError):
        mem.write(0x0000, 0x99)

def test_read_rom_ok():
    mem = Memory()
    _ = mem.read(0x0000)  # Should not raise

def test_write_out_of_bounds_raises_error():
    mem = Memory()
    with pytest.raises(ValueError):
        mem.write(0xFFFF, 0x01)
