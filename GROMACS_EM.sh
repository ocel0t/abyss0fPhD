#! /bin/bash

# GROMACS 4.5.5 EM script for peptides, using parallel processing
# Tamás Milán Nagy @2017

echo "Specify base_name, please:  "
read basename
echo "To specify disulfide bonds, type '-ss', or press execute"
read disulfide
echo "To specify lysine sidechain protonation, type '-lys', or press execute"
read lysine
echo "Set box size (nm):  "
read boxsize
echo "Specify file name for solvent (.gro):   "
read solventbox
echo "Set CPU number:  "
read CPU
pdb2gmx -f $basename.pdb -o $basename.gro -p $basename.top $disulfide $lysine &&
editconf -f $basename.gro -o $basename.box.gro  -box $boxsize &&
genbox -cp $basename.box.gro -cs $solventbox.gro -p $basename.top -o $basename.gen.gro &&
echo "Check the topology, then press a key to continue"
read key
echo "Specify EM input (.mdp) file name:   "
read em
grompp -f $em.mdp -o $em -c $basename.gen.gro -p $basename.top &&
mpirun -np $CPU mdrun_mpi -v -s $em -o $em -e $em -c $basename.em.gro -g emlog > $basename.em.log &&  
while true; do
    read -p "Generate PDB? (y/n)" yn
    case $yn in
        [Yy]* ) trjconv -f $basename.em.gro -s $em.tpr -o $basename.em.pdb; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


