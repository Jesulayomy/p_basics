from datetime import datetime


def vendorOperationStatus(openTime, closeTime):
    """ Checks the operating ttiem of a vendor """

    vendorOpen = datetime.strptime(openTime, "%H:%M")
    vendorClose = datetime.strptime(closeTime, "%H:%M")
    now = datetime.now()
    nw = "{}:{}".format(now.strftime("%H"), now.strftime("%M"))
    currentTime = datetime.strptime(nw, "%H:%M")

    print(openTime, closeTime, nw)
    print(openTime > closeTime)
    if currentTime < vendorClose and currentTime > vendorOpen:
        return True
    elif vendorClose < vendorOpen:
        return True
    else:
        return False
