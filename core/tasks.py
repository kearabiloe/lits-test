from celery import Celery
import os
import logging

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lits_demo.settings')

app = Celery('tasks')


app.conf.update(BROKER_URL=os.environ.get('REDIS_URL', "redis://"),
                CELERY_RESULT_BACKEND=os.environ.get('REDIS_URL', 'redis://'),
                )

@app.task
def send_order_confirmation_email(sender,  *args, **kwargs):
    from django.core.mail import send_mail
    from core.models import Order

    try:
        if kwargs.get('instance') and kwargs.get('created'):
            order = kwargs.get('instance')
            if not order.notification_sent:
                print("Sending email")
                send_mail(
                    'Order {order} Confirmation'.format(order=order.id),
                    'We have recieved your order',
                    order.vendor.user.email,
                    [order.placed_by.email],
                    fail_silently=False,
                )
                order.notification_sent=True

    except Exception as e:
        logger.warning(e)
    return
