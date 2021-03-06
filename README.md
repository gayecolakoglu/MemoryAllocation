# MemoryAllocation
 ## Contiguous Memory Allocation Algorithms

 This project involves implementing contiguous memory allocation algorithms. The program will read size of free memory partitions and size of processes from a text file and then will try to allocate a memory partition for each process using the first-fit, best-fit and worst-fit allocation algorithms.

 The implementation of this project may be completed in any programming language (although Python or Java recommended)

 The first line of the input file should contain the size of free memory partitions (in order) while the second line contains the size of processes (in order). Sample input file is shown below:

                 300,600,350,200,750,125

                 115,500,358,200,375

 The program should read the name input file as command line input and produce a text file named “output.txt” with the following example output:

 >> java Allocator memory.txt 

 >> cat output.txt

 First-Fit Memory Allocation

 -----------------------------------------------------------------------------------------------


 start  => 300 600 350 200 750 125

 115   => 115* 185 600 350 200 750 125

 500   => 115* 185 500* 100 350 200 750 125

 358   => 115* 185 500* 100 350 200 358* 392 125

 200   => 115* 185 500* 100 200* 150 200 358* 392 125

 375   => 115* 185 500* 100 200* 150 200 358* 375* 17 125



 Best-Fit Memory Allocation

 -----------------------------------------------------------------------------------------------


 start => 300 600 350 200 750 125

 115  => 300 600 350 200 750 115* 10

 500  => 300 500* 100 350 200 750 115* 10

 358  => 300 500* 100 350 200 358* 392 115* 10

 200  => 300 500* 100 350 200* 358* 392 115* 10

 375  => 300 500* 100 350 200* 358* 375* 17 115* 10


 Worst-Fit Memory Allocation

 -----------------------------------------------------------------------------------------------


 start => 300 600 350 200 750 125

 115  => 300 600 350 200 115* 635 125

 500  => 300 600 350 200 115* 500* 135 125

 358  => 300 358* 242 350 200 115* 500* 135 125

 200  => 300 358* 242 200* 150 200 115* 500* 135 125

 375  => not allocated, must wait
