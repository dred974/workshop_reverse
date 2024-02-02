import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        save = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Write some code here

        save[0x2598] = 0x84
        save[0x2599] = 0x8F
        save[0x259A] = 0x88
        save[0x259B] = 0x93
        save[0x259C] = 0x84
        save[0x259D] = 0x82
        save[0x259E] = 0x87
        checksum = 0xff
        for i in save[0x2598:0x3523]:
            checksum -= i
        save[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(save)