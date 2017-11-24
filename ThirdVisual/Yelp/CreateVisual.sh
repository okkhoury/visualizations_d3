echo ""
echo ""
echo "###################################################################################"
echo ""
echo ""
echo "THIRD VISUALIZATION CREATION"
echo ""
Python convertDataToJSON.py
echo ""
echo "###################################################################################"
echo ""
echo ""
read -n1 -p "Open the visual? [y,n]" doit 
case $doit in  
  y|Y) open individualClusterPlot.html -a firefox;; 
  n|N) echo ;; 
  *) echo ;; 
esac
echo ""
echo ""
