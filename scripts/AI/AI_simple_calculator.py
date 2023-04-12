import tensorflow as tf
from tensorflow import keras

def AImultiplier(ysm, number, epochsN):

    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    model.compile(optimizer='sgd', loss='mean_squared_error')

    ys1 = 1 * ysm
    ys2 = 2 * ysm
    ys3 = 3 * ysm
    ys4 = 4 * ysm
    ys5 = 5 * ysm
    ys6 = 6 * ysm

    xs=[1, 2, 3, 4, 5, 6]
    ys=[ys1, ys2, ys3, ys4, ys5, ys6]

    model.fit(xs, ys, epochs=int(epochsN))

    prediction = float(model.predict([float(number)]))

    return prediction

def AIadder(ysm, number, epochsN):

    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    model.compile(optimizer='sgd', loss='mean_squared_error')

    ys1 = 1 + ysm
    ys2 = 2 + ysm
    ys3 = 3 + ysm
    ys4 = 4 + ysm
    ys5 = 5 + ysm
    ys6 = 6 + ysm

    xs=[1, 2, 3, 4, 5, 6]
    ys=[ys1, ys2, ys3, ys4, ys5, ys6,]

    model.fit(xs, ys, epochs=int(epochsN))

    prediction = float(model.predict([float(number)]))

    return prediction

def AIdivider(ysm, number, epochsN):

    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    model.compile(optimizer='sgd', loss='mean_squared_error')

    ys1 = 1 / ysm
    ys2 = 2 / ysm
    ys3 = 3 / ysm
    ys4 = 4 / ysm
    ys5 = 5 / ysm
    ys6 = 6 / ysm

    xs=[1, 2, 3, 4, 5, 6]
    ys=[ys1, ys2, ys3, ys4, ys5, ys6]

    model.fit(xs, ys, epochs=int(epochsN))

    prediction = float(model.predict([float(number)]))

    return prediction

def AIsubtractor(ysm, number, epochsN):

    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    model.compile(optimizer='sgd', loss='mean_squared_error')

    ys1 = 1 - ysm
    ys2 = 2 - ysm
    ys3 = 3 - ysm
    ys4 = 4 - ysm
    ys5 = 5 - ysm
    ys6 = 6 - ysm

    xs=[1, 2, 3, 4, 5, 6]
    ys=[ys1, ys2, ys3, ys4, ys5, ys6]

    model.fit(xs, ys, epochs=int(epochsN))

    print("ready")

    prediction = float(model.predict([float(number)]))

    return prediction