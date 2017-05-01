ifort 	..\libs\cgnsdll.lib^
	..\libs\iriclib.lib ^
	..\src\gridgen.f90 /MD -o gridgen.exe

del *.obj 
del *.mod 

