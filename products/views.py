from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
import products.models
from .forms import CommentForm
from .models import Product, Comment, ActiveCommentManager



class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDietailView(generic.DetailView):
    model = Product
    template_name = 'products/detial_view.html'
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.object
        context['comments']=products.comments(manager='active_comments').all()
        context['comment_form'] = CommentForm()
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




