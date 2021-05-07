# [TO DO]:


from bayesian_network import BayesianNetwork


if __name__ == "__main__":
    net = BayesianNetwork('assets/alarm.json')
    print(net)

    # net.markov_blanket()
    net.markov_blanket('burglary')
    # print("-------------------------------------------------")
    # # res = net.MCMC(evidence={"burglary":1}, query=["John_calls", "earthquake", "alarm", "Marry_calls"])
    # res = net.mcmc(evidence={"burglary":1}, query=["John_calls"], step=1000)

    # {burglary:\\\"T\\\"} -q John_calls,earthquake,alarm,Marry_calls -s 1000000"


    # res = net.MCMC(evidence={"burglary":1}, query=["John_calls", "earthquake", "alarm", "Marry_calls"])
    # {'T': 0, 'F': 1.0000000000000007}
    # {“John_calls” : {“F”: 0.095, “T”: 0.905}}

    # print(net)
    # print(net)
    # net.markov_blanket('burglary')