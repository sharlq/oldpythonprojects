import tensorflow as tf


#node1 = tf.constant(3.0,tf.float32)
#node2 = tf.constant(4.0)


#print(node1,node2)

#sess = tf.Session()

#print(sess.run([node1,node2]))


#a = tf.constant(3)
#b = tf.constant(1)
#c = tf.constant(4)
#d = tf.multiply(a,b)
##f = tf.subtract(e,d)

#sess = tf.Session()
#outs = sess.run(f)
#sess.close()

#print("out={}".format(outs))

#a= tf.placeholder(tf.float32)
#b= tf.placeholder(tf.float32)

#adder_node = a+b
#sess=tf.Session()
#print(sess.run(adder_node, {a: [1,3], b:[2,4]}))


#####################################

w = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)

x= tf. placeholder(tf.float32)

linear_model = w*x +b

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(linear_model,{x:[1,2,3,4]}))
y = tf.placeholder(tf.float32)

sqaured_deltas = tf.square(linear_model - y)

loss = tf.reduce_sum(sqaured_deltas)

#print(sess.run(loss, {x:[1,2,3,4],y:[0,-1,-2,-3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)

train = optimizer.minimize(loss)

sess.run(init)

for i in range (1000):
    sess.run(train, {x:[1,2,3,4],y:[0,-1,-2,-3]})


print(sess.run([w,b]))

##############