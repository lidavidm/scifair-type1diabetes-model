clean:
	rm *-gnuplot-*
	rm *.tuc
	rm *.log
	rm *.pdf
	rm *.dat
	rm *.dat.*

time_diagrams:
	exec ./time_diagrams_xppaut.sh
	python rk4_ode.py
	context time_diagrams.tex

bifurcation_diagrams:
	@echo "XPP will now open. Generate and save the bifurcation diagram data."
	@read -p "Press Enter to continue..."
	-./xppaut -runnow mk_static.ode
	python bifurcation_diagrams.py
	context bifurcation_diagrams.tex
