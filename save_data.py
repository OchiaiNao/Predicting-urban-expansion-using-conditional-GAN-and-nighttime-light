import rasterio as rs
from matplotlib import pyplot as plt
for i in range(0, 128):
    fp = r'night_time/night_time/night_time_'+ str(i+1) + '.tif'
    img = rs.open(fp)
    plt.imshow(img.read(1))
    name = r'night_time/night_time_jpg/night_time_'+ str(i+1) + '.jpg'
    print(name)
    plt.axis('off')
    plt.savefig(name, bbox_inches='tight')