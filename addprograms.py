__author__ = 'trueutkarsh'
import django
from database.models import program
with open('database/input_programmes.csv') as csv:
	for x in csv:
	    y=x.split(',')
	    y[2]=y[2][:-2]            
	    prog=program()
	    prog.name=y[0]
	    prog.sancstrength=int(y[1])
	    prog.currstrength=int(y[2])
	    prog.save()


