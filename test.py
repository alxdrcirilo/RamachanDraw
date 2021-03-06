from RamachanDraw import fetch, phi_psi, plot

# Local file
file = 'data/4hhb.pdb'
# Plot from local file and show
plot(pdb_file=file, show=True)
# Plot from downloaded file and save with alpha argument set to 0.5
plot(pdb_file=fetch('2bxc'), show=False, save=True, alpha=0.5)
# Get phi and psi angles
angles = phi_psi(pdb_file=file)

# Batch of PDB ids
batch = ['1mbn', '4hhb', '1aoi', '2jip']
# Get phi and psi angles for each pdb in the batch
angles = phi_psi(pdb_file=fetch(batch), return_ignored=True)
# Plot from downloaded files and show
plot(pdb_file=fetch(batch), show=True, save=False)
