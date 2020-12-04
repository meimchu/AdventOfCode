# def num_coins(cents):
#     coin_dict = {25: 0, 10: 0, 5: 0, 1: 0}
#     for coin in coin_dict.keys():
#         if (cents % coin) == 0:
#             amount = cents / coin
#             coin_dict[coin] = amount
#             break
#         amount = int(cents / coin)
#         coin_dict[coin] = amount
#         cents = cents - (amount * coin)
#     return coin_dict
# # print num_coins(31)

# def min_coins(cents):
#     coin_dict = {}
#     coin_list = [10, 25]
#     for coin in coin_list:
#         if (cents % coin) == 0:
#             amount = cents / coin
#             coin_dict[coin] = amount
#             break
#         amount = int(cents / coin)
#         print coin, cents, amount
#         coin_dict[coin] = amount
#         cents = cents - (amount * coin)
#     coin_dict[1] = cents
#     return coin_dict
# print min_coins(31)

# import numpy as np
# import colour
# import colour.plotting
# DCI_P3 = colour.read_image('/Users/meichu/Downloads/Italy-P3.jpg')
# sRGB = colour.RGB_to_RGB(DCI_P3, colour.models.DCI_P3_COLOURSPACE, colour.models.sRGB_COLOURSPACE)
# colour.plotting.plot_image(np.where(sRGB < 0.0, 1.0, 0.0), text_parameters={'text': 'sRGB to XYZ'})

# import colour
# import colour.plotting
# print colour.RGB_COLOURSPACES.keys()
# RGB = colour.read_image('/Users/meichu/Downloads/SonyF35.StillLife.exr')
# colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB, colourspace='ACES2065-1', colourspaces=['ACES2065-1', 'sRGB', 'DCI-P3'])
# RGB = colour.read_image('/Users/meichu/Downloads/Italy-P3.jpg')
# colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
#     RGB, colourspace='DCI-P3', colourspaces=['ACES2065-1', 'sRGB', 'DCI-P3'])

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# pts = np.array([[0.6400,0.3300], [0.3000,0.6000], [0.1500,0.0600]])
# p = Polygon(pts, closed=True)
# ax = plt.gca()
# ax.add_patch(p)
# plt.show()

# from colour.plotting import plot_chromaticity_diagram_CIE1931
# plot_chromaticity_diagram_CIE1931()

# from colour.utilities import first_item
# from colour.plotting import filter_cmfs
# cmf = 'CIE 1931 2 Degree Standard Observer'
# cmfs = first_item(filter_cmfs(cmf).values())
# print cmfs

# from colour.plotting import diagrams
# diagrams.plot_spectral_locus()
# diagrams.plot_spectral_locus(spectral_locus_colours='RGB')

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# from collections import OrderedDict
# cmfs = []
# with open('/Users/meichu/Downloads/cie-cmf.txt', 'r') as f:
#     for line in f.readlines():
#         label, X, Y, Z = line.split(' ')
#         label = int(label)
#         X = float(X)
#         Y = float(Y)
#         Z = float(Z.replace('\n', ''))
#         cmfs.append((label, X, Y, Z))
#     f.close()
# XYZdict = OrderedDict()
# for cmf in cmfs:
#     label, X, Y, Z = cmf
#     XYZdict[int(label)] = {
#         'label': int(label),
#         'X': float(X),
#         'Y': float(Y),
#         'Z': float(Z)
#     }
# plt.figure(figsize=(6,6))
# axes = plt.gca()
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# prevXY = []
# xList = []
# yList = []
# xyList = []
# coords = [390, 460, 470, 480, 490, 500, 510, 520, 540, 560, 580, 600, 620, 700]
# for count, xyz in enumerate(XYZdict):
#     X, Y, Z = XYZdict[xyz]['X'], XYZdict[xyz]['Y'], XYZdict[xyz]['Z']
#     label = XYZdict[xyz]['label']
#     try:
#         XYZMatrix = np.array([[X, Y, Z]])
#         XYZtoRGB = np.array([[3.2404542, -1.5371385, -0.4985314],
#                              [-0.9692660, 1.8760108, 0.0415560],
#                              [0.0556434, -0.2040259, 1.0572252]])
#         rgb_colour = XYZMatrix.dot(XYZtoRGB)
#         r = rgb_colour[0][0]
#         if r < 0:
#             r = 0
#         if r > 1:
#             r = 1
#         g = rgb_colour[0][1]
#         if g < 0:
#             g = 0
#         if g > 1:
#             g = 1
#         b = rgb_colour[0][2]
#         if b < 0:
#             b = 0
#         if b > 1:
#             b = 1
#         x = X/(X + Y + Z)
#         y = Y/(X + Y + Z)
#         if xyz <= 700:
#             xyList.append((x, y))
#             if xyz in coords:
#                 axes.plot(x, y, marker='o', markersize='3', color='black')
#                 axes.text(x, y, label)
#             if count > 0:
#                 plt.plot([prevXY[0], x], [prevXY[1], y],
#                          linewidth=1, color=(r, g, b))
#         prevXY = [x, y]
#     except ZeroDivisionError:
#         pass
# spectral_locus = Polygon(xyList, fill=True, closed=True)
# rgb = np.array([[0.6400,0.3300], [0.3000,0.6000], [0.1500,0.0600]])
# sRGB = Polygon(rgb, fill=False, closed=True)
# axes.add_patch(spectral_locus)
# axes.add_patch(sRGB)
# plt.show()

print 13 % (10)
