
def scores_counter(scores_list):
    for score_list in scores_list:
        if 1 <= score_list <= 5:
            print("Negative Score")
        elif 5<= score_list <= 8:
            print("Neutral")
        else:
            print("Positive")

scores_counter([1,2,3,4,5,6,7,8,9,10])



def purchases_100(sales):
    count = 0                           # Set a counter of totals > 100
    for customer in sales:              # Loop over each inner list
        customer_total = 0              # Set 0 value of purchases for the inner list
        for purchase in customer:       # For price in inner list:
            customer_total += purchase  # Add the price to value of purchases for inner list
        if customer_total >= 100:       # After looping over all prices in inner list, if
                                        # total >= 100
            count+=1                    # Increment the counter
    return count
