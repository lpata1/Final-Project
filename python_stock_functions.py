###
""" 
This is all of the Python Functions that I will be using and testing for the project
"""
###
import math


def find_NPER(RATE, PV, PMT, FV=0):
    """
    This funntion finds the amount of periods when given RATE, PV, PMT, and FV
    """
    if RATE == 0:
        return -(PV+FV) / PMT
    else:
        return math.log((PMT-FV*RATE) / (PMT+PV*RATE), 1+RATE)


def find_RATE(NPER, PV, PMT, FV):
    """
    This function finds the rate when given NPER, PV, PMT, and FV
    """
    import numpy_financial as npf
    RATE = npf.rate(nper=NPER, pv=-PV, pmt=PMT, fv=FV)
    return f'{RATE:%}'


def find_PV(NPER, RATE, PMT, FV=0):
    """
    This fucntion finds the present value when given NPER, RATE, PMT, and FV
    """
    PV = PMT*((1-(1+RATE)**(-NPER))/RATE)
    PV += FV / (1+RATE)**NPER
    return PV


def find_PMT(NPER, RATE, PV, FV=0):
    """
    This function finds the payment when given NPER, RATE, PV, and FV
    """
    PV = -PV
    if RATE == 0:
        return -(PV+FV) / NPER
    else:
        return -(RATE * (FV+PV*(RATE+1)**NPER) / ((RATE+1)**NPER - 1))


def find_FV(NPER=0, RATE=0, PV=0, PMT=0):
    """
    This fucntion finds future/face value when given NPER, RATE, PV, and PMT
    """
    FV = PV*(1 + RATE/100) ** NPER + PMT * \
        ((1+RATE/100)**NPER-1) * (1+RATE/100) ** -1
    return FV


def main():
    print()
    # print(find_NPER(.05, 1000, 50, 900)) #Test all of these with excel or calculator
    # print(find_RATE(10, 1000, 50, 0))
    # print(find_PV(10, .05, 50, 0))
    # print(find_PMT(10, .05, 1000, 0))
    # print(find_FV(10, .05, 100, 50))


if __name__ == '__main__':
    main()
