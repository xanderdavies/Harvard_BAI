import pickle
import pathlib
current_path = pathlib.Path(__file__).parent.absolute()

print('Models are being loaded from: %s'%current_path)

def get_model(MODEL_ARCH, NUM_CLASSES):
    if MODEL_ARCH == 'CustomCNN':
        from models.CustomCNN import CustomCNN
        return CustomCNN(num_classes = NUM_CLASSES)
    if MODEL_ARCH == '<your_model_file>':
        ##### Add code to Load your model ####
        pass