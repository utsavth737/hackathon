import os
import gzip
import bz2
import lzma

filename = 'dummy.txt'
compressed_filename = filename + '.compressed'

# Get the original file size
original_size = os.path.getsize(filename)
print(f"Original file size: {original_size} bytes")

# Gzip compression
with open(filename, 'rb') as f_in, gzip.open(compressed_filename + '.gz', 'wb') as f_out:
    f_out.writelines(f_in)

# Get the Gzip compressed file size
gzipped_size = os.path.getsize(compressed_filename + '.gz')
print(f"Gzip compressed file size: {gzipped_size} bytes")

# Bzip2 compression
with open(filename, 'rb') as f_in, bz2.open(compressed_filename + '.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

# Get the Bzip2 compressed file size
bzipped_size = os.path.getsize(compressed_filename + '.bz2')
print(f"Bzip2 compressed file size: {bzipped_size} bytes")

# LZMA compression
with open(filename, 'rb') as f_in, lzma.open(compressed_filename + '.xz', 'wb') as f_out:
    f_out.writelines(f_in)

# Get the LZMA compressed file size
xz_size = os.path.getsize(compressed_filename + '.xz')
print(f"LZMA compressed file size: {xz_size} bytes")

print(f"File '{filename}' compressed using gzip, bzip2, and LZMA and saved as '{compressed_filename}.gz', '{compressed_filename}.bz2', and '{compressed_filename}.xz'.")
