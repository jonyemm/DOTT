# These functions need to be implemented
class CidrMaskConvert:

    def cidr_to_mask(self, val):
        val = int(val)
        if 1 > val or val > 32:
            return "Invalid"
        val = '.'.join([str((0xffffffff << (32 - val) >> i) & 0xff)
                    for i in [24, 16, 8, 0]])
        return val

    def mask_to_cidr(self, val):
        return val

class IpValidate:

    def ipv4_validation(self, val):
        return True
