import tensorflow as tf

# Not currently woking on tf 2.0
# global_variables_initializer() was deprecated


def network(bVal, cVal):

    # first, create a TensorFlow constant
    const = tf.constant(2.0, name="const")

    # create TensorFlow variables
    b = tf.Variable(bVal, name='b')
    c = tf.Variable(cVal, name='c')

    # now create some operations
    d = tf.add(b, c, name='d')
    e = tf.add(c, const, name='e')
    a = tf.multiply(d, e, name='a')
    # setup the variable initialisation
    init_op = tf.global_variables_initializer()

    # start the session
    with tf.Session() as sess:
        # initialise the variables
        sess.run(init_op)
        # compute the output of the graph
        a_out = sess.run(a)
        print("Variable a is {}".format(a_out))


if __name__ == "__main__":
    network(10.0, 20.0)
