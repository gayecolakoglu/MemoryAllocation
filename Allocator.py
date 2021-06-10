import sys
filename= str(sys.argv[1])

with open("output.txt","w",encoding="utf-8")as f:
    pass

# writeOutput() function for writing output.txt file
def writeOutput(p,lst,choice,name):
    with open("output.txt","a",encoding="utf-8")as f:
        if choice==0:
            f.write("\n")
            f.write(name)
            f.write("\n\n")
            f.write("-------------------------------------------------------\n\n")
            f.write("start")
            f.write(" => ")
            f.write(" ".join(list(map(str, lst))))
            f.write("\n\n")

        elif choice==1:
            f.write(str(p))
            f.write(" => ")
            f.write(" ".join(list(map(str, lst))))
            f.write("\n\n")

        elif choice==2:
            f.write(str(p))
            f.write(" => ")
            f.write("not allocated, must wait.")
            f.write("\n\n")


# this function is traverse memory array for every processes.
# then it puts given process to the first suitable location then pops it from process list. 
def firstFit(mList,pList):
    i=0
    writeOutput(0,mList,0,"First-Fit Memory Allocation")
    while i<len(mList) and len(pList)!=0:
        if (type(mList[i])!= str):
            p = pList[0]
            if (p <= mList[i]) :
                if(mList[i]-p > 0):
                    mList[i] = mList[i]-p
                    mList.insert(i,str(p)+'*')
                    writeOutput(p,mList,1,"First-Fit Memory Allocation")
                    pList.pop(0)                
                    i = 0
                elif(mList[i]-p == 0):
                    mList.pop(i)
                    mList.insert(i,str(p)+'*')
                    writeOutput(p,mList,1,"First-Fit Memory Allocation")
                    pList.pop(0)                
                    i = 0
                elif(mList[i]-p < 0):
                    writeOutput(p,mList,2,"First-Fit Memory Allocation")
                    pList.pop(0) 
            else:
                i+=1
                
        else:
            i+=1
        # if we travel all places and there is not any space for given process; 
        if(i==len(mList)):
            writeOutput(p,mList,2,"First-Fit Memory Allocation")
            pList.pop(0)
            i=0

# this function is traverse all spaces for every processes and keep suitable space for given process.
# And function keeps traverse all places until the and of the memory list inorder to find best(bigger enough or same as process size) location
# after all it puts given process best location then pops it from process list. 
def bestFit(mList,pList):
    i=0
    writeOutput(0,mList,0,"Best-Fit Memory Allocation")
    while(len(pList)>0):
        p = pList[0]    # process that we want to embed
        temp =sys.maxsize # temporary memory where we will place the process 
        i=0
        indexTemp=0     # index of temp
        while i<len(mList):
            if (type(mList[i])!= str):
                if(p<=mList[i] and temp>=mList[i]):
                    temp = mList[i]
                    indexTemp = i
                    i+=1
                else:
                    i+=1
            else:
                i+=1

        if(mList[indexTemp]-p >0):
            mList[indexTemp] = mList[indexTemp]-p
            mList.insert(indexTemp,str(p)+'*')
            writeOutput(p,mList,1,"Best-Fit Memory Allocation")
            pList.pop(0) 
        elif(mList[indexTemp]-p == 0):
            mList.pop(indexTemp)
            mList.insert(indexTemp,str(p)+'*')
            writeOutput(p,mList,1,"Best-Fit Memory Allocation")
            pList.pop(0)
        # if we travel all places and there is not any space for given process; 
        elif(mList[indexTemp]-p <0):
            writeOutput(p,mList,2,"Best-Fit Memory Allocation")
            pList.pop(0) 
           


# this function is traverse all spaces for every processes and keep suitable space for given process.
# And function keeps traverse all places until the and of the memory list inorder to find worst(bigger than all) location
# after all, it puts given process worst location then pops it from process list.
def worstFit(mList,pList):
    i=0
    
    writeOutput(0,mList,0,"Worst-Fit Memory Allocation")
    while(len(pList)>0):
        p = pList[0]    # process that we want to embed
        temp =0         # temporary memory where we will place the process
        i=0
        indexTemp=0     # index of temp
        while i<len(mList):
            if (type(mList[i])!= str):
                if(p<=mList[i] and temp<=mList[i]):
                    temp = mList[i]
                    indexTemp = i
                    i+=1
                else:
                    i+=1
            else:
                i+=1

        if(mList[indexTemp]-p >0):
            mList[indexTemp] = mList[indexTemp]-p
            mList.insert(indexTemp,str(p)+'*')
            writeOutput(p,mList,1,"Best-Fit Memory Allocation")
            pList.pop(0) 
        elif(mList[indexTemp]-p == 0):
            mList.pop(indexTemp)
            mList.insert(indexTemp,str(p)+'*')
            writeOutput(p,mList,1,"Best-Fit Memory Allocation")
            pList.pop(0)
        # if we travel all places and there is not any space for given process; 
        elif(mList[indexTemp]-p <0):
            writeOutput(p,mList,2,"Best-Fit Memory Allocation")
            pList.pop(0) 
            



with open(filename,"r",encoding="utf-8") as myFile:
    lines = myFile.readlines()
    lines[0] = lines[0].rstrip("\n")  
    mList = lines[0].split(",")
    pList = lines[1].split(",")
    mList = list(map(int, mList))
    pList = list(map(int, pList))
    firstFit(mList.copy(),pList.copy())
    bestFit(mList.copy(),pList.copy())
    worstFit(mList.copy(),pList.copy())
   



        

