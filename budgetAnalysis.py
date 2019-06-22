#Mark A
#1-6-2013

#Pg.199 Budget Analysis.

def main():

    #Collects data.

    Budget = int(input('Enter the your months budget: '))

    Costs(Budget)

def Costs(Budget):

    TotalExpenses = 0

    #Creates loop to find costs in a month.

    Month = 0
    while Month < 1:
        Cost = int(input('Enter your costs so far for the month: '))
        Done = int(input('Do you have more costs to enter? Yes(1) No(2) '))
        print()
        
        TotalExpenses = TotalExpenses + Cost


        Done == 1

        #Calculates if person is over, under, or equall to their months budget
        #and displays data.

        if Done == 2:
            print('Your total expenses for this month are $', TotalExpenses)
            Month = 1

            if TotalExpenses < Budget:
                UnderBudget = Budget - TotalExpenses
                print('You are under budget by $', UnderBudget)

            elif TotalExpenses > Budget:
                OverBudget = TotalExpenses - Budget
                print('You are over budget by $', OverBudget)

            elif TotalExpenses == Budget:
                EquallBudget = TotalExpenses - Budget
                print('You expenses were equall of your budget at $', EquallBudget)

main()


#Sample Runs

#Test Run 1

##Enter the your months budget: 500
##Enter your costs so far for the month: 250
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 250
##Do you have more costs to enter? Yes(1) No(2) 2
##Your total expenses for this month are $ 500 .
##You expenses were equall of your budget at $ 0

#Test Run 2

##Enter the your months budget: 1000
##Enter your costs so far for the month: 90
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 500
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 60
##Do you have more costs to enter? Yes(1) No(2) 2
##Your total expenses for this month are $ 650 .
##You are under budget by $ 350

#Test Run 3

##Enter the your months budget: 10000
##Enter your costs so far for the month: 900
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 500
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 800
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 5000
##Do you have more costs to enter? Yes(1) No(2) 2
##Your total expenses for this month are $ 7200 .
##You are under budget by $ 2800

#Test Run 4

##Enter the your months budget: 900
##Enter your costs so far for the month: 1000
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 500
##Do you have more costs to enter? Yes(1) No(2) 2
##Your total expenses for this month are $ 1500 .
##You are over budget by $ 600

#Test Run 5

##Enter the your months budget: 800
##Enter your costs so far for the month: 500
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 200
##Do you have more costs to enter? Yes(1) No(2) 1
##Enter your costs so far for the month: 700
##Do you have more costs to enter? Yes(1) No(2) 2
##Your total expenses for this month are $ 1400 .
##You are over budget by $ 600


