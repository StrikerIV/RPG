import sys
from noise import pnoise2, snoise2

def create_noise_map(octaves):
    biome = open("biome.pgm", 'wt')
    terrain = open("terrain.pgm", 'wt')

    width = 500
    height = 500

    biomefreq = 16.0 * octaves[0]
    biome.write('P2\n')
    biome.write('%s %s\n' % (width, height))
    biome.write('255\n')

    terrainfreq = 20.0 * octaves[1]
    terrain.write('P2\n')
    terrain.write('%s %s\n' % (width, height))
    terrain.write('255\n')

    for y in range(width):
        for x in range(height):
            biome.write("%s\n" %
                        int(snoise2(x / biomefreq, y / biomefreq, octaves[0]) * 127.0 + 128.0))

    for y in range(width):
        for x in range(height):
            terrain.write("%s\n" % int(
                snoise2(x / terrainfreq, y / terrainfreq, octaves[1]) * 127.0 + 128.0))

    biome.close()
    terrain.close()
