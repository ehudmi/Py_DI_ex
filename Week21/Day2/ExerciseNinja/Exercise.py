# Exercise 1 : Temperature
# Instructions
# Write a base class called Temperature.
# Implement the following subclasses: Celsius, Kelvin, Fahrenheit.
# Each of the subclasses should have a method which can convert the temperature to another type.
# You must consider different designs and pick the best one according to the SOLID Principle.


# Exercise 2: In The Quantum Realm
# Instructions
# Write a class called QuantumParticle and implement the following:
# The attributes - The particle has an initial position (x), momentum (y) and spin (p)

# The method position() - Position measurement: generate a random position (integer between 1 and 10,000)

# The method momentum() - Momentum measurement: generate a random momentum (float - a number between 0 and 1)

# The method spin() - Spin measurement: can randomly be 1/2 or -1/2

# Create a method that implements a disturbance. A disturbance occurs each time a measurement is made (e.g. one of the
# measurements method is called). Disturbance changes the position and the momentum of the particle (randomly generated)
#  and then prints ‘Quantum Interferences!!’

# Implement a meaningful representation of the particle (repr)

# Quantum Entanglement: two particle can be entangled, meaning that if I measure the spin of one of them the second one
# is automatically set to the opposite value. A quantum particle can only be entangled to another quantum particle
# (check that when you run the method !!)
# Modify as you see fit the attributes and methods of your class to fit the previous definition
# When two particles are entangled print: ‘Spooky Action at a Distance !!’
# >>>p1 = QuantumParticle(x=1,p=5.0)
# >>>p2 = QuantumParticle(x=2,p=5.0)
# >>>p1.entangle(p2)
# >>>'Particle p1 is now in quantum entanglement with Particle p2'
# >>>p1 = QuantumParticle()
# >>>p2 = QuantumParticle()
# >>>p1.entangle(p2)
# >>>'Spooky Action at a Distance'
