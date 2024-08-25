from mace.calculators import mace_mp
from ase.md import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import read, write
from ase import units
from ase.optimize import BFGS
from ase.constraints import FixAtoms

macemp = mace_mp() # return the default medium ASE calculator equivalent to mace_mp(model="medium")
#macemp = mace_mp(model="large") # return a larger model
#macemp = mace_mp(model="https://tinyurl.com/y7uhwpje") # downlaod the model at the given url
#macemp = mace_mp(dispersion=True) # return a model with D3 dispersion correction
atoms = read("wet-nanoribbon.lammps-data")

atoms.calc = macemp

print("Starting otimization")
dyn = BFGS(atoms)
dyn.run(fmax=0.05,steps=100)

print("Optimization done!")

write("wet-nanoribbon-min.lammps-data",atoms)

# Initialize velocities.
T_init = 330  # Initial temperature in K
MaxwellBoltzmannDistribution(atoms, T_init * units.kB)

print("Starting MD")
# Set up the Langevin dynamics engine for NVT ensemble.
dyn = Langevin(atoms, 0.5 * units.fs, T_init * units.kB, 0.001)
def write_frame():
        dyn.atoms.write('md.xyz', append=True)
dyn.attach(write_frame, interval=100)

#Fix ribbons atoms
c = FixAtoms(indices=[745,795])
atoms.set_constraint(c)

n_steps = 2000000 # Number of steps to run
dyn.run(n_steps)
print("MD done!")

write("wet-nanoribbon-final.lammps-data",atoms)
