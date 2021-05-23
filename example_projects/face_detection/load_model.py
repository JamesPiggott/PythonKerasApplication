import tensorflow as tf

def main(_argv):
    model = tf.saved_model.load('res50_saved_model')


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass