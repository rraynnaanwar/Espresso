class Customer:
    def __init__(self, name, email, password):
        '''
        uid: int | unique identifier for customer
        email: str | email of customer
        password: str | password of customer
        uid: int | unique identifier for customer
        history: list of tuples (details, datetime)
        num_points: int | number of points customer has
        '''
        self.name = name
        self.email = email
        self.password = password
        self.uid = self.create_new_uid(self.name, self.email, self.password)
        self.history = {}
        self.num_points = 0
    
    def add_order_to_history(self, details, datetime, subtotal):
        """
        details: str | details of items in order
        datetime: datetime | datetime of order
        subtotal: int | subtotal of order
        """
        self.history[datetime] = details
        self.num_points += subtotal
    
    def redeem_points(self, points):
        """
        points: int | points to redeem for reward
        """
        self.num_points -= points
    
    def create_new_uid(self, name, email, password):
        """
        create a new uid for customer based on name, email, and password

        name: str | name of customer
        email: str | email of customer
        password: str | password of customer
        """
        return 0
    
    def get_freq_visit_after(self, datetime):
        """
        get frequency of visits after a certain datetime

        datetime: datetime | datetime to check frequency of visits after
        """
        freq = 0
        for order in self.history:
            if order[1] > datetime:
                freq += 1
        return freq
    
    # getters
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_uid(self):
        return self.uid

    def get_history(self):
        return self.history

    def get_num_points(self):
        return self.num_points
