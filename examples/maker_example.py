#!/usr/bin/env python2.7

############################
# Test case on maker gff3  #
############################

import subprocess
import os
import sys

def fill_path(file):
	path =  os.path.realpath(__file__)
	tail = path.rsplit('/',1)
	return tail[0]+"/"+file

def main():
	#FASTA file used to produce the annotation
	GENOME="maker.fa"

	# ANNOATION in gff3 FORMAT
	ANNOTATION="maker.gff3"

	#PROJECT name registered on EMBL
	PROJECT="17285"

	#Locus tag registered on EMBL
	LOCUS_TAG="MY_LOCUS_TAG"

	# species name
	SPECIES="Drosophila melanogaster"

	# Taxonomy
	TAXONOMY="INV"

	#The working groups/consortia that produced the record. No default value
	REFERENCE_GROUP="MyGroup"

	#Translation table
	TABLE="1"

	#Molecule type of the sample.
	MOLECULE="genomic DNA"

	#Create the command
	command = "EMBLmyGFF3 --rg REFERENCE_GROUP -i "+LOCUS_TAG+" -p "+PROJECT+" -m \""+MOLECULE+"\" -r "+TABLE+" -t linear -s \""+SPECIES+"\" -x "+TAXONOMY+" -o EMBLmyGFF3-maker-test.embl "+fill_path(ANNOTATION)+" "+fill_path(GENOME)
	print("Running the following command: "+command)

	#Execute the command
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	stdout, stderr = process.communicate()
	print stdout

if __name__ == '__main__':
	main()