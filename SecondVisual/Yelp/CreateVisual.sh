echo ""
echo ""
echo "###################################################################################"
echo ""
echo "SECOND VISUALIZATION CREATION FOR YELP"
echo ""
echo "To update the topic words for model, copy the following map into affinityPlot.html: "
echo ""
Python topicWordsToJSMap.py
echo ""
echo "###################################################################################"
echo ""
read -n1 -p "Open affinityPlot.html? [y,n] " doit 
case $doit in  
  y|Y) vi YelpAffinityPlot.html;;
  n|N) echo ;; 
  *) echo ;; 
esac
echo ""
read -p "Choose int value for top K: " topK
Python Affinity.py $topK
echo ""
read -n1 -p "Open the visual? [y,n] " doit 
case $doit in  
  y|Y) open YelpAffinityPlot.html -a firefox;; 
  n|N) echo ;; 
  *) echo ;; 
esac
echo ""
echo "###################################################################################"
echo ""