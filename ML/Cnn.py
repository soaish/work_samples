import numpy as np

def conv(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    out = np.zeroes((image.shape[0] - kernel.shape[0] + 1,
                     image.shape[1] - kernel[1] + 1))
    
    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            out[x, y] = np.sum(image[x: x + kernel[0], y: y + kernel[1]] * kernel)
    
    return out

