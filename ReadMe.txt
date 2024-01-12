cnvrtwfm.exe v2.00
reference number: 066084200

cnvrtwfm.exe is the utility used to convert ISF files to CSV files. Supported Scopes: 

MSO4000, DPO4000, MSO3000, DPO3000, MSO2000, DPO2000, TDS3000, TDS3000B, TDS3000C Series oscilloscopes 
Normal Usage: 
cnvrtwfm -l -8- myfile.isf

Executing this command will generate a file called myfile.csv which is viewable in a spreadsheet application such as Microsoft Excel.

General Notes: 
-The csv files for waveforms with record lengths greater than 10,000 points cannot be completely loaded by some versions of Microsoft Excel.
-Peak Detect mode and Envelope mode are not supported in this release

This is a DOS prompt utility program.  It requires to execute in the DOS prompt.  
In order to bring up the DOS prompt, go to "Start" menu and then "Run".  Type in either "cmd" or "command" to bring up the DOS prompt.
Then go to the directory where you have saved the cnvrtwfm.exe and type in the following command.

usage: cnvrtwfm [flags] files
       Flags:	-p	include waveform preamble/header (default)
		-p-	exclude waveform preamble/header
		-d	include waveform data (default)
		-d-	exclude waveform data
		-8	output 8 bit data (default)
		-8-	output 16 bit data
		-b	output binary data (default)
		-b-	output ascii data
		-s	swap binary data bytes, Intel (default)
		-s-	don't swap binary data bytes
		-i	show file info
		-i-	don't show file info (default)
		-r	output raw data only
		-r-	don't output raw data (default)
		-l	output spreadsheet data only 
		-l-	don't output spreadsheet data (default)
		-m	output mathcad data only 
		-m-	don't output mathcad data (default)
		-w	output wfm files 
		-w-	don't output wfm files (default)