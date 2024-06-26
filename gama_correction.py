def gamma_adjust(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table=np.array([((i/255)**invGamma)*255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)
