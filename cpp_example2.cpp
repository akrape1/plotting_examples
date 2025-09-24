#include "TApplication.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TRandom3.h"
#include "TH2F.h"
//#include <cstdlib>
//#include <cmath>
//#include <iostream>

using namespace std;
using namespace ROOT::Math;

void cpp_example2(int samples=10000){
    //I did all colormaps and we definitely don't want the stats box over the bins so turn those off
    gStyle->SetOptStat(0);
    TRandom3 rand(12345); 

    auto *h1 = new TH2F("h1", "2D random gauss;x;y", 100, 50, 150, 100, 50, 150);
    //i dont like the way the 1d example fills random gaussians with that peak stuff. i prefer this for loop
    for (int i=0; i<samples; i++) {
        double x = rand.Gaus(100, 6);
        double y = rand.Gaus(100, 6);
        h1->Fill(x, y);
    }

    auto *h2 = (TH2F*) h1->Clone("h2");
    h2->SetTitle("Gauss+offset;x;y");
    //offset by adding points from a uniform distribution. once again for loop
    for (int i=0; i<samples/3; ++i){
        double x2 = rand.Uniform(50, 150);
        double y2 = rand.Uniform(50, 150);
        h2->Fill(x2,y2);
    }
    
    auto *h3 = (TH2F*) h1->Clone("h3");
    h3->SetTitle("Gauss+offset2;x;y");
    auto base2 = new TF1("base2","1/x/x",1,11);
    //i took this straight from the example pretty much
    for (int i=0; i<samples*30; ++i){
        double x3 = base2->GetRandom()*10+40;
        double y3 = base2->GetRandom()*10+40;
        h3->Fill(x3,y3);
    }

    //this guy looks the same as h4 do the range of bins. this effect is less important in 1d. ask for help here
    auto *h4 = (TH2F*) h1->Clone("h4");
    h4->SetTitle("Double Gaussian;x;y");
    for (int i=0; i<samples/2; ++i){
        double x4 = rand.Gaus(100,20);
        double y4 = rand.Gaus(100,20);
        h4->Fill(x4,y4);
    }

    //i prefer to do all my plotting in one spot, so here it is
    auto c1 = new TCanvas("c1","Canvas1");
    c1->Divide(2,2); 
    c1->cd(1);
    h1->Draw("COLZ");
    c1->cd(2);
    h2->Draw("COLZ");
    c1->cd(3);
    h3->Draw("COLZ");
    c1->cd(4);
    h4->Draw("COLZ");

    c1->Update();
    c1->SaveAs("./canvas2d_cpp.png");

}

int main(int argc, char **argv) {
    int samples = 10000;             // default
    if (argc > 1) samples = atoi(argv[1]);
    cpp_example2(samples);            // call your plotting function
    return 0;                         // exit
}
  