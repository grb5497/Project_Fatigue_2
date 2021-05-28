#command
#target: dependency
#	action

#orange-juice: oranges
#	squeeze orangesm
PLOT_SCRIPT=project_fatigue_2/visualization/plot_script.py
LANGUAGE=python
PLOT_EXE=$(LANGUAGE) $(PLOT_SCRIPT)
RAW=data/input
PROCESSED=data/output

##plot_ae: Generate plots for all specimens
.PHONY: plot_ae
plot_ae: data/output/Plot_AE_Specimen_1-8.png data/output/Plot_AE_Specimen9.png data/output/Plot_AE_Specimens10-11.png data/output/Plot_AE_Specimen12.png

$(PROCESSED)/Plot_AE_Specimen_1-8.png: $(RAW)/AE*0[1-8].csv 
	$(PLOT_EXE) $^ $@ "Time (s)" "Cumulative Energy (J)"

$(PROCESSED)/Plot_AE_Specimen_9-11.png: $(RAW)/AE*09.csv $(RAW)/AE*1[0-1].csv
	$(PLOT_EXE) $^ $@ "Time (s)" "Cumulative Energy (J)"

$(PROCESSED)/Plot_AE_Specimen_12.png: $(RAW)/AE*12.csv
	$(PLOT_EXE) $^ $@ "Time (s)" "Cumulative Energy (J)"

.PHONY: clean
clean:
	rm -f data/output/*.png

.PHONY: help
help: Makefile
	sed -n 's/^##//p' $<
