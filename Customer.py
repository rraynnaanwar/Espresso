class Customer:
    def __init__(self, uid, history, num_points):
        self.uid = uid
        self.history = history
        self.num_points = num_points
    
    def add_order(self, details, datetime, subtotal):
        self.history.append((details, datetime))
        self.num_points += subtotal
    
    def redeem_points(self, points):
        self.num_points -= points

    def get_freq_visit_before(self, datetime):
        freq = 0
        for order in self.history:
            if order[1] > datetime:
                freq += 1
        return freq
    
    def get_uid(self):
        return self.uid

    def get_history(self):
        return self.history

    def get_num_points(self):
        return self.num_points
