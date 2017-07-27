// Just use python. C++ sucks

int fileN0 [] = {1593, 1594, 1595, 1596, 1597};
int fileN1 [] = {1598, 1599, 1600, 1601};
int fileN2 [] = {1602, 1603, 1604, 1605};
int fileN3 [] = {1606, 1607, 1608, 1609};
int fileN4 [] = {1610, 1611, 1612, 1613};
int fileN5 [] = {1614, 1615, 1616, 1617};
int fileN6 [] = {1618, 1619, 1620, 1621};
int fileN7 [] = {1622, 1623, 1624, 1625};
int fileN8 [] = {1626, 1627, 1628, 1629};
int fileN9 [] = {1630, 1631, 1632, 1633, 1634};
int fileN10 [] = {1635, 1636, 1637, 1638};
int fileN11 [] = {1639, 1640, 1641, 1642, 1643};
int fileN12 [] = {1644, 1645, 1646, 1647};
int fileN13 [] = {1648, 1649, 1650, 1651};
int* datasets [] = {fileN0, fileN1, fileN2, fileN3, fileN4, fileN5, fileN6, fileN7, fileN8, fileN9, fileN10, fileN11, fileN12, fileN13};

double avgEffs [14];
double effDist [48*299];
for (int d=0; d<14; d++) {
    double sumTracksTotal = 0.0;
    double sumTracksPass = 0.0;
    int* fileN = datasets[d];
    int nFiles = sizeof(fileN)/sizeof(fileN[0]);
    for (int n=0; n<nFiles; n++) {
        TFile* _file0 = TFile::Open(TString("run00"+to_string(fileN[n])+"-match-hists.root"));
        TDirectoryFile* Efficiency = (TDirectoryFile*)(_file0->Get("Efficiency"));
        TH2D* tracksTotal = (TH2D*)(Efficiency->Get("h35-TracksTotal"));
        TH2D* tracksPass = (TH2D*)(Efficiency->Get("h35-TracksPass"));
        for (int i=16; i<=63; i++) {
            if (i==39 || i==40) continue;
            for (int j=36; j<=334; j++) {
                sumTracksTotal += tracksTotal->GetBinContent(i,j);
                sumTracksPass += tracksPass->GetBinContent(i,j);
                if (d==0 && n==0)
                    effDist[j + i*299] = tracksPass->GetBinContent(i,j)/tracksTotal->GetBinContent(i,j);
            }
        }
    }
    avgEffs[d] = sumTracksPass/sumTracksTotal;
}
avgEffs
