from django.db.models.signals import post_save
from django.dispatch import receiver
from user_app.models import User
from cart_app.models import Cart  

@receiver(post_save, sender=User)
# post_save：信号在模型的实例保存（创建或更新）后触发。
# sender=User：指定信号的发送者是 User 模型。也就是说，只有在 User 模型的实例保存后，信号才会触发。
def create_user_cart(sender, instance, created, **kwargs):
# sender：发送信号的模型类，这里是 User 模型。它表示哪个模型实例触发了信号。
# instance：当前触发信号的 User 实例，即被保存（创建或更新）的用户对象。
# created：一个布尔值，指示该 User 实例是否是新创建的。如果是新创建的，created 为 True；如果是更新已有的用户，created 为 False。
# **kwargs：传入的其他额外的关键字参数，通常用于接收额外的信息（例如 update_fields）。这里没有使用它。
    """用户创建后自动创建购物车"""
    if created:  # 仅当用户是新创建时触发（避免更新用户时重复创建）
        Cart.objects.create(user=instance)  # 创建购物车，关联当前用户