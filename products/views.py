from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
import products.models
from .forms import CommentForm
from .models import Product, Comment, ActiveCommentManager
from cart.forms import AddCartForm
from cart.cart import Cart
from cart.views import cart_detail_view, add_to_cart_view

class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDietailView(generic.DetailView):
    model = Product
    template_name = 'products/detial_view.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.object
        cart = Cart(self.request).cart
        quantity_cart=0
        product_id_str = str(self.kwargs.get('pk'))
        if product_id_str in cart:
            quantity_cart = cart[product_id_str]['quantity']
        context['comments']=products.comments(manager='active_comments').all()
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddCartForm
        context['quantity'] = quantity_cart
        return context





class CreateCommentForm(generic.CreateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.auther = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        messages.success(self.request,message=_('your comment is succsfully.'))
        return super().form_valid(form)




