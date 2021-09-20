ip_addr =input('enter the ip address(xxx.xxx.xxx.xxx) \n')
cidr= int(input('enter the cidr \n'))


ip_addr = ip_addr.split(".")
print(ip_addr)

def to_mask(cidr: int):
    output = ""
    for i in range(32):
        if i < cidr:
            output += "1"
        else:
            output += "0"
        return output

print(to_mask(cidr))

def to_bin(octet:str ) -> str:
    bin_num = bin(int(octet))[2:]
    return "0"*(8 - len(bin_num)) + bin_num[2:]

output = ""
for octet in ip_addr:
    output += to_bin(octet)

print(output)