#This script is to check for violations of the minimum image convention

import MDAnalysis as mda
import numpy as np


print('Enter your .gro file name:')
gro_file = input()

u=mda.Universe('TMD_KET_POPC.gro') 
prot=u.select_atoms('protein') 

prot_x=[]
prot_y=[]
prot_z=[]

#obtain all coordinates in x,y and z for the protein and store in
#repsective individual arrays
for shmleh in prot.positions:
    prot_x.append(shmleh[0])
    prot_y.append(shmleh[1])
    prot_z.append(shmleh[2])

#extract the PBC coordinates from the last line of the gro file of interest
with open(gro_file) as f:
    for line in f:
        pass
    last_line = line

#as these coordinates are extracted initially as a string, in the following lines
#you are converting this to a float for each x,y,z of the pbc
#Multiply by 10 to convert from nm to angstrom unit.
pbc=str.split(last_line)
pbc_x=np.float(pbc[0])*10
pbc_y=np.float(pbc[1])*10
pbc_z=np.float(pbc[2])*10

#by taking the difference between the largest and smallest coordinate in x,y and z
#you can obtain the dimensions of the protein
prot_x_length=max(prot_x)-min(prot_x)
prot_y_length=max(prot_y)-min(prot_y)
prot_z_length=max(prot_z)-min(prot_z)

#the difference between the dimensions of the protein and the PBC box
#gives you the size of the buffer in each direction.
x_buffer=prot_x_length-pbc_x
y_buffer=prot_y_length-pbc_y
z_buffer=prot_z_length-pbc_z

print(x_buffer)
print(y_buffer)
print(z_buffer)

