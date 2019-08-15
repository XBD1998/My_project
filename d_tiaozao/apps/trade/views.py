from django.shortcuts import render, HttpResponse


#商品浏览模块
def goods_list(request):
    return render(request, 'goods_list.html')

def sale_history(request):
    return render(request, 'sale_history.html')
# #商品详情页模块
# def goodsDetail(req):
#     if not req.session.get('islogin'):
#         msg = '你还未登陆，请先登陆！'
#         return render_to_response('error_msg.html', locals())
#     if req.method == 'GET':
#         data = req.GET
#         goods_detail = controller.get_goods_detail(data)
#         return render_to_response('goods_detail.html', locals(), context_instance=RequestContext(req))
#     if req.method == 'POST':
#         data = req.POST
#         buyer_id = req.session['user_info']['uid']
#         rt = controller.purchase(data, buyer_id)
#         if rt == 1:
#             msg = '购买成功，请返回主页！'
#         else:
#             msg = '购买失败，请联系管理员！！'
#         return render_to_response('error_msg.html', locals(), context_instance=RequestContext(req))
#
#
# #购买记录模块
# def buyHis(req):
#     if not req.session.get('islogin'):
#         msg = '你还没登录，先登录吧....'
#         return render_to_response('error_msg.html', locals(), context_instance=RequestContext(req))
#     buyer_id = req.session['user_info']['uid']
#     id_group = []
#     #将购买者id装入列表后传入controller，是为了迎合controller的处理
#     id_group.append((buyer_id, None))
#     result = controller.trade_his(id_group)
#     return render_to_response('buy_history.html', locals(), context_instance=RequestContext(req))
