import ROOT as r

def python_example2(samples=10000):
    r.gStyle.SetOptStat(0)

    rand = r.TRandom3(12345)

    h1 = r.TH2F("h1", "2D random gauss;x;y", 100, 50, 150, 100, 50, 150)
    for _ in range(samples):
        x = rand.Gaus(100, 6)
        y = rand.Gaus(100, 6)
        h1.Fill(x, y)

    h2 = h1.Clone("h2")
    h2.SetTitle("Gauss+offset;x;y")
    for _ in range(samples // 3):
        x2 = rand.Uniform(50, 150)
        y2 = rand.Uniform(50, 150)
        h2.Fill(x2, y2)

    h3 = h1.Clone("h3")
    h3.SetTitle("Gauss+offset2;x;y")
    base2 = r.TF1("base2", "1/x/x", 1, 11)
    for _ in range(samples * 30):
        x3 = base2.GetRandom() * 10 + 40
        y3 = base2.GetRandom() * 10 + 40
        h3.Fill(x3, y3)

    h4 = h1.Clone("h4")
    h4.SetTitle("Double Gaussian;x;y")
    for _ in range(samples // 2):
        x4 = rand.Gaus(100, 20)
        y4 = rand.Gaus(100, 20)
        h4.Fill(x4, y4)

    c1 = r.TCanvas("c1", "Canvas1", 1000, 800)
    c1.Divide(2,2)
    c1.cd(1)
    h1.Draw("COLZ")
    c1.cd(2)
    h2.Draw("COLZ")
    c1.cd(3)
    h3.Draw("COLZ")
    c1.cd(4)
    h4.Draw("COLZ")

    c1.Update()
    c1.SaveAs("canvas2d_py.png")


if __name__ == "__main__":
    python_example2(10000)