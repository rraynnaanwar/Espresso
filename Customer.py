class Customer:
    def __init__(self, name, email, password):
        '''
        Args:
            name (str): the name of the customer
            email (str): the email of the customer
            password (str): the password of the customer
            uid (int): the unique identifier for the customer
            history (dict): key: datetime, value: details of items in order
            num_points (int): the number of points the customer has

        Returns: 
            void: None
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
            details (str): the details of items in order
            datetime (datetime): the datetime of order
            subtotal (int): the subtotal of order

        Returns:
            void: None
        """
        self.history[datetime] = details
        self.num_points += subtotal
    
    def redeem_points(self, points):
        """
        Args:
            points (int): the points to redeem for reward

        Returns:
            void: None
        """
        self.num_points -= points
    
    def create_new_uid(self, name, email, password):
        """
        Args:
            name (str): the name of the customer
            email (str): the email of the customer
            password (str): the password of the customer

        Returns:
            uid (int): the unique identifier for the customer
        """
        return 0
    
    def get_freq_visit_after(self, datetime):
        """
        gets the frequency of visits after a certain datetime

        Args:
            datetime (datetime): the datetime to check frequency of visits after

        Returns:
            freq (int): the frequency of visits after datetime
        """
        freq = 0
        for order in self.history:
            if order[1] > self.datetime:
                freq += 1
        return freq
    
    def get_total_freq_visit(self):
        """
        gets the total frequency of visits

        Returns:
            freq (int): the total frequency of visits
        """
        return len(self.history)
    
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
