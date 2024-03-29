import caption_generator
from keras.callbacks import ModelCheckpoint
import os

def train_model(weight = None, batch_size=32, epochs = 10):

    cg = caption_generator.CaptionGenerator()
    model = cg.create_model()

    if weight != None:
        model.load_weights(weight)

    counter = 0
    p = 'weights-improvement-{epoch:02d}.hdf5'
    file_name = os.path.join(os.path.split(os.path.dirname(__file__))[0], p) 
    checkpoint = ModelCheckpoint(file_name, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    model.fit(cg.data_generator(batch_size=batch_size), steps_per_epoch=cg.total_samples/batch_size, epochs=epochs, verbose=2, callbacks=callbacks_list)
    try:
        model.save(os.path.join(os.path.split(os.path.dirname(__file__))[0], "Models", "WholeModel.h5"), overwrite=True)
        model.save_weights(os.path.join(os.path.split(os.path.dirname(__file__))[0], "Models", "Weights.h5"),overwrite=True)
    except:
        print("Error in saving model.")
    print("Training complete...\n")

if __name__ == '__main__':
    train_model(epochs=50)
