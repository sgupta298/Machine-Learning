#!/usr/bin/python3
import tensorflow as tf
x=tf.constant([2,3])
y=tf.constant([6,9])
process=tf.add(x,y)
with tf.Session() as f:
	output=f.run(process)
	print(output)
