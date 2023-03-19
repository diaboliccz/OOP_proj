from payment import Payment, CardPayment

payment_test_obj1 = Payment(500, "15-03-2023")
payment_test_obj2 = Payment(1000, "16-03-2023")
payment_test_obj3 = Payment(1500, "17-03-2023")
payment_test_obj4 = Payment(2000, "18-03-2023")
payment_test_obj4.make_payment()

CreditCard1 = CardPayment(500, "18-03-2023", "Kolawat Inpan", "1234 4321 2562 2512", "01/28", 601)
CreditCard1.make_payment()