from io import BytesIO

from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import get_template


def render_pdf_view(context):
    template_path = 'to_pdf.html'    
    response = HttpResponse(content_type='application/pdf')    
    response['Content-Disposition'] = 'filename="report.pdf"'    
    template = get_template(template_path)
    html = template.render(context)    
    pisa_status = pisa.CreatePDF(
        html.encode('utf-8'), dest=response,
        encoding='utf-8')    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')    
    return response


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    html = html.encode('cp1251')
    print(html)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None