import acopy
import pandas as pd
import matplotlib.pyplot as plt

class PrintingPlugin(acopy.solvers.SolverPlugin):

    def __init__(self,delta):
        super().__init__(delta=delta)
        self.delta = delta
        print("ADJACENCY MATRIX")
        print(self.delta)
        self.counter = 0
        ## ENTER OPTIMAL ROUTE, COST AND NUMBER OF ITERATIONS HERE

        #self.optimal_route = [0,7,6,4,5,9,12,1,2,11,10,8,3]
        self.optimal_route = [0,1,3,2]
        self.optimal_cost = 9
        self.number_of_iterations = 30

        self.optimal_route_dist = []
        till = 0
        for i in range(1,len(self.optimal_route)):
            till = till + self.delta[self.optimal_route[i-1],self.optimal_route[i]]
            self.optimal_route_dist.append(till)

        self.payoff_list=[]
        self.payoff_matrix = []
        for i in range(0,len(self.optimal_route)):
            inner_list = []
            inner_list.append(i)
            self.payoff_matrix.append(inner_list)
        print("INITIAL")
        print(self.payoff_matrix)

    def on_iteration(self, state):
        print("===========================================")
        print("ITERATION NUMBER  = {}".format(self.counter))
        print("===========================================")
        print(" ")
        print("ALL AVAILABLE SOLUTIONS!!!")
        print("===========================================")
        print(state.solutions)
        print("===========================================")
        self.counter=self.counter+1
        print("Best Solution")
        print(state.best)
        s = str(state.best)
        print("CHIN")
        index = s.index('0,')
        current_cost = int(s[:index])
        print(current_cost)
        # print("RECORD")
        # record_cost = int(str(state.record)[:2])
        
        # print(record_cost)
        actual_route = s[index:]
        print("ACTUAL ROUTE")
        print(actual_route)
        if current_cost == self.optimal_cost:
            for i in range(0,len(self.optimal_route)):
                payoff = 0
                self.payoff_matrix[i].append(payoff)
            
        else:



            rroute_list = actual_route.split(',')
            route_list = []
            for r in rroute_list:
                route_list.append(int(r))
            weight_till = 0
            curr_diff = 0
            opt_weight_till = 0
            payoff = 0
            print("IMPOPOPO")
            print(route_list)
            till = 0
            actual_route_dist = []
            for i in range(1,len(self.optimal_route)):
                till = till + self.delta[route_list[i-1],route_list[i]]
                actual_route_dist.append(till)
            print("PAYOFFFSSSS")

            for i in range(0,len(self.optimal_route)):
                payoff = self.optimal_route_dist[self.optimal_route.index(i)-1] - actual_route_dist[route_list.index(i)-1]
                self.payoff_matrix[i].append(payoff)
                print(payoff)
        

    def on_finish(self, state):
        ll = []
        iterations = self.number_of_iterations + 1
        for i in range(1,(iterations)):
            ll.append(i)

        for l in self.payoff_matrix:
            l.pop(0)
        
        ctr = 1;
        for l in self.payoff_matrix:
            plt.plot(ll,l)
            s = "Node " + str(ctr)
            ctr = ctr+1;

            plt.savefig(s)
            plt.close()