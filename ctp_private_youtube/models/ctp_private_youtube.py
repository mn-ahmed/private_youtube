F=False
from odoo import api,fields as A,models as B,_
from odoo.http import request as D
from odoo.addons.http_routing.models.ir_http import url_for as E
from werkzeug import urls
class C(B.Model):
	_inherit='slide.slide';embed_code=A.Html('Embed Code',readonly=True,compute='_compute_embed_code',sanitize=F)
	@api.depends('document_id','slide_type','mime_type')
	def _compute_embed_code(self):
		B=D and D.httprequest.url_root
		for A in self:
			if not B:B=A.get_base_url()
			if B[-1]=='/':B=B[:-1]
			if A.datas and(not A.document_id or A.slide_type in['document','presentation']):G=B+E('/slides/embed/%s?page=1'%A.id);A.embed_code='<iframe src="%s" class="o_wslides_iframe_viewer" allowFullScreen="true" height="%s" width="%s" frameborder="0" oncontextmenu="return false;"></iframe>'%(G,315,420)
			elif A.slide_type=='video'and A.document_id:
				if not A.mime_type:C=urls.url_parse(A.url).query;C=C+'&theme=light'if C else'theme=light';A.embed_code='<iframe sandbox="allow-forms allow-scripts allow-pointer-lock allow-same-origin allow-top-navigation" src="//www.youtube-nocookie.com/embed/%s?%s&modestbranding=1&rel=0&fs=0" allowFullScreen="true" frameborder="0" autoplay="1" allow="autoplay" control="0" oncontextmenu="return false;"></iframe><div class="cpy1"/><div class="cpy4"/><div class="cpy3"/>'%(A.document_id,C)
				else:A.embed_code='<iframe sandbox="allow-forms allow-scripts allow-pointer-lock allow-same-origin allow-top-navigation"  src="//drive.google.com/file/d/%s/preview" allowFullScreen="true" frameborder="0" autoplay="1" allow="autoplay" control="0" oncontextmenu="return false;"></iframe><div class="cpy1"/><div class="cpy4"/><div class="cpy3"/>'%A.document_id
			else:A.embed_code=F