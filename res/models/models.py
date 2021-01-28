import sys
import os
sys.path.append('/data/graphics/toyota-pytorch/training_scaffold_own/res/')
import torchvision

print('Models are being loaded from: %s'%os.getcwd())

def get_model(MODEL_ARCH, NUM_CLASSES):
    if MODEL_ARCH == 'CustomCNN':
        from models.CustomCNN import CustomCNN
        return CustomCNN(num_classes = NUM_CLASSES)
    if MODEL_ARCH == '<your_model_file>':
        ##### Add code to Load your model ####
        pass