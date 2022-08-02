# @version ^0.3.3

## Using a dynamic array

nums: DynArray[uint256, 3]

@external
def ___init__():
    self.nums.append(11)  # equivalent to Solidity's push
    self.nums.append(22)
    self.nums.append(33)
    self.nums.append(44)

    self.nums.pop()
    self.nums = []
    self.nums = [1, 2, 3]

@external
@pure
def examples(xs: DynArray[uint256, 5]) -> DynArray[uint256, 8]:
    ys: DynArray[uint256, 8] = [1, 2, 3]
    for x in xs:
        ys.append(x)
    return ys

@external
@pure
def filter(addrs: DynArray[address, 5]) -> DynArray[address, 5]:
    nonzeros: DynArray[address, 5] = []
    for addr in addrs:
        if addr != ZERO_ADDRESS:
            nonzeros.append(addr)
    return nonzeros