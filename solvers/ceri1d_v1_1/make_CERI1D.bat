ifort 	src\general.f90 ^
	src\hqsiki_out.f90 ^
	src\supplementation.f90 ^
	src\eq_cross.f90 ^
	src\image.f90 ^
	src\IRS.f90 ^
	src\number.f90 ^
	src\Ice_Break.f90 ^
	src\alpha_cal.f90 ^
	src\n_R.f90 ^
	src\Ice.f90 ^
	src\Ice_Flow.f90 ^
	src\Bed_Flow.f90 ^
	src\iRIC_inout.F90 ^
	src\CERI1DIce.f90 ^
	src\unsteady.f90 ^
	lib\iriclib.lib ^
	lib\cgnsdll.lib ^
	lib\msvcprt.lib ^
	src\files.f90 ^
	src\Tw.f90 ^
	src\set_grid_from_riversurvey.F90 ^
	/MD -o CERI1D.exe

del *.obj 
del *.mod 

