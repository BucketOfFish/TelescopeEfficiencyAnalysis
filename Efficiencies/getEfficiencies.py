import ROOT
import numpy as np
import h5py as h5

files = [[1644, 1645, 1646, 1647], # 1000, 0
    [1630, 1631, 1632, 1633, 1634], # 1000, 20
    [1618, 1619, 1620, 1621], # 1000, 60
    [1606, 1607, 1608, 1609], # 1000, 100
    [1593, 1594, 1595, 1596, 1597], # 1000, 140
    [1648, 1649, 1650, 1651], # 2000, 0
    [1635, 1636, 1637, 1638], # 2000, 20
    [1622, 1623, 1624, 1625], # 2000, 60
    [1610, 1611, 1612, 1613], # 2000, 100
    [1598, 1599, 1600, 1601], # 2000, 140
    [1639, 1640, 1641, 1642, 1643], # 3000, 20
    [1626, 1627, 1628, 1629], # 3000, 60
    [1614, 1615, 1616, 1617], # 3000, 100
    [1602, 1603, 1604, 1605]] # 3000, 140

saveFile = h5.File("efficiencies.h5", "w")
datasetThresholdEfficiency = [0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5]

for index, dataset in enumerate(files):

    sumTracksTotal = 0
    sumTracksPass = 0
    pixelEfficiencies = []

    for fileN in dataset:

        file0 = ROOT.TFile("run00"+str(fileN)+"-match-hists.root")
        Efficiency = file0.Get("Efficiency")
        tracksTotal = Efficiency.Get("h35-TracksTotal")
        tracksPass = Efficiency.Get("h35-TracksPass")
        for i in range(16, 64):
            if (i==39 or i==40): continue
            for j in range(36, 335):
                if tracksTotal.GetBinContent(i,j) != 0:
                    pixelEfficiency = tracksPass.GetBinContent(i,j)/tracksTotal.GetBinContent(i,j)
                    pixelEfficiencies.append(pixelEfficiency)
                    if pixelEfficiency > datasetThresholdEfficiency[index]:
                        sumTracksTotal += tracksTotal.GetBinContent(i,j)
                        sumTracksPass += tracksPass.GetBinContent(i,j)
                else:
                    pixelEfficiencies.append(0)

    saveFile.create_dataset("dataset_"+str(index)+"_pixelEfficiencies", data=pixelEfficiencies)
    saveFile.create_dataset("dataset_"+str(index)+"_efficiency", data=float(sumTracksPass)/sumTracksTotal)
    print float(sumTracksPass)/sumTracksTotal

saveFile.close()
