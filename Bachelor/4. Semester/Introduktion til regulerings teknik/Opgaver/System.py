import bdsim 
class customFilter(bdsim.components.FunctionBlock): 
    nin = 1
    nout = 1

    def __init__(
        self, num, den, **blockargs
    ):
        """
        :param K: The gain value, defaults to 1
        :type K: scalar, array_like
        :param premul: premultiply by constant, default is postmultiply, defaults to False
        :type premul: bool, optional
        :param blockargs: |BlockOptions|
        :type blockargs: dict

        """
        super().__init__(**blockargs)
        self.num = num
        self.den = den
       

        self.add_param("num")
        self.add_param("den")

    def output(self, t, inports, x):
        input = inports[0]

        if isinstance(input, np.ndarray) and isinstance(self.K, np.ndarray):
            # array x array case
            # numerator = np.empty_like(s.shape)
            # denominator = np.empty_like(s.shape)
            # func = np.empty_like(s.shape)
            for i in reversed(range(len(num))): # Læg tæller til
                    numerator += num[i]*(s**i)
            for i in reversed(range(len(num))):
                denominator += den[i]*(s**i)
            func = numerator / denominator
            if self.premul:  
                # premultiply
                print(input.shape)
                return [input]
            else:
                print(input.shape)
                # postmultiply by gain
                return [input]
        else:
            print(input.shape)
            return [input]



sim = bdsim.BDSim(animation=True)  # create simulator
bd = sim.blockdiagram()  # create an empty block diagram
bd = bdsim.bdload(bd, "System.bd")
# Hvilken path skal der være? 

# define the blocks
demand = bd.STEP(T=1, name="demand")
add = bd.SUM("++")
gain = bd.GAIN(17.4)

K = 17.4
num = [K] # 0s^2 + 0s + K  
den = [1, 5, K] # G1 * G2 = s^2 +5s + K
plant = bd.LTI_SISO(0.5, [2, 1], name="plant") 
# filter = customFilter(num, den)
#out = bd.SCOPE(styles=["k", "r--"], loc="lower right")

# connect the blocks
bd.connect(demand, add[0])
bd.connect(plant, add[1]) # Feedback
bd.connect(add, gain)
bd.connect(gain, plant)


bd.compile()  # check the diagram
# sim.report(bd)  # , format="latex")
sim.report(bd, "schedule")



# out = sim.run(bd, T=5)  # , watch=[demand, sum])  # simulate for 5s
out = sim.run(bd, watch=[plant, demand])  # simulate for 5s
bd.done()
print(out)