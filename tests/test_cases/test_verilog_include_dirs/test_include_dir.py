import cocotb


# The purpose of this test is just to complete an elobation cycle up to time 0, before simulation
# If it fails to get to this point then the addition of the include dirs failed!
@cocotb.test()
async def test_noop(_):
    pass
