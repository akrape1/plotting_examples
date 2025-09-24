# plotting_examples

The included Jupyter notebook gives additional examples of making basic plots needed to work on upcoming exercises.  

Exercise 1:
- Complete cells at the bottom of the notebook and include your updated notebook in your repo.

The most convenient way to work on the notebook on Rivanna is to spin up a Jupyterlab session after making a local clone of your repository.  Make sure to select the Phys56xx kernel.

Exercise 2: 

This repo also contains basic examples of using ROOT in your C++ or Python programs to generate plots.  To build the C++ program, first make sure you are in the phys56xx environment, then type ```make```.  This will create a program called cpp_example. Run the program with ```./cpp_program```.  The equivalent Python example can be run using ```python python_example.py```. 

The C++ example is more advanced.  This is provided as a first example of one way to incorporate graphing in a compiled C++ program.  The ```Makefile``` contains the necessary definitions to build the program.  These definitions include the location of header files so the compiler can check that the ROOT classes are being used properly and the location of the shared libraries so the linker can utilize the precompiled code in your program.  You will not be responsible for writing Makefiles from scratch in this class, examples will be provided as needed.  Run and observe the output of this code.

- Write a python program ```myplots.py``` that uses Matplotlib/numpy, etc. to generate the plots shown in the C++ example (canvas1_py.png, canvas2_py.pdf) .  Push these to your repo.

Exercise 3 (PHYS5630 only):

- Modify both the C++ and Python examples as follows 
  - Turn each of the Gaussian distributions into a 2D Gaussian with the same $\mu, \sigma$ in each dimension as in the original example
  - Similarly include 2D versions of the background distributions
  - For the C++ version, include a second build definition to in the Makefile to build the cpp_example2.cpp program.
  - For the Python version you may use either ROOT or Matplotlib, etc.
  - Output the following 2 files, one from each program: ```canvas2d_py.png``` and ```canvas2d_cpp.png```, and include these in your repo.  In this case you only need to save the second plot containing 4 panels.

(Use program names: ```cpp_example2.cpp``` , ```python_example2.py``` and push these to your github repo)


plotting_examples.ipynb - I had to do this work locally on my jupyter lab because VSCode is giving me issues with the 56xx kernel so I deleted the OG file and replaced it with a copy that I filled everything out in on my local build. 

myplots.py - The instructions seem to imply we have to use matplotlib instead of root since it would be pretty redundant to just translate root cpp into pyroot. this script does all the plotting with pyplot. first it generates canvas1_py.png which is just a random gaussian with error bars. the second part creates 3 more gaussian (offset, offset2, and double gaussian). i then made a function to help with plotting. this half of the code is used to generate canvas2_py.pdf. This exercise taught me to only use root from now on lol

cpp_example2.cpp - The translation from 1D to 2D is pretty obvious. My biggest change came from altering how you fill Gaussians which is using rand.Gaus(mu, std dev) instead of the fpeak thing given in the example. There is a difference when it comes to the double gaussian. In the 1D example, the extra gaussian is centered at 1 with a std dev of 20, so a lot of entries simply miss the bins when filling. This issue is significantly worsened in the 2d case, so h1 and h4 looked the same. So i changed it to center the second gaussian at 100, not 1. I also changed my main method at the end because i don't care about the interactive stuff

Makefile - I copied the cpp_example lines and just threw a 2 on the end. 

python_example2.py - I used pyroot, so it was just switching syntax from cpp to python. Same thing, the h4 plot is weird, so switched that second gaussian again.

Note: I also modified the original python_example and cpp_example scripts to shift the mean of the double gaussian to 100. I was having some issues with this running properly (Bob was also a bit confused at it) so the plots generated from these scripts aren't quite right. mine are good to go for the actual exercises