
import paddle


from paddle.nn import Layer
from paddle.nn import Conv2D, AvgPool2D, Conv2DTranspose
from paddle.vision.models import vgg16

class FCN8s(Layer):
    def __init__(self, num_classes = 59):
        super(FCN8s, self).__init__()
        backbone = vgg16(False)

        self.layer1 = backbone