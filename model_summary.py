from keras.models import load_model

# Load the model file (ensure the path is correct)
model = load_model('model.h5')

# Check the model summary to see if it loaded properly
model.summary()