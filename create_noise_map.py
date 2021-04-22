import sys
from noise import pnoise2, snoise2

# inital code came from 2dtexture.py example from noisepy on github 
# https://github.com/caseman/noise/blob/master/examples/2dtexture.py

def create_noise_map(octaves):
    biome = open("biome.pgm", 'wt')
    foliage = open("foliage.pgm", 'wt')

    width = 500
    height = 500

    biomefreq = 16.0 * octaves[0]
    biome.write('P2\n')
    biome.write('%s %s\n' % (width, height))
    biome.write('255\n')

    foliagefreq = 20.0 * octaves[1]
    foliage.write('P2\n')
    foliage.write('%s %s\n' % (width, height))
    foliage.write('255\n')

    for y in range(width):
        for x in range(height):
            biome.write("%s\n" %
                        int(snoise2(x / biomefreq, y / biomefreq, octaves[0]) * 127.0 + 128.0))

    for y in range(width):
        for x in range(height):
            foliage.write("%s\n" % int(
                snoise2(x / foliagefreq, y / foliagefreq, octaves[1]) * 127.0 + 128.0))

    biome.close()
    foliage.close()
