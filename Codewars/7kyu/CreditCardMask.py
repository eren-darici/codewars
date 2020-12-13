def maskify(cc):
    maskified = str()
    if len(cc) >= 4:
        for i in cc[0:-4]:
            maskified+="#"
        for j in cc[-4:]:
            maskified+=j
        return maskified
    else:
        return cc