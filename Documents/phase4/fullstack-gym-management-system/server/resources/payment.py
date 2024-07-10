from flask_restful import Resource, reqparse
from models import Payment, db

class PaymentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('member_id', type=int, required=True, help='Member ID cannot be blank.')
    parser.add_argument('amount', type=float, required=True, help='Amount cannot be blank.')
    parser.add_argument('date', type=str, required=True, help='Date cannot be blank.')

    def get(self, payment_id=None):
        if payment_id:
            payment = Payment.query.get(payment_id)
            if payment:
                return payment.to_dict()
            return {'message': 'Payment not found'}, 404
        payments = Payment.query.all()
        return [payment.to_dict() for payment in payments]

    def post(self):
        data = PaymentResource.parser.parse_args()
        new_payment = Payment(member_id=data['member_id'], amount=data['amount'], date=data['date'])
        db.session.add(new_payment)
        db.session.commit()
        return new_payment.to_dict(), 201

    def put(self, payment_id):
        data = PaymentResource.parser.parse_args()
        payment = Payment.query.get(payment_id)
