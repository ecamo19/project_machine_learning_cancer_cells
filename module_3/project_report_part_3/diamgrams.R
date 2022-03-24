

library(DiagrammeR)
grViz("digraph{

      graph[rankdir = LR]
  
      node[shape = rectangle, style = filled]
      A[label = 'Step 5: KNN and 10-fold Crossvalidation: \n4_knn.py'] 
      
      
     subgraph cluster_4 {
        graph[shape = rectangle]
        style = rounded
        bgcolor = Coral
        
        label = 'Step 4: Feature Extraction: \n2_extract_distinctive_features.py'
    	node[fillcolor = LemonChiffon, margin = 0.1]
    	B[label = ' • Area
    				• Perimeter 
    				• Orientation
    				• Eccentricity
    				• Convex_area
    				• Centroid
    				• Major axis length
    				• Minor axis length']}
  
      subgraph cluster_3 {
        graph[shape = rectangle]
        style = rounded
        bgcolor = Cyan
        
        label = 'Step 3: Image Segmentation \n1_image_enhancement_segmentation.py'
        node[fillcolor = LemonChiffon, margin = 0.1]
        C[label = 'Region Based Watershed algorithm']}
  
	 subgraph cluster_2 {
        graph[shape = rectangle]
        style = rounded

        
        label = 'Step 2: Edge detection \n1_image_enhancement_segmentation.py'
        node[shape = folder, fillcolor = LemonChiffon, margin = 0.1]
        E[label = ' • Sobel filter']}
	
  
      subgraph cluster_1 {
        graph[shape = rectangle]
        style = rounded
        bgcolor = Violet
        
        label = 'Step 1: Image Enhancement \n1_image_enhancement_segmentation.py'
        node[shape = folder, fillcolor = LemonChiffon, margin = 0.1]
        D[label = '• Median filter
        • Dilation 
        • Gaussian filter']}
      
  
      subgraph cluster_0 {
        graph[shape = rectangle]
        style = rounded
        bgcolor = Gold
    
        label = 'Data Source: .BMP cancer images'
        node[shape = folder, fillcolor = LemonChiffon, margin = 0.1]
        F[label = '
• 50 columnar epithelial cells
• 50 parabasal squamous epithelial cells
• 50 intermediate squamous epithelial cells
• 49 superficial squamous epithelial cells
• 100 mild nonkeratinizing dysplastic cells
• 100 moderate nonkeratinizing dysplastic cells
• 100 severe nonkeratinizing dysplastic cells']}
      edge[color = black, arrowhead = vee, arrowsize = 1.25]
      B -> A
      C -> B
      D -> E
      F -> D
      E	-> C
      
      }")
