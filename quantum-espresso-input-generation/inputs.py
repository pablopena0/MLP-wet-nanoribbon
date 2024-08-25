import ase.io
from ase.io.espresso import write_espresso_in

input_data = {
    'calculation': 'scf',
    'input_dft': 'SCAN',
    'outdir': './',
    'tprnfor': True,
    'ecutwfc': 110,
    'conv_thr': 1e-6,
    'mixing_beta': 0.7,
    'pseudo_dir': '../../pseudo/',
    'disk_io': 'none',
    'degauss': 0.002,
}  # This flat dictionary will be converted to a nested dictionary where, for example, "calculation" will be put into the "control" section

pseudopotentials={'C':'C_ONCV_PBE_sr.upf','H':'H_ONCV_PBE_sr.upf','O':'O_ONCV_PBE_sr.upf'}


filemd='./md.xyz'   #MD simulation result of a Foundation Model simulation
outfolder='./extracted-confs-atmospheric-pressure/'

for i in range(5000,20000,100):
    atoms=ase.io.read(filemd,i)
    write_espresso_in(outfolder+f'wet-ribbon-conf-{conf}.in', atoms, input_data=input_data, pseudopotentials=pseudopotentials, format='espresso-in')
