SECONDS=0
python3 Generator.py
#make
./main testvvv.txt 200 75
./Top_1_freq
./Top_5_freq
./Top_15_freq
./Top_25_freq
./Top_40_freq
python3 line_delete.py
#python3 Threshold_calculation_final.py
python3 findingpathlengths_forAPM.py
#python3 agreement_percentage_calculation.py
#python3 agreement_percentage_calculation_big.py
python3 frequency_distribution.py
python3 strict_measure_calculation_dest.py
#python3 strict_measure_fullpath.py
python3 strict_measure_fullpath_big.py
#python3 frequency.py
duration=$SECONDS
echo "$(($duration / 3600)) hours, $((($duration / 60) % 60)) minutes and $(($duration % 60)) seconds elapsed."
