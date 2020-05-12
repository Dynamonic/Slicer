# Slicer
Basic slicer for additive manufacturing toolpaths

## Slice Test
Used for taking one layer of geometry and turning it into a toolpath for a WAAM system  
How to use:  
1.  You can create a Toolpath object which specifies the .txt filename in the init  
2.  Doing Toolpath.(pathtype) (raster, contour, hybrid) should send out a .txt file using the proper pathtype  
    **NOTE:** Currently only raster is setup to work  

## Slice Vis
Used for visualizing the toolpaths that come out of the Slice Test  
How to use:  
1. Have matplotlib installed (dependancy)  
2. Create a visualizer object  
3. Load the .txt toolpath file with Visualizer.load("FILENAMEHERE.txt")  
4. To visualize with lines run Visualizer.run() / To visualize with arrows run Visualizer.run(0)  

If there are any questions do not hesitate to message me.    