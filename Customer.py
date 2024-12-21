class Customer:
    def __init__(self, name, email, password):
        '''
        Args:
            name: str | name of customer
            email: str | email of customer
            password: str | password of customer
            uid: int | unique identifier for customer
            history: dict | key: datetime, value: details of items in order
            num_points: int | number of points customer has

        Returns: 
            None
        '''
        # initialize customer account attributes
        self.name = name
        self.email = email
        self.password = password
        self.uid = self.create_new_uid(self.name, self.email, self.password)
        self.history = {}
        self.num_points = 0

    def add_order_to_history(self, details, datetime, subtotal):
        """
        Args:
            details: str | details of items in order
            datetime: datetime | datetime of order
            subtotal: int | subtotal of order

        Returns:
            None
        """
        self.history[datetime] = details
        self.num_points += subtotal
    
    def redeem_points(self, points):
        """
        Args:
            points: int | points to redeem for reward

        Returns:
            None
        """
        self.num_points -= points
    
    def create_new_uid(self, name, email, password):
        """
        Args:
            name: str | name of customer
            email: str | email of customer
            password: str | password of customer

        Returns:
            uid: int | unique identifier for customer
        """
        return 0
    
    def get_freq_visit_after(self, datetime):
        """
        get frequency of visits after a certain datetime

        Args:
            datetime: datetime | datetime to check frequency of visits after

        Returns:
            freq: int | frequency of visits after datetime
        """
        freq = 0
        for order in self.history:
            if order[1] > self.datetime:
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
